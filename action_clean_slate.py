import shutil
import os

def main(**kwargs):
    folder_delete_list = ["outputs", "navigation", "parts", "temporary", "data"]
    for folder in folder_delete_list:        
        #check if folder exists
        if os.path.exists(folder):
            #delete folder
            print(f"deleting {folder}")
            try:
                shutil.rmtree(folder)
            except Exception as e:
                #try deleting with system command on windows        
                try:  
                    print(f"error deleting {folder} with shutil.rmtree")
                    os.system(f"rmdir /s /q {folder}")
                    print(f"deleted {folder} with os.system")
                except Exception as e:
                    print(f"error deleting {folder} with os.system")
                    print(e)
                
        else:
            print(f"folder {folder} does not exist")
    

if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)