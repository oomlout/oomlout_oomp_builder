import action_load
import action_create
import action_make_links
import os
import yaml
import json

utilities = []
utilities.append("https://github.com/oomlout/oomlout_oomp_utility_readme_generation")


def main(**kwargs):
    parts = {}
    action_create.main(**kwargs)
    parts = action_load.main(**kwargs)    
    #action_make_links.main(**kwargs)

    for utility in utilities:
        #clone utility from github into temporary
        print(f"cloning {utility} from github")
        repo_name = utility.split("/")[-1]
        repo_path = f"{repo_name}"
        repo_path = os.path.join("temporary", repo_path)
        #if repo already exists pull
        if os.path.exists(repo_path):
            os.system(f"git -C {repo_path} pull")
        else:
            os.system(f"git clone {utility} {repo_path}")
        
        module_name = f"temporary.{repo_name}.working"
        utility_module = __import__(module_name, fromlist=["temporary"])        
        kwargs["folder"] = "parts"
        utility_module.main(**kwargs)

    #dump parts to yaml
    for part_id in parts:
        part = parts[part_id]
        directory = f"parts/{part_id}"
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_yaml = f"{directory}/working.yaml"
        with open(file_yaml, 'w') as stream:
            print(f"saving yaml {file_yaml}")
            yaml.dump(part, stream)
        file_json = f"{directory}/working.json"
        with open(file_json, 'w') as stream:
            print(f"saving json {file_json}")
            json.dump(part, stream)
        
    

    #create zip file
    print("creating zip file")
    file_output = "outputs/oomp_mine"
    directory_source = "parts"
    import shutil
    shutil.make_archive(file_output, 'zip', directory_source)
    




if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)