import json

# loads and dumps deal with raw data
# load and dump deals with files


with open('details.json') as json_file:
	data = json.load(json_file)

json_details = json.dumps(data,sort_keys=True, indent=2) #converts to json
print(json_details)

dict_details = json.loads(json_details) #converts back to a python dict

# Accessing details
for person in data['details']:
	print(f"{person['name']} - {person['email']}")