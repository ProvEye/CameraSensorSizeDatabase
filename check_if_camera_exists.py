import sys

camera_make = sys.argv[1]
camera_model = sys.argv[2]

query = camera_make.lower()+" "+camera_model.lower()

print("query is:{}".format(query))

originals = []
with open("sensor_database.csv") as fp:
    for line in fp.readlines():
        originals.append(line)

for ofile in originals:
    if(query in ofile.lower()):
        print(ofile)
        exit(0)
