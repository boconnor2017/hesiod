import os

with open("json/lab_environment.json") as file:
    json_stringvar = file.read()
    print(json_stringvar)