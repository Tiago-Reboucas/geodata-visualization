# #------------------------------------------------- 01 - GEODATA_LOAD ----------------------------------------------#
import sqlite3
import urllib.request, urllib.parse, urllib.error
import ssl
import json
import time
import subprocess


# API Key
api_key = False
# If you have an API Key for Google Places enter it bellow and uncomment
# api_key = 'Bla1blAh...eTc29'

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Igonre SSL Certificate erros
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create database if doesn't exists
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)")

places_h = open("where.data")


def commit_print(start_time: float, count: int):
    conn.commit()
    time_taken = time.time() - start_time
    print("\r\nRetrieved", count, f"locations in{time_taken: 0.3f}s.\r\n")

def run_again(sentence: str):
    while True:
        more = input(sentence)
        if more.strip().upper() == 'Y': return True
        elif more.strip().upper() == 'N': return False

def add_to_database():
    count = 0
    max_count = 50
    start_time = time.time()
    for place in places_h:
        place = place.strip()

        # Check if address already exists
        cur.execute("SELECT address FROM Locations WHERE address = ?", (memoryview(place.encode()), ))

        try:
            cur.fetchone()[0]
            print("Address already on database:", place)
            continue
        except: pass

        # Add location to the database
        param = dict()
        param['address'] = place
        param['key'] = api_key

        url = service_url + urllib.parse.urlencode(param)

        data = urllib.request.urlopen(url, context=ctx)
        data = data.read().decode()
        
        try:
            js = json.loads(data)
        except: continue

        if "status" not in js or js["status"] != "OK":
            print("\r\n=========COULD NOT RETRIEVE DATA=========\r\n")
            continue

        cur.execute("INSERT INTO Locations (address, geodata) VALUES (?, ?)", (memoryview(place.encode()), memoryview(data.encode())))

        count += 1
        if count % 10 == 0:
            conn.commit()
            print("Commited 10")
            time.sleep(3)
            
        if count == max_count:
            commit_print(start_time, max_count)

            if run_again("Fetch more entries on this document (y/n)?: "): return True
            else: return False
    commit_print(start_time, count)

while True:
    if not add_to_database(): break

cur.close()
conn.close()

if run_again("\r\nWant to run 'geodata_dump.py' (y/n)?: "):
    subprocess.run(["py", "geodata_dump.py"])
    input("\r\nPress 'Enter' to quit.")
    quit()
else:    
    input("\r\nPress 'Enter' to quit.")