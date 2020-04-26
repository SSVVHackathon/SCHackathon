import json

def data():
    with open('signup/blah.json') as f:
        info = json.load(f)
    return info