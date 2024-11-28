
import os
import yaml
import json

utilities = []
utilities.append("https://github.com/oomlout/oomlout_oomp_utility_readme_generation")


def main(**kwargs):
    import time

    times = []


    parts = {}
    
    time_start_start = time.time()

    #      create
    import action_create
    time_start = time.time()
    time_name = "action_create.main()"
    print("starting action_create.main()")
    action_create.main(**kwargs)
    time_end = time.time()
    time_entry = {"name": time_name, "time": time_end - time_start}
    times.append(time_entry)    
    hour = int(time_entry['time']/3600)
    minute = int((time_entry['time'] - hour*3600)/60)
    seconds = int(time_entry['time'] - hour*3600 - minute*60)
    print()
    print()
    print()
    print()
    print(f"{time_name} took {hour} hours and {minute} minutes and {seconds} seconds")
    print()
    print()
    
    
    #      load in the yaml files
    import action_load
    time_start = time.time()
    time_name = "action_load.main()"
    print("starting action_load.main()")
    parts = action_load.main(**kwargs)        
    kwargs["parts"] = parts
    time_end = time.time()
    time_entry = {"name": time_name, "time": time_end - time_start}
    times.append(time_entry)
    
    hour = int(time_entry['time']/3600)
    minute = int((time_entry['time'] - hour*3600)/60)
    seconds = int(time_entry['time'] - hour*3600 - minute*60)
    print()
    print()
    print()
    print()
    print(f"{time_name} took {hour} hours and {minute} minutes and {seconds} seconds")
    print()
    print()

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
    print("starting action_load.main() second time")
    parts = action_load.main(**kwargs)    
    kwargs["parts"] = parts
    time_end = time.time()
    time_entry = {"name": time_name, "time": time_end - time_start}
    times.append(time_entry)
    
    hour = int(time_entry['time']/3600)
    minute = int((time_entry['time'] - hour*3600)/60)
    seconds = int(time_entry['time'] - hour*3600 - minute*60)
    print()
    print()
    print()
    print()
    print(f"{time_name} took {hour} hours and {minute} minutes and {seconds} seconds")
    print()
    print()

    #      dump parts to yaml
    import action_dump
    time_start = time.time()
    time_name = "action_dump.main()"    
    print("starting action_dump.main()")
    action_dump.main(**kwargs)
    time_end = time.time()
    time_entry = {"name": time_name, "time": time_end - time_start}
    times.append(time_entry)
    
    hour = int(time_entry['time']/3600)
    minute = int((time_entry['time'] - hour*3600)/60)
    seconds = int(time_entry['time'] - hour*3600 - minute*60)
    print()
    print()
    print()
    print()
    print(f"{time_name} took {hour} hours and {minute} minutes and {seconds} seconds")
    print()
    print()

    #       create archive
    import action_create_archive
    #action_create_archive.main(**kwargs)    
    

    time_end_end = time.time()
    time_entry = {"name": "total time", "time": time_end_end - time_start_start}
    times.append(time_entry)

    #print the times in a nice hour:min format
    print()
    print()
    print()
    print()
    print("Times:")
    for time_entry in times:
        hour = int(time_entry['time']/3600)
        minute = int((time_entry['time'] - hour*3600)/60)
        seconds = int(time_entry['time'] - hour*3600 - minute*60)

        print(f"{time_entry['name']} took {hour} hours and {minute} minutes and {seconds} seconds")
        

    
    




if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)