import yaml
import os

cnt_dump = 1

def main(**kwargs):
    parts = kwargs.get("parts", {})
    #dump parts to yaml

    mode = "semaphore"
    if mode == "semaphore":
        import threading
        semaphore = threading.Semaphore(1000)
        threads = []

        def create_thread(**kwargs):
            with semaphore:
                kwargs.pop("part_id", "")
                create_recursive_thread(part_id, **kwargs)
        
        for part_id in parts:
            #kwargs["part_id"] = part_id            
            thread = threading.Thread(target=create_thread, kwargs={"part_id": part_id, **kwargs})  
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()


def create_recursive_thread(part_id, **kwargs):
            #part_id = kwargs.get("part_id", None)
            parts = kwargs.get("parts", {})
            part = parts[part_id]
            directory = f"parts/{part_id}"
            if not os.path.exists(directory):
                os.makedirs(directory)
            file_yaml = f"{directory}/working.yaml"
            with open(file_yaml, 'w') as stream:
                #print(f"saving yaml {file_yaml}")
                yaml.dump(part, stream)
            file_json = f"{directory}/working.json"
            with open(file_json, 'w') as stream:
                #print(f"saving json {file_json}")
                #json.dump(part, stream)
                 pass
            global cnt_dump
            cnt_dump += 1
            if cnt_dump % 100 == 0:
                print(f".", end="")




if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)