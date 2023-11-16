# Geodata Visualization

### Functionality
- Opens the file `where.data` with various locations around the globe;
- Get their Geodata (Latitude, Longitude and Full address) on Google Geocode API (or dr-chuck API if you haven't a key);
- Save the Geodata in a database `geodata.sqlite`;
- Write `where.js` file to be used to open all the locations on a map in `where.html`, (.html and .data file provided by [dr-chuck](https://py4e-data.dr-chuck.net/));

### Necessary Modules
- sqlite3
- urllib.request, urllib.parse, urllib.error
- ssl
- json
- time
- subprocess

### Recomendations
- Set the `max_count` in `geodata_load.py` line 47 to change how many searches the program will do before asking for more (default 50).

### How to use
1. If you have a ***Google Geocode API Key***, open `geodata_load.py` with an editor, uncomment the ***line 13*** and insert your code in `api_key = ""`;
2. Run `geodata_load.py`, the program will scan `where.data` and create a database `geodata.sqlite`;
3. If the program ends with the `where.data` or you select **"N"** when prompted, the program will ask to run `geodata_dump.py`;
4. Run `geodata_dump.py` to write the database data in the `where.js`;
5. Open `where.html` in a browser to visualize all the locations around the globe.

OBS: Credits to [dr-chuck](https://py4e-data.dr-chuck.net/) for providing `where.data` and `where.html` so this project could be made.
