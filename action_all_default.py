
import os
import yaml
import json

utilities = []
utilities.append("https://github.com/oomlout/oomlout_oomp_utility_readme_generation")


def main(**kwargs):
    import time

    times = []


    parts = {}
    
    #      create
    import action_create
    time_start = time.time()
    time_name = "action_create.main()"
    action_create.main(**kwargs)
    time_end = time.time()
    time_entry = {"name": time_name, "time": time_end - time_start}
    times.append(time_entry)
    
    #      load in the yaml files
    import action_load
    time_start = time.time()
    time_name = "action_load.main()"
    parts = action_load.main(**kwargs)        
    kwargs["parts"] = parts
    time_end = time.time()
    time_entry = {"name": time_name, "time": time_end - time_start}
    times.append(time_entry)
    
    #      make links
    import action_make_links
    #action_make_links.main(**kwargs)

    #      run utilities
    import action_run_utilities
    kwargs["times"] = times
    times = action_run_utilities.main(**kwargs)


    #      reload parts from their new yaml files
    #      this makes the changes permanent
    import action_load
    time_start = time.time()
    time_name = "action_load.main() second time"
    parts = action_load.main(**kwargs)    
    kwargs["parts"] = parts
    time_end = time.time()
    time_entry = {"name": time_name, "time": time_end - time_start}
    times.append(time_entry)

    #      dump parts to yaml
    import action_dump
    time_start = time.time()
    time_name = "action_dump.main()"    
    action_dump.main(**kwargs)
    time_end = time.time()
    time_entry = {"name": time_name, "time": time_end - time_start}
    times.append(time_entry)

    #       create archive
    import action_create_archive
    #action_create_archive.main(**kwargs)    
    
    #print the times in a nice hour:min format
    print("Times:")
    for time_entry in times:
        print(f"{time_entry['name']} took {time_entry['time']/60:.2f} minutes")
    
    




if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)