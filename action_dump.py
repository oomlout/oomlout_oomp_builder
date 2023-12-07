import yaml
import os
import json

def main(**kwargs):
    parts = kwargs.get("parts", {})
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




if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)