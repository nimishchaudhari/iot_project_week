# License plate detection
import json,requests
from pprint import pprint
# path = "mqtt_onServer/received_image.jpg"
regions = ['fr'] # Change to your country


def get_license_number(path="mqtt_onRPI/photo.jpg"):    
    with open(path, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            # data=dict(regions=['fin'], config=json.dumps(dict(region="strict"))),  # Optional
            files=dict(upload=fp),
            headers={'Authorization': 'Token b8a93ecfa67a1110708f72ccb66d423ecca836a8'})

        # pprint(response.json(['filename']))
        # pprint(response.json(['results','plate']))
        json_data = json.loads(response.text)
        return str(json_data['results'][0]['plate'])
