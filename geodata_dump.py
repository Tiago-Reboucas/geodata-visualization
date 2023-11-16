import sqlite3
import json

conn = sqlite3.connect("geodata.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM Locations")
file_h = open("where.js", "w", encoding="utf-8")
file_h.write("myData = [\n")

count = 0
for entry in cur:
    data = str(entry[1].decode())
    
    try:
        data = json.loads(data)
    except: continue

    if not ("status" in data and data["status"] == "OK"): continue

    
    address = data['results'][0]['formatted_address']
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']

    if lat == 0 or lng == 0: continue

    count += 1
    if count > 1: file_h.write(",\n")
    
    write = "[" + str(lat) + "," + str(lng) + "," + "\"" + str(address) + "\"" + "]"
    write.replace('"', "'")
    file_h.write(write)

write = "\n];"
file_h.write(write)

cur.close()
conn.close()
file_h.close()

print("\r\nDatabase read, " + str(count), "locations added to the map.")
print("Open 'where.html' to view all the places in a map.")
input("\r\nPress 'Enter' to quit.")