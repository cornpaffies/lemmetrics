import json
import re
import sys

import requests
from bs4 import BeautifulSoup

community_aggregate_data_regex = re.compile('"community":.*"counts":({.*"subscribers".*?})')

if len(sys.argv) != 2:
    exit("Requires a single link to a Lemmy community")

request_response = requests.get(sys.argv[1])
page = BeautifulSoup(request_response.text, "html.parser")
isodata = page.find(text=community_aggregate_data_regex)
community_aggregate_data_string = re.findall(community_aggregate_data_regex, isodata)[0]
community_aggregate_data_json_object = json.loads(community_aggregate_data_string)

#print(f"{sys.argv[1]}:")
#for i in community_aggregate_data_json_object:
#    print(f"{i}: {community_aggregate_data_json_object[i]}")

print(f"{sys.argv[1]}:")
print(community_aggregate_data_json_object)