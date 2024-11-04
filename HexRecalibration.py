"""
QGIS Model to recalibrate split hexes based on their domain location
Name : hex_border
Group : 
With QGIS : 33203
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Hex_border(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('hex1', 'Hex1', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('hex10', 'Hex10', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('hex2', 'Hex2', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('hex3', 'Hex3', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('hex4', 'Hex4', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('hex5', 'Hex5', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('hex6', 'Hex6', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('hex7', 'Hex7', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('hex8', 'Hex8', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('hex9', 'Hex9', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out9', 'out9', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out10', 'out10', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out1', 'out1', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out2', 'out2', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out3', 'out3', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out4', 'out4', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out5', 'out5', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out6', 'out6', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out7', 'out7', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Out8', 'out8', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(73, model_feedback)
        results = {}
        outputs = {}

        # Extract layer extent 5
        alg_params = {
            'INPUT': parameters['hex5'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent5'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Extract layer extent 7
        alg_params = {
            'INPUT': parameters['hex7'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent7'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Extract layer extent 4
        alg_params = {
            'INPUT': parameters['hex4'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent4'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Extract layer extent 3
        alg_params = {
            'INPUT': parameters['hex3'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent3'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Extract layer extent 1
        alg_params = {
            'INPUT': parameters['hex1'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent1'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 3
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent3']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines3'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 7
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent7']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines7'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 4
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent4']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines4'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 5
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent5']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines5'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(9)
        if feedback.isCanceled():
            return {}

        # Extract by location 4
        alg_params = {
            'INPUT': parameters['hex4'],
            'INTERSECT': outputs['PolygonsToLines4']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation4'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(10)
        if feedback.isCanceled():
            return {}

        # Extract layer extent 8
        alg_params = {
            'INPUT': parameters['hex8'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent8'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(11)
        if feedback.isCanceled():
            return {}

        # Extract layer extent 10
        alg_params = {
            'INPUT': parameters['hex10'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent10'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(12)
        if feedback.isCanceled():
            return {}

        # Extract by location 5
        alg_params = {
            'INPUT': parameters['hex5'],
            'INTERSECT': outputs['PolygonsToLines5']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation5'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(13)
        if feedback.isCanceled():
            return {}

        # Extract layer extent 2
        alg_params = {
            'INPUT': parameters['hex2'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent2'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(14)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 10
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent10']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines10'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(15)
        if feedback.isCanceled():
            return {}

        # Extract by location 7
        alg_params = {
            'INPUT': parameters['hex7'],
            'INTERSECT': outputs['PolygonsToLines7']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation7'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(16)
        if feedback.isCanceled():
            return {}

        # Extract layer extent 9
        alg_params = {
            'INPUT': parameters['hex9'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent9'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(17)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 8
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent8']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines8'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(18)
        if feedback.isCanceled():
            return {}

        # Extract by location 3
        alg_params = {
            'INPUT': parameters['hex3'],
            'INTERSECT': outputs['PolygonsToLines3']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation3'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(19)
        if feedback.isCanceled():
            return {}

        # Extract layer extent 6
        alg_params = {
            'INPUT': parameters['hex6'],
            'ROUND_TO': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractLayerExtent6'] = processing.run('native:polygonfromlayerextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(20)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 9
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent9']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines9'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(21)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 2
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent2']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines2'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(22)
        if feedback.isCanceled():
            return {}

        # Extract by location 9
        alg_params = {
            'INPUT': parameters['hex9'],
            'INTERSECT': outputs['PolygonsToLines9']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation9'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(23)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 1
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent1']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines1'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(24)
        if feedback.isCanceled():
            return {}

        # Extract by location 8
        alg_params = {
            'INPUT': parameters['hex8'],
            'INTERSECT': outputs['PolygonsToLines8']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation8'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(25)
        if feedback.isCanceled():
            return {}

        # Extract by location 10
        alg_params = {
            'INPUT': parameters['hex10'],
            'INTERSECT': outputs['PolygonsToLines10']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation10'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(26)
        if feedback.isCanceled():
            return {}

        # Polygons to lines 6
        alg_params = {
            'INPUT': outputs['ExtractLayerExtent6']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PolygonsToLines6'] = processing.run('native:polygonstolines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(27)
        if feedback.isCanceled():
            return {}

        # Extract by location 6
        alg_params = {
            'INPUT': parameters['hex6'],
            'INTERSECT': outputs['PolygonsToLines6']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation6'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(28)
        if feedback.isCanceled():
            return {}

        # Extract by location 1
        alg_params = {
            'INPUT': parameters['hex1'],
            'INTERSECT': outputs['PolygonsToLines1']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation1'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(29)
        if feedback.isCanceled():
            return {}

        # Extract by location 2
        alg_params = {
            'INPUT': parameters['hex2'],
            'INTERSECT': outputs['PolygonsToLines2']['OUTPUT'],
            'PREDICATE': [0,4,5,7],  # intersect,touch,overlap,cross
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByLocation2'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(30)
        if feedback.isCanceled():
            return {}

        # Merge vector layers
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractByLocation1']['OUTPUT'],outputs['ExtractByLocation10']['OUTPUT'],outputs['ExtractByLocation2']['OUTPUT'],outputs['ExtractByLocation3']['OUTPUT'],outputs['ExtractByLocation4']['OUTPUT'],outputs['ExtractByLocation5']['OUTPUT'],outputs['ExtractByLocation6']['OUTPUT'],outputs['ExtractByLocation7']['OUTPUT'],outputs['ExtractByLocation8']['OUTPUT'],outputs['ExtractByLocation9']['OUTPUT']],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['MergeVectorLayers'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(31)
        if feedback.isCanceled():
            return {}

        # Dissolve
        alg_params = {
            'FIELD': ['GRID_ID'],
            'INPUT': outputs['MergeVectorLayers']['OUTPUT'],
            'SEPARATE_DISJOINT': False,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Dissolve'] = processing.run('native:dissolve', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(32)
        if feedback.isCanceled():
            return {}

        # Centroids
        alg_params = {
            'ALL_PARTS': False,
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Centroids'] = processing.run('native:centroids', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(33)
        if feedback.isCanceled():
            return {}

        # Difference 9
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex9'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference9'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(34)
        if feedback.isCanceled():
            return {}

        # Extract centroids 4
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent4']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids4'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(35)
        if feedback.isCanceled():
            return {}

        # Extract centroids 8
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent8']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids8'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(36)
        if feedback.isCanceled():
            return {}

        # Extract centroids 7
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent7']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids7'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(37)
        if feedback.isCanceled():
            return {}

        # Extract centroids 10
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent10']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids10'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(38)
        if feedback.isCanceled():
            return {}

        # Difference 6
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex6'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference6'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(39)
        if feedback.isCanceled():
            return {}

        # Extract centroids 6
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent6']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids6'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(40)
        if feedback.isCanceled():
            return {}

        # Extract hexes 7
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids7']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes7'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(41)
        if feedback.isCanceled():
            return {}

        # Extract centroids 1
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent1']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids1'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(42)
        if feedback.isCanceled():
            return {}

        # Difference 7
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex7'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference7'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(43)
        if feedback.isCanceled():
            return {}

        # Difference 8
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex8'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference8'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(44)
        if feedback.isCanceled():
            return {}

        # Merge 7
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractHexes7']['OUTPUT'],outputs['Difference7']['OUTPUT']],
            'OUTPUT': parameters['Out7']
        }
        outputs['Merge7'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out7'] = outputs['Merge7']['OUTPUT']

        feedback.setCurrentStep(45)
        if feedback.isCanceled():
            return {}

        # Difference 2
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex2'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference2'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(46)
        if feedback.isCanceled():
            return {}

        # Difference 1
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex1'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference1'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(47)
        if feedback.isCanceled():
            return {}

        # Extract centroids 9
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent9']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids9'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(48)
        if feedback.isCanceled():
            return {}

        # Extract centroids 2
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent2']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids2'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(49)
        if feedback.isCanceled():
            return {}

        # Extract hexes 1
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids1']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes1'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(50)
        if feedback.isCanceled():
            return {}

        # Extract centroids 3
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent3']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids3'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(51)
        if feedback.isCanceled():
            return {}

        # Extract hexes 4
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids4']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes4'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(52)
        if feedback.isCanceled():
            return {}

        # Merge 1
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['Difference1']['OUTPUT'],outputs['ExtractHexes1']['OUTPUT']],
            'OUTPUT': parameters['Out1']
        }
        outputs['Merge1'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out1'] = outputs['Merge1']['OUTPUT']

        feedback.setCurrentStep(53)
        if feedback.isCanceled():
            return {}

        # Difference 3
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex3'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference3'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(54)
        if feedback.isCanceled():
            return {}

        # Difference 5
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex5'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference5'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(55)
        if feedback.isCanceled():
            return {}

        # Difference 4
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex4'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference4'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(56)
        if feedback.isCanceled():
            return {}

        # Extract centroids 5
        alg_params = {
            'INPUT': outputs['Centroids']['OUTPUT'],
            'INTERSECT': outputs['ExtractLayerExtent5']['OUTPUT'],
            'PREDICATE': [6],  # are within
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractCentroids5'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(57)
        if feedback.isCanceled():
            return {}

        # Difference 10
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters['hex10'],
            'OVERLAY': outputs['Dissolve']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Difference10'] = processing.run('native:difference', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(58)
        if feedback.isCanceled():
            return {}

        # Extract hexes 8
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids8']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes8'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(59)
        if feedback.isCanceled():
            return {}

        # Extract hexes 5
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids5']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes5'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(60)
        if feedback.isCanceled():
            return {}

        # Extract hexes 10
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids10']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes10'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(61)
        if feedback.isCanceled():
            return {}

        # Merge 5
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractHexes5']['OUTPUT'],outputs['Difference5']['OUTPUT']],
            'OUTPUT': parameters['Out5']
        }
        outputs['Merge5'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out5'] = outputs['Merge5']['OUTPUT']

        feedback.setCurrentStep(62)
        if feedback.isCanceled():
            return {}

        # Extract hexes 2
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids2']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes2'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(63)
        if feedback.isCanceled():
            return {}

        # Extract hexes 6
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids6']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes6'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(64)
        if feedback.isCanceled():
            return {}

        # Merge 10
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractHexes10']['OUTPUT'],outputs['Difference10']['OUTPUT']],
            'OUTPUT': parameters['Out10']
        }
        outputs['Merge10'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out10'] = outputs['Merge10']['OUTPUT']

        feedback.setCurrentStep(65)
        if feedback.isCanceled():
            return {}

        # Extract hexes 3
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids3']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes3'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(66)
        if feedback.isCanceled():
            return {}

        # Extract hexes 9
        alg_params = {
            'INPUT': outputs['Dissolve']['OUTPUT'],
            'INTERSECT': outputs['ExtractCentroids9']['OUTPUT'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractHexes9'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(67)
        if feedback.isCanceled():
            return {}

        # Merge 4
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractHexes4']['OUTPUT'],outputs['Difference4']['OUTPUT']],
            'OUTPUT': parameters['Out4']
        }
        outputs['Merge4'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out4'] = outputs['Merge4']['OUTPUT']

        feedback.setCurrentStep(68)
        if feedback.isCanceled():
            return {}

        # Merge 3
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractHexes3']['OUTPUT'],outputs['Difference3']['OUTPUT']],
            'OUTPUT': parameters['Out3']
        }
        outputs['Merge3'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out3'] = outputs['Merge3']['OUTPUT']

        feedback.setCurrentStep(69)
        if feedback.isCanceled():
            return {}

        # Merge 8
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractHexes8']['OUTPUT'],outputs['Difference8']['OUTPUT']],
            'OUTPUT': parameters['Out8']
        }
        outputs['Merge8'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out8'] = outputs['Merge8']['OUTPUT']

        feedback.setCurrentStep(70)
        if feedback.isCanceled():
            return {}

        # Merge 6
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractHexes6']['OUTPUT'],outputs['Difference6']['OUTPUT']],
            'OUTPUT': parameters['Out6']
        }
        outputs['Merge6'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out6'] = outputs['Merge6']['OUTPUT']

        feedback.setCurrentStep(71)
        if feedback.isCanceled():
            return {}

        # Merge 9
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractHexes9']['OUTPUT'],outputs['Difference9']['OUTPUT']],
            'OUTPUT': parameters['Out9']
        }
        outputs['Merge9'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out9'] = outputs['Merge9']['OUTPUT']

        feedback.setCurrentStep(72)
        if feedback.isCanceled():
            return {}

        # Merge 2
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['ExtractHexes2']['OUTPUT'],outputs['Difference2']['OUTPUT']],
            'OUTPUT': parameters['Out2']
        }
        outputs['Merge2'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Out2'] = outputs['Merge2']['OUTPUT']
        return results

    def name(self):
        return 'hex_border'

    def displayName(self):
        return 'hex_border'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Hex_border()
