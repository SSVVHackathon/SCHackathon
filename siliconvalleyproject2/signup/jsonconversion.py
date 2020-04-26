import json
def conversion(address, shelter_or_restaurant, email, company_name):
    with open('signup/blah.json') as f:
        data = json.load(f)
    new_info = {
        'address':address,
        'shelter_or_restaurant':shelter_or_restaurant,
        'email':email,
        'company_name':company_name
    }
    data['companies'].append(new_info)
    with open('signup/blah.json', 'w') as f:
        json.dump(data, f, indent = 2)