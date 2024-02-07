# imports
import os
import yaml
import fnmatch
import shutil

# settings
#      cheange these
directory_oomp = "" # directory to create your oomp
#      don't change these
directory_oomp_parts = os.path.join(directory_oomp, "parts")
directory_temporary = "temporary" # directory to create your oomp

repo_source_yaml = "configuration/repos_source.yaml"
#check if file exists
if not os.path.exists(repo_source_yaml):
    print(f"{repo_source_yaml} doesn't exist using default")
    repo_source_yaml = "configuration/repos_source_default.yaml"


def main(**kwargs):
    
    #if temporary directory doesn't exist create it
    if not os.path.exists(directory_temporary):
        os.makedirs(directory_temporary)
    # if oomp directory doesn't exist create it
    if not os.path.exists(directory_oomp_parts):
        os.makedirs(directory_oomp_parts)


    # load filter
    filter_file = "configuration/filter.yaml"
    if not os.path.exists(filter_file):
        filter_file = "configuration/filter_default.yaml"

    with open(filter_file, 'r') as stream:
        filters = yaml.safe_load(stream)

    # load repo_source
    with open(repo_source_yaml, 'r') as stream:
        repo_source = yaml.safe_load(stream)
    for repo_url in repo_source:
        repo_name = repo_url.split("/")[-1] 

        repo_path = f"{repo_name}"
        repo_path = os.path.join(directory_temporary, repo_path)
        git_clone_pull(repo_url, repo_path)
        # copy part folders to oomp
        folders = ["parts", "data"]
        for folder in folders:
            repo_path_parts = os.path.join(repo_path, folder)
            oomp_path_parts = os.path.join(directory_oomp, folder)
            if os.path.exists(repo_path_parts):
                print(f"copying {repo_path_parts} to {oomp_path_parts}")
                #copy all files and overwrite if it exists use xcopy if windows and cp if linux
                #if no filter use fast copy
                if filter == "*" or folder == "data":
                    if os.name == "nt":
                        os.system(f"xcopy /E /Y /I {repo_path_parts} {oomp_path_parts}")
                    else:
                        oomp_path_parts = oomp_path_parts.replace(folder,".")
                        os.system(f"cp -r {repo_path_parts} {oomp_path_parts}") 
                else:
                    #get folder listing from repo_path_parts

                    source_path = repo_path_parts
                    destination_path = oomp_path_parts
                    for root, dirs, files in os.walk(source_path):
                        for filter_pattern in filters:
                            for folder in fnmatch.filter(dirs, filter_pattern):
                                source_folder = os.path.join(root, folder)
                                destination_folder = os.path.join(destination_path, os.path.relpath(source_folder, source_path))
                                print(f"copying {source_folder} to {destination_folder}")
                                if os.name == "nt":
                                    os.system(f"xcopy /E /Y /I {source_folder} {destination_folder}")
                                else:
                                    os.system(f"cp -r {source_folder} {destination_folder}")
                                

                        


            



          
def git_clone_pull(repo_url, repo_path):
    if os.path.exists(repo_path):
        os.system(f"git -C {repo_path} pull")
    else:
        os.system(f"git clone {repo_url} {repo_path}")

if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)
