import lib_json as libjson 
import os

url = "https://raw.githubusercontent.com/boconnor2017/e2e-patterns/main/json/vcf-5-bringup-template.json"
json_filename = "random_json_file.json"
json_stringvar = libjson.download_json_to_var_from_url(url)
json_pyvar = libjson.load_json_variable(json_stringvar)

# Get keys from JSON
json_keys = libjson.get_keys_from_json(json_pyvar)

# Initialize input_var
input_var = []
json_keys_count = len(json_keys)

# Prompt User for Changes
i=0 
for x in range(json_keys_count):
    prompt_input = input(json_keys[i]+" (original value: "+str(json_pyvar[json_keys[i]])+"): " )
    input_var.append(prompt_input)
    i=i+1

# Edit the python variable
i=0 
for x in json_pyvar:
    json_pyvar[json_keys[i]] = input_var[i]
    i=i+1

# Publish new JSON file
new_json_filename = "new_json_file.json"
new_json_file = libjson.dump_json_to_file(json_pyvar, new_json_filename)