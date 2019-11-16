import json

with open('details-0.json', 'r+') as file:
    data = json.load(file)
    print(data['products'][0]['brandName'])