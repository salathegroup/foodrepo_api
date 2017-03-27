"""
Sample Python 2.7 code for a call against the OpenFood API product search
Replace [API_KEY] with your API Key
curl -X POST --header "Content-Type: application/vnd.api+json" --header "Accept: application/json" --header "Authorization: Token token=[API_KEY]" -d "{
  \"query\": {
    \"wildcard\": {
      \"name_translations.en\" : \"toblerone*\"
    }
  }
}" "https://www.openfood.ch/api/v3/products/_search"

USAGE:
$ python product_search.py

MORE INFO:
For more examples of search queries using Elastic Search's DSL, see the curl examples here:
https://github.com/salathegroup/openfood_api/blob/master/sample_code/curl/openfood_api.md
"""

import requests

BASE_URL='https://www.openfood.ch/api/v3'
API_KEY='API_KEY'

url = BASE_URL + '/products/_search'

query =   {
  "query": {
    "wildcard": {
      "name_translations.en" : "toblerone*"
    }
  }
}

headers = {
  'Authorization': "Token token={}".format(API_KEY)
}

r = requests.post(url, json=query, headers=headers)
print r.status_code
print r.json()
