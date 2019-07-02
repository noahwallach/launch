#!/usr/bin/env python3

import requests
import pprint 
import argparse
import json

headers = {'X-Auth-Token': '8AuatCR8Vqj4LC1rpquzkHAU8kqirXfF'}

def getJson(url):
  resp = requests.get(url, headers=headers)
  return resp.json()

def createDevice(url, data):
  resp = requests.post(url, headers=headers, data=json.dumps(data))
  return resp.json()

### main
parser = argparse.ArgumentParser()
parser.add_argument('-e', dest='action', help="Show events")
parser.add_argument('-l', dest='action', help="Show devices")
parser.add_argument('-a', dest='action', help="Add a server")
parser.add_argument('-d', dest='action', help="Delete a server with ID", type=str)
args = parser.parse_args()

choice = args.action
pp = pprint.PrettyPrinter(indent=4)

# https://github.com/timeline.json
if choice == 'events':
  pp.pprint(getJson('https://api.packet.net/projects/ca73364c-6023-4935-9137-2132e73c20b4/events'))

elif choice == 'devices':
  pp.pprint(getJson('https://api.packet.net/projects/ca73364c-6023-4935-9137-2132e73c20b4/devices'))

elif choice == 'add':
  jsonBody = {
	  "facility": "any",
    "hostname": "test1.packet.com",
    "plan": "any"  } 
  pp.pprint(createDevice('https://api.packet.net/projects/ca73364c-6023-4935-9137-2132e73c20b4/devices',jsonBody))

elif choice == 'delete':
  pass
print(choice)

