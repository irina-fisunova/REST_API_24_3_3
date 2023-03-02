import requests
import json
from config import base_url, statuses, headers, id

pet_put_api = '/pet'
url = base_url + pet_put_api

put_data ={
  "id": id,
  "category": {
    "id": 1,
    "name": "cats"
  },
  "name": "kittens123",
  "photoUrls": [],
  "tags": [
    {
      "id": 1,
      "name": "белая"
    }
  ],
  "status": statuses[0],
}

res = requests.put(url, headers=headers, data=json.dumps(put_data))
print(res.json())
print(res.status_code)
