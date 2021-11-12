"""
请求接口示例

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import json
from urllib.request import Request, urlopen

request_url = "https://dog.ceo/api/breeds/image/random"
request = Request(request_url, method="GET")

with urlopen(request) as response:
    string_data = response.read().decode()
    json_data = json.loads(string_data)
    print(json_data["message"])
