#!/usr/bin/env python3

#./call.py -f data.txt -u http://192.168.1.145:8080 -e dpm

from argparse import ArgumentParser
from time import sleep
import requests
import sys
import json

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="file",
                    help="Line separated file of qrcode value", metavar="FILE")
parser.add_argument("-u", "--url", dest="url",
                    help="Base url of the rpi instance", metavar="URL")
parser.add_argument("-e", "--event", dest="event",
                    help="Event short name", metavar="EVENT")

args = parser.parse_args()

if args.file == None:
  print('file is required')
  sys.exit()
  
if args.url == None:
  print('url is required')
  sys.exit()
  
if args.event == None:
  print('event is required')
  sys.exit()

print(f'file is: {args.file}\nurl is: {args.url}\nevent is: {args.event}')

event = args.event
file = args.file
base_url = args.url

url_to_call_base = base_url + '/admin/api/check-in/event/' + event + '/ticket/'


def call_check_in(ticket_data):
  ticket_id = ticket_data.split('/')[0]
  url_to_call = url_to_call_base + ticket_id
  res = requests.post(url_to_call, json = {"code": ticket_data})
  print(res.text)


with open(file, "r") as ins:
  for line in ins:
    call_check_in(line.strip())
    sleep(1) #sleep 1s



