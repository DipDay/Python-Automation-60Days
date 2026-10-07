import json

my_data = '''
    {
        "name": "Dip",
        "age": 20,
        "address": {
            "road no.": "999/99",
            "village": "Elongi",
            "city": "Kushtia"        
        },
        "skills": ["Python", "C", "graphic design"],
        "student": true,
        "girlfriend": null
    }
'''
data = json.loads(my_data)

# print(data)
# print(type(data))
# print(len(data['address']))

# for i in data['skills']:
#     print(i)

del data['age']
# new_data = json.dumps(data)
new_data = json.dumps(data, indent=2)               #use indent to create readable space in new_data
print(new_data)
