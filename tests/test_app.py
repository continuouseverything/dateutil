import pytest
from flask import g
from flask import session

import requests
import json

def test_status():
    url = 'http://0.0.0.0:80/'
    resp = requests.get(url)

    assert resp.status_code == 200

def test_date():
    url = 'http://0.0.0.0/normalize/10.10.2019'
    resp = requests.get(url)

    resp_body = resp.json()
    print(resp.text)
    assert resp_body['day'] == '2019-10-10'