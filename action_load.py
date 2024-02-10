# imports
import yaml
import os
import glob
import pickle
import time

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
    
    for file_yaml_part in file_yaml_parts:
        with open(file_yaml_part, 'r') as stream:
            part_yaml = yaml.load(stream, Loader=yaml.FullLoader)        
                   
        id = part_yaml.get("id", part_yaml.get("oomp_id", None))
        if id is None:
            Exception(f"part_yaml has no id: {part_yaml}")
        print(f"loading {id}")
        if id not in parts:
            parts[id] = {}
        parts[id].update(part_yaml)
            

    #add data files
    for file_name_yaml in file_names_yaml:
        file_yaml_data = glob.glob(f"{directory_oomp_data}/*/{file_name_yaml}")

    for file_yaml in file_yaml_data:
        with open(file_yaml, 'r') as stream:
            data_yaml = yaml.load(stream, Loader=yaml.FullLoader)
        
        for part_id in data_yaml:
            part = data_yaml[part_id]
            id = part.get("id", part.get("oomp_id", None))
            if id is None:
                Exception(f"part_yaml has no id: {data_yaml}")
            print(f"updating {id}")
            if id not in parts:
                #Exception(f"part_yaml has no id: {part_yaml}")
                print(f"part_yaml has no id: {id}")
                time.sleep(2)
            else:
                parts[id].update(part)

    # save parts to pickle
    if not os.path.exists(os.path.dirname(file_oomp_parts_pickle)):
        os.makedirs(os.path.dirname(file_oomp_parts_pickle))

    with open(file_oomp_parts_pickle, 'wb') as handle:
        print(f"saving {file_oomp_parts_pickle}")
        pickle.dump(parts, handle)

    if not os.path.exists(os.path.dirname(file_oomp_parts_yaml)):
        os.makedirs(os.path.dirname(file_oomp_parts_yaml))
    # save parts to yaml
    with open(file_oomp_parts_yaml, 'w') as stream:
        print(f"saving {file_oomp_parts_yaml}")
        yaml.dump(parts, stream)

    #save all parts back to their directory to make the data injections permanent
    for part_id in parts:
        part = parts[part_id]
        file_oomp_part = os.path.join(directory_oomp_parts, part_id, "working.yaml")
        if not os.path.exists(os.path.dirname(file_oomp_part)):
            os.makedirs(os.path.dirname(file_oomp_part))
        with open(file_oomp_part, 'w') as stream:
            print(f"saving {file_oomp_part}")
            yaml.dump(part, stream)

    return parts


if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)