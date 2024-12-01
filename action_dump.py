import yaml
import os
import json
import pickle

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
                create_recursive_thread(**kwargs)
        
        for part_id in parts:
            kwargs["part_id"] = part_id
            thread = threading.Thread(target=create_thread, kwargs=pickle.loads(pickle.dumps(kwargs, -1)))  
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()


def create_recursive_thread(**kwargs):
            part_id = kwargs.get("part_id", None)
            parts = kwargs.get("parts", {})
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