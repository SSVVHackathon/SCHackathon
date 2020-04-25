import json
def conversion():
    with open('signup/blah.json') as f:
        data = json.load(f)
    for company in data['companies']:
        del company['type']
    with open('signup/blah.json', 'w') as f:
        json.dump(data, f, indent = 2)