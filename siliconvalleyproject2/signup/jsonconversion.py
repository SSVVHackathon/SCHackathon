import json
def conversion(lat, lng, email, company_name, shelter_or_restaurant, address):
    with open('templates/blah.json') as f:
        data = json.load(f)
    new_info = {
        "address":address,
        "lat":lat,
        "lng":lng,
        "shelter_or_restaurant":shelter_or_restaurant,
        "email":email,
        "company_name":company_name
    }
    data['companies'].append(new_info)
    with open('templates/blah.json', 'w') as f:
        json.dump(data, f, indent = 2)