import json

with open('e:/Code/Python-Automation-60Days/day03/data.json') as f:
    my_data = json.load(f)

print(my_data)

del my_data['age']
with open('e:/Code/Python-Automation-60Days/day03/new_data.json', 'w') as f:
    json.dump(my_data, f, indent=2)