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

def createDevice(url, headers, data):
  resp = requests.post(url, headers=headers, data=data)
  return resp.json()

def deleteDevice(url):
  resp = requests.delete(url, headers=headers)
  return resp.json()

def bgpSession(url, data):
  resp = requests.post(url, headers=headers, data=data)
  return resp.json()

### main
parser = argparse.ArgumentParser()
parser.add_argument('-e', dest='events', action='store_true', help="Show events", default=False)
parser.add_argument('-l', dest='devices', action='store_true', help="Show devices", default=False)
parser.add_argument('-a', dest='add', action='store_true', help="Add a server", default=False)
parser.add_argument('-d', dest='delete', action='store', help="Delete a server with ID", type=str)
parser.add_argument('-bv4', dest='bv4', action='store', help="Configure IPv4 BGP for server with ID", type=str)
parser.add_argument('-bv6', dest='bv6', action='store', help="Configure IPv6 BGP for server with ID", type=str)
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)

if args.events == True:
  url = ('https://api.packet.net/projects/{}/events'.format(projectId))
  pp.pprint(getJson(url))

elif args.devices == True:
  url = ('https://api.packet.net/projects/{}/devices'.format(projectId))
  pp.pprint(getJson(url))

elif args.add == True:
  print('adding server')
  jsonBody = {
	  "facility": "ewr1",
    "hostname": "test2",
    "operating_system": "ubuntu_14_04",
    "plan": "c1.small.x86",  
  } 
  headers.update({'content-type': "multipart/form-data"})
  print(headers)
  url = ('https://api.packet.net/projects/{}/devices'.format(projectId))
  pp.pprint(createDevice(url,headers,jsonBody))

elif args.delete != None:
  if len(args.delete) > 0:
    print('deleting server ', args.delete)
    url = ('https://api.packet.net/devices/{}'.format(args.delete))
    jsonBody=''
    pp.pprint(deleteDevice(url))

elif args.bv4 != None:
  if len(args.bv4) > 0:
    print('configuring bgp ', args.bv4)  
    headers.update({'content-type': "multipart/form-data"})
    url = ('https://api.packet.net/devices/{}/bgp/sessions'.format(args.bv4))
    print(url)
    jsonBody={"default_route": True, "address_family": "ipv4"}
    pp.pprint(bgpSession(url,jsonBody))

elif args.bv6 != None:
  if len(args.bv6) > 0:
    print('configuring bgp ', args.bv6)  
    headers.update({'content-type': "multipart/form-data"})    
    url = ('https://api.packet.net/devices/{}/bgp/sessions'.format(args.bv6))
    jsonBody={"default_route": True, "address_family": "ipv6"}
    pp.pprint(bgpSession(url,jsonBody))
