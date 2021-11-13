# Write your awesome code here
import json
from typing import List
import re

data = json.loads(input())

error_ids = dict()
keys: List[str] = ['bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time']
bus_info = dict()

for bus in data:
    if not bus[keys[0]] or not isinstance(bus[keys[0]], int):
        error_ids[keys[0]] = error_ids.get(keys[0], 0) + 1
    if not bus[keys[1]] or not isinstance(bus[keys[1]], int):
        error_ids[keys[1]] = error_ids.get(keys[1], 0) + 1
    if not bus[keys[2]] or not isinstance(bus[keys[2]], str):
        error_ids[keys[2]] = error_ids.get(keys[2], 0) + 1
    elif not re.match(r"([A-Z]\w+ )+(Road|Avenue|Boulevard|Street)$", bus[keys[2]]):
        error_ids[keys[2]] = error_ids.get(keys[2], 0) + 1

    if bus[keys[3]] is None or not isinstance(bus[keys[3]], int):
        error_ids[keys[3]] = error_ids.get(keys[3], 0) + 1
    if not isinstance(bus[keys[4]], str):
        error_ids[keys[4]] = error_ids.get(keys[4], 0) + 1
    elif not re.match("^[SOF]?$", bus[keys[4]]):
        error_ids[keys[4]] = error_ids.get(keys[4], 0) + 1
    if not bus[keys[5]] or not isinstance(bus[keys[5]], str):
        error_ids[keys[5]] = error_ids.get(keys[5], 0) + 1
    elif not re.match(r"^(2[0-3]|1[0-9]|0[1-9]):[0-5]\d$", bus[keys[5]]):
        error_ids[keys[5]] = error_ids.get(keys[5], 0) + 1

    bus_info[bus[keys[0]]] = bus_info.get(bus[keys[0]], 0) + 1

print("Line names and number of stops:")
for bus in bus_info:
    print(f"bus_id: {bus}, stops: {bus_info[bus]}")

