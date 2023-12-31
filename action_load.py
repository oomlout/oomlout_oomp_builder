# imports
import yaml
import os
import glob
import pickle

#  settings
directory_oomp = "" # directory of your oomp
directory_oomp_parts = os.path.join(directory_oomp, "parts")
directory_oomp_data = os.path.join(directory_oomp, "data")
file_oomp_parts_pickle = os.path.join(directory_oomp, "temporary/parts.pickle")
file_oomp_parts_yaml = os.path.join(directory_oomp, "temporary/parts.yaml")

def main(**kwargs):
    parts = {}

    file_names_yaml = ["working.yaml"]
    # go through every directory in parts and load the yaml files
    
    file_yaml_parts = []
    for file_name_yaml in file_names_yaml:
        file_yaml_parts += glob.glob(f"{directory_oomp_parts}/*/{file_name_yaml}")
    #add data files
    for file_name_yaml in file_names_yaml:
        file_yaml_parts += glob.glob(f"{directory_oomp_data}/*/{file_name_yaml}")

    glob.glob(f"{directory_oomp_parts}/*/*.yaml")
    for file_yaml_part in file_yaml_parts:
        with open(file_yaml_part, 'r') as stream:
            parts_yaml = yaml.load(stream, Loader=yaml.FullLoader)
        
        if not isinstance(parts_yaml, list):
            parts_yaml = [parts_yaml]
        
        for part_yaml in parts_yaml:            
            id = part_yaml["id"]
            print(f"loading {id}")
            if id not in parts:
                parts[id] = {}
            parts[id].update(part_yaml)
            

    if not os.path.exists(os.path.dirname(file_oomp_parts_pickle)):
        os.makedirs(os.path.dirname(file_oomp_parts_pickle))

    # save parts to pickle
    with open(file_oomp_parts_pickle, 'wb') as handle:
        print(f"saving {file_oomp_parts_pickle}")
        pickle.dump(parts, handle)

    if not os.path.exists(os.path.dirname(file_oomp_parts_yaml)):
        os.makedirs(os.path.dirname(file_oomp_parts_yaml))
    # save parts to yaml
    #with open(file_oomp_parts_yaml, 'w') as stream:
    #    print(f"saving {file_oomp_parts_yaml}")
    #    yaml.dump(parts, stream)

    return parts


if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)