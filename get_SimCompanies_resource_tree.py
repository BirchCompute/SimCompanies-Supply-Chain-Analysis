import json

def recursiveInputsTree(ID, _data, count = 1):
    if(_data[ID]):
        for i in _data[ID]:
            print("-"*count, i)
            recursiveInputsTree(i, _data, count = count+1)


if __name__=="__main__":

    with open("SimCoInputsData.json") as file:
        data = json.load(file)
    print("144")
    recursiveInputsTree('144', data)