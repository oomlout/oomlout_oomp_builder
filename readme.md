# oomlout_oomp_builder
This is part of OOMP the Oopen Organization Method For Parts. For more details: https://github.com/oomlout/oomp_base

This utility will pull in the repos in repos_source.yaml and copy their parts folders to whever you want your OOMP to go.

## usage
python working.py

## settings
### working.py
* directory_oomp - the directory you'd like your oomp put. Default is parts/
### repos_source.yaml
* a list of the repos you'd like to source your oomp from. Default is oomp_base_electronics and oomp_base_hardware