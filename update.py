#!/bin/python

originals = []
with open("sensor_database.csv") as fp:
    for line in fp.readlines():
        parts = line.split(",")
        print(parts)
        newline = parts[1]+";"+parts[2]
        originals.append(newline)

latest = []
with open("sensor_database2.csv") as fp:
    for line in fp.readlines():
        latest.append(line)

oset = set(originals)
lset = set(latest)

nset = oset.union(lset)

with open("sensor_database3.csv","w") as fp:
    for line in sorted(nset):
        fp.write(line)
