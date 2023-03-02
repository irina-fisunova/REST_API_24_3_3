import requests
import json
from config import base_url, statuses, headers


pet_post_api = '/pet'
url = base_url + pet_post_api

post_data = {
    'id': 1,
    'category': {
        'id': 1,
        'name': 'cats'
    },
    'name': 'kitten',
    'photoUrls': [],
    'tags': [
        {
            'id': 1,
            'name': 'черная',
        },
        {
            'id': 2,
            'name': 'пушистая',
        }
    ],
    'status': statuses[0],
}

res = requests.post(url, headers=headers, data=json.dumps(post_data))
print(res.json())