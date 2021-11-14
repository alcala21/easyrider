# Write your awesome code here
import json
from typing import List
import re

data = json.loads(input())

bus_info = dict()
stop_counts = {"start": [], "finish": [], "stops": dict()}

for bus in data:
    busid = bus["bus_id"]
    if not bus_info.get(busid, False):
        bus_info[busid] = {"start": 0, "finish": 0}
    if bus["stop_type"] == "S":
        bus_info[busid]["start"] += 1
        stop_counts["start"] += [bus["stop_name"]]
    elif bus["stop_type"] == "F":
        bus_info[busid]["finish"] += 1
        stop_counts["finish"] += [bus["stop_name"]]

    stop_counts["stops"][bus["stop_name"]] = stop_counts["stops"].get(bus["stop_name"], 0) + 1

print_next = True
for bus in bus_info:
    if bus_info[bus]["start"] == 0 or bus_info[bus]["finish"] == 0:
        print(f"There is no start or end stop for the line: {bus}")
        print_next = False
        break

if print_next:
    stop_list = sorted(set(stop_counts['start']))
    transfers = sorted(set([k for k, x in stop_counts["stops"].items() if x > 1]))
    finish_list = sorted(set(stop_counts['finish']))
    print(f"Start stops: {len(stop_list)} {stop_list}")
    print(f"Transfer stops: {len(transfers)} {transfers}")
    print(f"Finish stops: {len(finish_list)} {finish_list}")
