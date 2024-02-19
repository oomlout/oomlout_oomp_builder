import shutil
import os

def main(**kwargs):
    filter = kwargs.get("filter", "")
    if filter == "":
        return
    else:
        folder = f"parts"
        if os.path.exists(folder):
            #remove all folders in parts that have filter in their name
            for part in os.listdir(folder):
                if filter in part:
                    print(f"removing {part}")
                    shutil.rmtree(os.path.join(folder, part))

if __name__ == "__main__":
    kwargs = {}
    filter = "hardware"
    kwargs["filter"] = filter
    main(**kwargs)