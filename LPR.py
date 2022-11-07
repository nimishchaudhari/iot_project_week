# # pip install requests
# import requests
# from pprint import pprint
# img_path = ""
# regions = ['mx', 'us-ca'] # Change to your country
# with open(img_path, 'rb') as fp:
#     response = requests.post(
#         'https://api.platerecognizer.com/v1/plate-reader/',
#         data=dict(regions=regions),  # Optional
#         files=dict(upload=fp),
#         headers={'Authorization': 'Token my-token******'})
# pprint(response.json())

# Calling with a custom engine configuration
import json,requests
from pprint import pprint
img_path = "frankrijk262.jpg"
with open(img_path, 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=['it'], config=json.dumps(dict(region="strict"))),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token b8a93ecfa67a1110708f72ccb66d423ecca836a8'})


