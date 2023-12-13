
import os
import yaml
import json

utilities = []
utilities.append("https://github.com/oomlout/oomlout_oomp_utility_readme_generation")


def main(**kwargs):
    parts = {}
    
    #      create
    import action_create
    action_create.main(**kwargs)
    
    #      load in the yaml files
    import action_load
    parts = action_load.main(**kwargs)    
    kwargs["parts"] = parts
    
    #      make links
    import action_make_links
    #action_make_links.main(**kwargs)

    #      run utilities
    import action_run_utilities
    action_run_utilities.main(**kwargs)

    #      dump parts to yaml
    import action_dump
    action_dump.main(**kwargs)

    #       create archive
    import action_create_archive
    action_create_archive.main(**kwargs)    
    

    
    




if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)