import json
with open('jumiaData.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    print (i['date'])