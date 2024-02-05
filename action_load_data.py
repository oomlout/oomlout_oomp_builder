import os
import glob
import yaml

def main(**kwargs):
    folder_data = "data"
    folder_parts = "parts"
    #get all files called working.yaml in the data directoy ecursive
    files = glob.glob(f"{folder_data}/**/working.yaml", recursive=True)
    for file in files:
        print(f"loading {file}")
        with open(file, 'r') as stream:
            data = yaml.load(stream, Loader=yaml.FullLoader)
            #print(data)

    for d in data:
        id_oomp = d.get("id_oomp", d.get("id", None))
        if id_oomp == None:
            print(f"no id_oomp in {file}")
        else:
            yaml_file_input = f"{folder_parts}/{id_oomp}/working.yaml"
            d.pop("id_oomp", None)
            d.pop("id", None)
            #load yaml file
            with open(yaml_file_input, 'r') as stream:
                data = yaml.load(stream, Loader=yaml.FullLoader)
            data.update(d)
            #dump yaml file
            with open(yaml_file_input, 'w') as stream:
                yaml.dump(data, stream, default_flow_style=False)
                pass




if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)