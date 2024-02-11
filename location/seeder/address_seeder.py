#!/usr/bin/env python3

import requests
import json

url = "http://host.docker.internal:8000/address"

with open('location.json', 'r') as file:
    rows = json.load(file)
    for row in rows:
        response = requests.post(url, data = json.dumps(row))
        if response.status_code != 200:
            print(f"An error occured for payload {row} and returned status {response.status_code}")