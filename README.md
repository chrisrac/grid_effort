# H3 hexagonal grid processor  
Hex grid analysis working directory.
<br>
<br>
This repository contains scripts used for H3 grid processing. <br>
<br>
Grid was divided into 10 chunks on all levels 5-10. Some slicing errors were present. To fix them, [HexRecalibration](https://github.com/chrisrac/grid_effort/blob/main/HexRecalibration.py) was used, to grab sliced hexes, merge them and reasign to segment according to centroid location.
<br>
Use [centroidMultiprocessor](https://github.com/chrisrac/grid_effort/blob/main/centroidMultiprocessor.py) to run segments in parallel on 10 CPUs.<br>
The result is saved into single gdb. Instructions in the file.<br>
<br>
Level 10 hex were computed on Orion HPC due to domain size. <br>
All results are in K drive, in Grid_Effort project, DomainOutputs folder. <br> 
<br>
<br>
Initial analysis on timing and code simplification were run. Results are in timing_analysis folder. <br>
File [timing_results](https://github.com/chrisrac/grid_effort/blob/main/timing_analysis/timing_results.ipynb) contains summarized timing experiments for initial domain. 


