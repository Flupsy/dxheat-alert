#!/usr/bin/python
#
# Get the heatmap raw data from DXHeat and print output if bands are active.
# Designed to be used as a cron job such that an email will be generated
# if there is any output.
#
# Ian Chard  26/05/2023
#

import sys
import requests
import json

# Replace 'EU' with one of the following if you're not in Europe:
#   'NA' = North America
#   'SA' = South America
#   'AS' = Asia
#   'AF' = Africa
#   'OC' = Oceania
URL = 'https://dxheat.com/heatmap/source/heatmap/?c=EU'

# Just comment out any bands you're not interested in.
band_map = {
        #'55': '6m',
        '85': '10m',
        '115': '12m',
        '145': '15m',
        '175': '17m',
        '205': '20m',
        '235': '30m',
        '265': '40m',
        #'295': '80m',
        #'325': '160m',
        }


if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <band alert threshold, e.g. 100>')
    exit(0)

try:
    threshold = int(sys.argv[1])
except ValueError:
    print(f'{sys.argv[0]}: argument must be a number')
    exit(1)

response = requests.get(URL)
response.raise_for_status()

heatmap = json.loads(response.text)
band_activity = {}

for i in heatmap:
    try:
        band_activity[band_map[i['y']]] = band_activity.get(band_map[i['y']], 0) + i['value']
    except KeyError:
        continue

for i in band_activity:
    if band_activity[i] >= threshold:
        print(f'{i}: {band_activity[i]}')
