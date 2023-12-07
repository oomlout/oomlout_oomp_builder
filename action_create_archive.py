import shutil

def main(**kwargs):
    #create zip file
    print("creating zip file")
    file_output = "outputs/oomp_mine"
    directory_source = "parts"
    import shutil
    shutil.make_archive(file_output, 'zip', directory_source)

if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)