# -*- coding: utf-8 -*-
"""
Created on Fri Nov 1 2024
@author: Chris Raczynski
"""

# Multi-layer merge by centroid script
# This script runs a centroid based join for the H3 hex grid.
# ProcessPoolExecutor used for multiprocessing of each segment

# Import modules
import geopandas as gpd
import fiona
import pandas as pd
from concurrent.futures import ProcessPoolExecutor

# --------- >>> EDIT BLOCK <<< -------------

# Define hex level
hexLevel = '5'
# Names of layers to join in the list, determines the order of joins
layersToJoin = ['tl_2021_us_county', 'Estuarine_Drainage_Areas', 'WBDHUC8', 'dtl_cnty_Census_ESRI', 'WBDHUC12', 'SVI_tract']

# Path to hex grid input database
# Level 10 segments are here "K://projects/rgmg/MSGeoProject/Projects/Grid_Effort/H3_L10_NoOverlap10_sgm.gdb"
hexGdb = r"C://Users/chrisr/hex_svi/fixed/HexDomain.gdb"

# Path to the geodatabase with layers to join
inputsGdb = r'K://projects/rgmg/MSGeoProject/Projects/Grid_Effort/H3_10segments.gdb'

# Path to output database with autonaming
outputGdb = "C:/Users/chrisr/hex_svi/fixed/H"+hexLevel+"_DomainOutput.gdb"

# --------- >>> END EDIT BLOCK <<< ---------

# Segments that hold input data
segments = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Main body function for processing
def dataProcessor(args):
    '''
    Function to run in multiprocessing to perform spatial join on each segment
    based on the hex centroid.

    Parameters
    ----------
    hexInput : string, path 
        Path to the location of input database holding H3 hexes in segments.
    joinInputs : string, path 
        Path to the location of input database holding layers to join to hexes.
    segmentId : string
        Segment identifier passed from segments to multiprocessor.

    Returns
    -------
    baseLayer : GeoDataFrame
        Output GeoDataFrame based on H3 hexes with joinInputs joined., 

    '''
    hexInput, joinInputs, segmentId = args
    
    # Define layer identificator
    # on level 10, naming is: 'H3_L10_S'+segmentId
    layerId = 'H'+hexLevel+'_'+segmentId
    
    # Read in the hex polygon grid layer as the base layer
    baseLayer = gpd.read_file(hexGdb, layer=layerId)
    baseLayer.drop(columns=['Shape_Length', 'Shape_Area'], inplace=True)
    
    # Calculate the centroids of the hexes for the spatial join, but keep the original geometries
    baseCentroids = baseLayer.copy()
    baseCentroids['geometry'] = baseLayer['geometry'].centroid
    
    # Ensure the geometry column is set correctly for centroids
    baseCentroids = baseCentroids.set_geometry('geometry')

    # Read the joined layers into a dictionary
    layerGdfs = {layer: gpd.read_file(inputsGdb, layer=layer) for layer in layersToJoin}

    # Check if garbage data is present and try to remove it
    for name, gdf in layerGdfs.items():
        # Ensure the CRS is the same between the base layer and the current layer
        if not gdf.crs == baseCentroids.crs:
            gdf = gdf.to_crs(baseCentroids.crs)
        
        # Check if garbage data is present and remove it
        if 'Shape_Length' in gdf.columns:
            gdf.drop('Shape_Length', axis=1, inplace=True)
        if 'Shape_Area' in gdf.columns:
            gdf.drop('Shape_Area', axis=1, inplace=True)
    
        # Check for duplicate column names and rename them before the join, but don't rename 'geometry'
        for col in gdf.columns:
            if col in baseCentroids.columns and col != 'geometry':
                gdf.rename(columns={col: col + '_joined'}, inplace=True)
        
        # Set the geometry column to ensure spatial join works
        gdf = gdf.set_geometry('geometry')
    
        # Perform spatial join using centroids of base_layer hexes
        joinResult = gpd.sjoin(baseCentroids, gdf, how="left")
    
        # Transfer the join result back to the original base_layer (with full hex geometries)
        baseLayer = baseLayer.join(joinResult.drop(columns='geometry'), rsuffix='_joined')
    
        # Drop the `index_right` column if it exists
        if 'index_right' in baseLayer.columns:
            baseLayer.drop('index_right', axis=1, inplace=True)

    # After the join, check for any duplicated columns and rename them to avoid conflicts
    baseLayer = baseLayer.loc[:, ~baseLayer.columns.duplicated()]
    
    # return result
    return baseLayer


# Run segments in muliprocessing
if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        # Collect results into a list by mapping the function to the list of numbers
        results = list(executor.map(dataProcessor, [(hexGdb, inputsGdb, seg) for seg in segments]))
    # Save each GeoDataFrame in the results list to a separate layer in the geodatabase
    for i, gdf in enumerate(results):
        layerName = "H"+hexLevel+f"_{i+1}"  # Create a unique layer name for each GeoDataFrame
        gdf.drop(['OBJECTID_1','Shape_Leng','layer','path','OBJECTID_1_joined','GRID_ID_joined','Shape_Leng_joined','layer_joined','path_joined','HUC12_TYPE'], axis=1, inplace=True)
        gdf.to_file(outputGdb, driver="OpenFileGDB", layer=layerName)
