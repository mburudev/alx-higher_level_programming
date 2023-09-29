#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content.decode('utf-8'))
        print("\t- utf8 content: {}".format(content))
except Exception as e:
    print(e)
