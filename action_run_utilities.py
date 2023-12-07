import os
import yaml

# settings
utility_source_yaml = "configuration/utility_source.yaml"

def main(**kwargs):
    utilities = []
    # load utility_source
    with open(utility_source_yaml, 'r') as stream:
        utilities = yaml.load(stream, Loader=yaml.FullLoader)
        
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



if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)