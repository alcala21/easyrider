# Write your awesome code here
import json
from typing import List

data = json.loads(input())

error_ids = dict()
keys: List[str] = ['bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time']

for bus in data:
    if not bus[keys[0]] or not isinstance(bus[keys[0]], int):
        error_ids[keys[0]] = error_ids.get(keys[0], 0) + 1
    if not bus[keys[1]] or not isinstance(bus[keys[1]], int):
        error_ids[keys[1]] = error_ids.get(keys[1], 0) + 1
    if not bus[keys[2]] or not isinstance(bus[keys[2]], str):
        error_ids[keys[2]] = error_ids.get(keys[2], 0) + 1
    if bus[keys[3]] is None or not isinstance(bus[keys[3]], int):
        error_ids[keys[3]] = error_ids.get(keys[3], 0) + 1
    if not isinstance(bus[keys[4]], str):
        error_ids[keys[4]] = error_ids.get(keys[4], 0) + 1
    elif bus[keys[4]] not in ['', 'S', 'O', 'F']:
        error_ids[keys[4]] = error_ids.get(keys[4], 0) + 1
    if not bus[keys[5]] or not isinstance(bus[keys[5]], str):
        error_ids[keys[5]] = error_ids.get(keys[5], 0) + 1

print("Type and required field validation:", str(sum(error_ids.values())), "errors")
for k in keys:
    print(f"{k}: {error_ids.get(k, 0)}")
