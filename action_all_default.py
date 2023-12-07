import action_load
import action_create
import action_make_links
import os

utilities = []
utilities.append("https://github.com/oomlout/oomlout_oomp_utility_readme_generation")


def main(**kwargs):
    action_create.main(**kwargs)
    action_load.main(**kwargs)    
    action_make_links.main(**kwargs)

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

    
    #create zip file
    print("creating zip file")
    file_output = "outputs/oomp_mine"
    directory_source = "parts"
    import shutil
    shutil.make_archive(file_output, 'zip', directory_source)
    




if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)