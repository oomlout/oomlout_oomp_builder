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

cnt = 1
cnt_error = 0
def main(**kwargs):
    global cnt, cnt_error
    parts = {}

    file_names_yaml = ["working.yaml"]
    # go through every directory in parts and load the yaml files
    
    file_yaml_parts = []
    for file_name_yaml in file_names_yaml:
        file_yaml_parts += glob.glob(f"{directory_oomp_parts}/*/{file_name_yaml}")
    
    
    for file_yaml_part in file_yaml_parts:
        import threading
        threading.Thread(target=load_part_thread, args=(file_yaml_part, parts)).start()

    if cnt_error > 0:
        print(f"error in {cnt_error} files")
        import time
        #time.sleep(30)
        cnt_error = 0
        
            

    #add data files
    print(f"loading parts from {directory_oomp_data}")
    for file_name_yaml in file_names_yaml:
        file_yaml_data = glob.glob(f"{directory_oomp_data}/*/{file_name_yaml}")



    for file_yaml in file_yaml_data:
        with open(file_yaml, 'r') as stream:
            data_yaml = yaml.load(stream, Loader=yaml.FullLoader)
        
        for part_id in data_yaml:
            if part_id in parts:
                part = data_yaml[part_id]
                id = part.get("id", part.get("oomp_id", None))
                if id is None:
                    Exception(f"part_yaml has no id: {data_yaml}")
                print(f"updating {id}")
                if id not in parts:
                    #Exception(f"part_yaml has no id: {part_yaml}")
                    print(f"part_yaml has no id: {id}")
                    #time.sleep(2)
                else:
                    parts[id].update(part)
                    print(f"." , end="", flush=True)
            else:
                print(f"part_id {part_id} not in parts")

    # save parts to pickle
    if not os.path.exists(os.path.dirname(file_oomp_parts_pickle)):
        os.makedirs(os.path.dirname(file_oomp_parts_pickle))

    with open(file_oomp_parts_pickle, 'wb') as handle:
        print(f"saving {file_oomp_parts_pickle}")
        pickle.dump(parts, handle)

    if not os.path.exists(os.path.dirname(file_oomp_parts_yaml)):
        os.makedirs(os.path.dirname(file_oomp_parts_yaml))
    
    import io
    
    # save parts to yaml    
    buffer = io.StringIO()
    print(f"saving {file_oomp_parts_yaml}")
    yaml.dump(parts, buffer)
    with open(file_oomp_parts_yaml, 'w') as stream:
        stream.write(buffer.getvalue())

    #save all parts back to their directory to make the data injections permanent
    import threading
    semaphore = threading.Semaphore(1000)
    threads = []

    def create_thread(part, part_id, directory_oomp_parts):
        with semaphore:
            save_part_threading(part, part_id, directory_oomp_parts)
            
    for part_id in parts:
        part = parts[part_id]
        
        thread = threading.Thread(target=create_thread, args=(part, part_id, directory_oomp_parts))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

  
    return parts

def save_part_threading(part, part_id, directory_oomp_parts):
    global cnt
    file_oomp_part = os.path.join(directory_oomp_parts, part_id, "working.yaml")
    if not os.path.exists(os.path.dirname(file_oomp_part)):
        os.makedirs(os.path.dirname(file_oomp_part))
    with open(file_oomp_part, 'w') as stream:
        #print(f"saving {file_oomp_part}")
        cnt += 1
        yaml.dump(part, stream)
    if cnt % 100 == 0:
        print(f".", end="")

def load_part_thread(file_yaml_part, parts):
    global cnt, cnt_error
    with open(file_yaml_part, 'r') as stream:
        part_yaml = yaml.load(stream, Loader=yaml.FullLoader)        

        try:
            id = part_yaml.get("id", part_yaml.get("oomp_id", None))
            if id is None:
                #Exception(f"part_yaml has no id: {part_yaml}")
                print(f"part_yaml has no id: {part_yaml}")
                cnt_error += 1
            #print(f"loading {id}")
                
            if id not in parts:
                parts[id] = {}
            parts[id].update(part_yaml)

            cnt += 1
            if cnt % 100 == 0:
                print(f".", end="")
        except Exception as e:
            print(f"error in {file_yaml_part}")
            cnt_error += 1


if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)