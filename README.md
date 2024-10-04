# HEX Grid effort 
Hex grid analysis working directory.
<br>
<br>
This contains timing experiment and code simplification for basic runs.
<br>
<br>
File [timing_results](https://github.com/chrisrac/grid_effort/blob/main/timing_results.ipynb) contains summarized timing experiments. This was run with [timing_script](https://github.com/chrisrac/grid_effort/blob/main/timing_script.ipynb), h10 is too big for 64GB memory and requires either slicing or HPC to run.
<br>
<br>
File [Single_merge](https://github.com/chrisrac/grid_effort/blob/main/Single_merge.ipynb) is used to merge one layer to grid.
<br>
<br>
File [Multi_merge](https://github.com/chrisrac/grid_effort/blob/main/Multi_merge.ipynb) joins multiple layers.
<br>
<br>
No parallelization is made yet. Some initial problems identified and discussed on 10/04/2024. 
<br>
<br>
Possible improvements:
- [ ] slicing domain and running in batch/multiprocess
- [ ] using Kerrie's Dask idea to improve performance
- [ ] increade file read time

