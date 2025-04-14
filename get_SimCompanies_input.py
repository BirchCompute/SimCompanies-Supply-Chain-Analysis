import json


def getResourceData():
    '''Open the Resource data file and return the JSON dict inside it'''
    #Another module gets the Resource data and turns it into a JSON file

    with open("SimCoResourceData.json", mode = "r") as file:
        _data = json.load(file)

    return _data



def getInputData():
    '''Take the Resource data from SimCo Tools and make a new dictionary that just has ID and Input IDs'''

    _resourceData = getResourceData()
    _inputsData = {}

    for k,v in _resourceData.items():
        try:
            _inputsData[k]=list(v["resource"]["inputs"])
        except:
            #print("fail")
            pass
        
    return _inputsData



if __name__ == "__main__":

    inputsData = getInputData()

    with open("SimCoInputsData.json", mode= "w") as file:
        json.dump(inputsData, file, indent=4)

    #Test print
    #for y,z in newData.items():
    #    print(y, z)