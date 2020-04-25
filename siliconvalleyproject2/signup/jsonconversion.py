import json
def conversion():
    with open('blah.json') as f:
        data = json.load(f)
    for company in data['companies']:
        del company['type']
    with open('blah.json', 'w') as f:
        json.dump(data, f, indent = 2)