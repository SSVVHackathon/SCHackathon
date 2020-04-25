import json
def conversion(address, email, company_name):
    with open('signup/blah.json') as f:
        data = json.load(f)
    new_info = {
        "address":address,
        "email":email,
        "company_name":company_name
    }
    data['companies'].append(new_info)
    with open('signup/blah.json', 'w') as f:
        json.dump(data, f, indent = 2)