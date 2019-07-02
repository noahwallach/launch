#!/usr/bin/env python3

import requests
import pprint 
import argparse
import json

headers = {'X-Auth-Token': '8AuatCR8Vqj4LC1rpquzkHAU8kqirXfF'}
projectId = 'ca73364c-6023-4935-9137-2132e73c20b4'

def getJson(url):
  resp = requests.get(url, headers=headers)
  return resp.json()

def createDevice(url, data):
  resp = requests.post(url, headers=headers, data=data)
  return resp.json()

def deleteDevice(url, data):
  resp = requests.delete(url, headers=headers)
  return resp.json()


### main
parser = argparse.ArgumentParser()
parser.add_argument('-e', dest='events', action='store_true', help="Show events", default=False)
parser.add_argument('-l', dest='devices', action='store_true', help="Show devices", default=False)
parser.add_argument('-a', dest='add', action='store_true', help="Add a server")
parser.add_argument('-d', dest='delete', action='store', help="Delete a server with ID", type=str)
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)

if args.events == True:
  url = ('https://api.packet.net/projects/{}/events'.format(projectId))
  pp.pprint(getJson(url))

elif args.devices == True:
  url = ('https://api.packet.net/projects/{}/devices'.format(projectId))
  pp.pprint(getJson(url))

elif args.add == 'add':
  jsonBody = {
	  "facility": "any",
    "hostname": "test1",
    "operating_system": "ubuntu_14_04",
    "plan": "baremetal_2a4"  
  } 
  url = ('https://api.packet.net/projects/{}/devices'.format(projectId))
  pp.pprint(createDevice(url,jsonBody))

elif args.delete != None:
  if len(args.delete) > 0:
    url = ('https://api.packet.net/devices/{}'.format(args.delete))
    jsonBody=''
    pp.pprint(deleteDevice(url,jsonBody))
  
  

