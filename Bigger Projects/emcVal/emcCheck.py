import json

with open('custom_emc.json') as f:
    data = json.load(f)
name = ''
max = 0

for i in range(len(data['entries'])):
    # print(data['entries'][1]['emc'])
    if data['entries'][i]['emc'] > max:
        max = data['entries'][i]['emc']
        name = data['entries'][i]['item']
print(max)
print(name)
