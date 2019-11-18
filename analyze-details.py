import json

with open('details-0.json', 'r+') as file:
    data = json.load(file)
    """
    print(len(data['products'][0]))
    for key in data['products'][0]:
        print(key)
    """

    #print(len(data['priceHasError']))
    print(data['totalCount'])

    """
    for key in data['coupons']:
        print(key)
    """

    #print(data['products'][0]['brandName'])