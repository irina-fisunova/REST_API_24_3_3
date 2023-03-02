import requests
import json
from config import base_url, statuses, headers

pet_put_api = '/pet'
url = base_url + pet_put_api

put_data =	{
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": statuses[0],
}

res = requests.put(url, headers=headers, data=json.dumps(put_data))
print(res.json())
