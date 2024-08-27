import lib_json as libjson 
import os
import urllib

url = "https://raw.githubusercontent.com/boconnor2017/e2e-patterns/main/json/vcf-5-bringup-template.json"
json_filename = "sample_json.json"
#json_file = libjson.download_json_file_from_url(url, json_filename)
#json_stringvar = libjson.populate_var_from_json_file(os.getcwd(), json_filename)
json_web = urllib.request.urlopen(url)
json_binvar = json_web.read()
json_stringvar = json_binvar.decode("utf-8")
print(json_stringvar)
#json_pyvar = libjson.load_json_variable(json_stringvar)
#print("DNS Servers: "+json_pyvar["dnsSpec"]["nameserver"]+", "+json_pyvar["dnsSpec"]["secondaryNameserver"])