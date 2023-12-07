#imports
import os
import pickle

# settings
#      change these
directory_oomp = "" # directory to create your oomp
directory_links = os.path.join(directory_oomp, "links")
#      don't change these
directory_oomp_parts = os.path.join(directory_oomp, "parts")
file_pickle = os.path.join(directory_oomp, "temporary/parts.pickle")


def main(**kwargs):
    parts = {}
    # load parts from pickle
    with open(file_pickle, 'rb') as handle:
        print(f"loading {file_pickle}")
        parts = pickle.load(handle)

    # make links
    if not os.path.exists(directory_links):
        os.makedirs(directory_links)
        
    # go through every part and make a link
    for part_id in parts:
        part = parts[part_id]
        part_path = os.path.join(directory_oomp_parts, part_id)
        links = ["md5_6_alpha", "short_code", "id"]
        for link in links:
            target_dir = os.path.join(part_path)
            if os.path.exists(target_dir):            
                link_extra = part[link]
                if link_extra != "":                                            
                    link_dir = f"{directory_links}\\{part[link]}"
                    if os.path.exists(link_dir):
                        os.remove(link_dir)
                    target_dir = os.path.abspath(target_dir)
                    print(f"making link {target_dir} to {link_dir}")
                    try:
                        os.symlink(target_dir, link_dir, target_is_directory=True)
                    except e as Exception:
                        print(e)
                        print(f"failed to make link {target_dir} to {link_dir}")
                        pass
                
                #import time
                #delay ten seconds
                #time.sleep(10)



if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)