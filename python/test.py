import lib_json as libjson 
import os
import urllib

url = "https://raw.githubusercontent.com/boconnor2017/e2e-patterns/main/json/vcf-5-bringup-template.json"
json_stringvar = libjson.download_json_to_var_from_url(url)
json_pyvar = libjson.load_json_variable(json_stringvar)
print("DNS Servers: "+json_pyvar["dnsSpec"]["nameserver"]+", "+json_pyvar["dnsSpec"]["secondaryNameserver"])