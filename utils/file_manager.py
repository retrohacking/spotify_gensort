from json import dumps, load
from os.path import isfile

def check_json(file):
    if isfile(file):
        return True
    else:
        return False
    
def create_json(filename, data):
    if not ".json" in filename:
        filename+=".json"
    jsondata=dumps(data, indent=4)
    file=open(filename, "w")
    file.write(jsondata)
    file.close()

def load_json(file):
    f=open(file, "r")
    jsonfile=load(f)
    f.close()
    return jsonfile