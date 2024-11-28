import os
import yaml
import time

# settings
utility_source_yaml = "configuration/utility_source.yaml"
#check if file exists
if not os.path.exists(utility_source_yaml):
    print(f"{utility_source_yaml} doesn't exist using default")
    utility_source_yaml = "configuration/utility_source_default.yaml"

def main(**kwargs):
    utilities = []
    times = kwargs.get("times", [])
    # load utility_source
    with open(utility_source_yaml, 'r') as stream:
        utilities = yaml.load(stream, Loader=yaml.FullLoader)
        
    if utilities != None:
        for utility in utilities:
            time_start = time.time()
            time_name = f"utility: {utility}"
            #clone utility from github into temporary
            print(f"cloning {utility} from github")
            repo_name = utility.split("/")[-1]
            repo_path = f"{repo_name}"
            #repo_path = os.path.join("temporary", repo_path)
            repo_path = os.path.join("c:\\gh", repo_name)
            #if repo already exists pull
            if os.path.exists(repo_path):
                os.system(f"git -C {repo_path} pull")
            else:
                os.system(f"git clone {utility} {repo_path}")
            
            #if not os.path.exists("temporary/__init__.py"):
            if not os.path.exists("c:\\gh\\__init__.py"):
                # Create __init__.py
                #open("temporary/__init__.py", 'a').close()
                open("c:\\gh\\__init__.py", 'a').close()

            #module_name = f"temporary.{repo_name}.working"
            #add c:\\gh to pythonpath
            import sys
            sys.path.append("c:\\gh")
            module_name = f"{repo_name}.working"
            #utility_module = __import__(module_name, fromlist=["temporary"])        
            utility_module = __import__(module_name, fromlist=[""])        
            kwargs["folder"] = "parts"
            utility_module.main(**kwargs)
            time_end = time.time()
            time_entry = {"name": time_name, "time": time_end - time_start}
            times.append(time_entry)
            
            hour = int(time_entry['time']/3600)
            minute = int((time_entry['time'] - hour*3600)/60)
            print(f"{time_name} took {hour} hours and {minute} minutes")
    return times



if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)