# oomlout_oomp_builder
This is part of OOMP the Oopen Organization Method For Parts. For more details: https://github.com/oomlout/oomp_base  



## usage  

### action_create.py  
This utility will pull in the repos in repos_source.yaml and copy their parts folders to whever you want your OOMP to go.  

#### settings
* directory_oomp - the directory you'd like your oomp put. Default is parts/
##### repos_source.yaml
* a list of the repos you'd like to source your oomp from. Default is oomp_base_electronics and oomp_base_hardware

### action_load.py
This utility will load all the yaml files and create a pickle in temporary/

#### settings
* directory_oomp - the directory you'd like your oomp put. Default is parts/

### action_make_links.py
This creates a folder called links/ that has links for full name, shortcode, and md5_6_alpha