# imports
import os
import yaml
# settings
#      cheange these
directory_oomp = "" # directory to create your oomp
#      don't change these
directory_oomp_parts = os.path.join(directory_oomp, "parts")
directory_temporary = "temporary" # directory to create your oomp
repo_source_yaml = "repos_source.yaml"


def main(**kwargs):
    
    #if temporary directory doesn't exist create it
    if not os.path.exists(directory_temporary):
        os.makedirs(directory_temporary)
    # if oomp directory doesn't exist create it
    if not os.path.exists(directory_oomp_parts):
        os.makedirs(directory_oomp_parts)

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
                if os.name == "nt":
                    os.system(f"xcopy /E /Y {repo_path_parts} {oomp_path_parts}")
                else:
                    oomp_path_parts = oomp_path_parts.replace("parts",".")
                    os.system(f"cp -r {repo_path_parts} {oomp_path_parts}") 


            



          
def git_clone_pull(repo_url, repo_path):
    if os.path.exists(repo_path):
        os.system(f"git -C {repo_path} pull")
    else:
        os.system(f"git clone {repo_url} {repo_path}")

if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)
