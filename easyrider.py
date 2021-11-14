# Write your awesome code here
import json

data = json.loads(input())


def decimal(t):
    str_vals = t.split(":")
    return float(str_vals[0]) + float(str_vals[1])/60


def positive_timediff(t1, t2):
    return decimal(t2) > decimal(t1)


time_info = dict()

for station in data:
    bus_id = station["bus_id"]
    if not time_info.get(bus_id, False):
        time_info[bus_id] = {}
    time_info[bus_id][station['stop_id']] = {
        "name": station['stop_name'],
        "time": station['a_time'],
        'next_stop': station['next_stop']}

print("Arrival time tests:")
ok = True
for bus_id, bus_info in time_info.items():
    for id, values in bus_info.items():
        next_stop = values['next_stop']
        if next_stop in bus_info:
            if not positive_timediff(values['time'], bus_info[next_stop]['time']):
                print(f"bus_id line {bus_id}: wrong time on station {bus_info[next_stop]['name']}")
                ok = False
                break

if ok:
    print("OK")

