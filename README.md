# Visualização de Geodados / Geodata Visualization

### Funcionalidade / Functionality
- Abre o arquivo `where.data` que contém várias localidades no globo;
- Adquire os dados de geolocalicação (Latitude, Longitude e Endereço completo) através do Google Geocode API (ou dr-chuck API caso não tenha uma chave);
- Salva os Geodados no banco de dados `geodata.sqlite`;
- Escreve um arquivo `where.js` que será usado para abrir todas as localidades em um mapa através do `where.html` (arquivos .html e .data cedidos por [dr-chuck](https://py4e-data.dr-chuck.net/));
---
- *Opens the file `where.data` with various locations around the globe*;
- *Get their Geodata (Latitude, Longitude and Full address) on Google Geocode API (or dr-chuck API if you haven't a key)*;
- *Save the Geodata in the database `geodata.sqlite`;*
- *Write `where.js` file to be used to open all the locations on a map in `where.html` (.html and .data file provided by [dr-chuck](https://py4e-data.dr-chuck.net/))*;

### Modulos Necessários / Necessary Modules
- sqlite3
- urllib.request, urllib.parse, urllib.error
- ssl
- json
- time
- subprocess

### Recomendações / Recomendations
- Ajuste o `max_count` na ***linha 47*** em `geodata_load.py` para alterar quantas procuras o programa deverá fazer antes de perguntar por mais (padrão 50).
---
- *Set the `max_count` in `geodata_load.py` ***line 47*** to change how many searches the program will do before asking for more (default 50)*.

### Como Usar / How to use
1. Se possuir uma ***Chave Google Geocode API***, abra `geodata_load.py` com um editor, retire de comentário a ***linha 13*** e insira sua chave em `api_key = ""`;
2. Rode `geodata_load.py`, o programa ira escanear `where.data` e criará o banco de dados `geodata.sqlite`;
3. Se o programa rodar todo o arquivo `where.data` ou for selecionado **"N"** quando perguntado, o programa irá perguntar se deseja rodar `geodata_dump.py`;
4. Rode `geodata_dump.py` para escrever os dados do banco de dados em `where.js`;
5. Abra `where.html` em um browser de internet para visualizar todas as localidades em um mapa mundi.
---
1. *If you have a ***Google Geocode API Key***, open `geodata_load.py` with an editor, uncomment the ***line 13*** and insert your key in `api_key = ""`*;
2. *Run `geodata_load.py`, the program will scan `where.data` and create the database `geodata.sqlite`*;
3. *If the program ends with the `where.data` or you select **"N"** when prompted, the program will ask to run `geodata_dump.py`*;
4. *Run `geodata_dump.py` to write the database data in the `where.js`*;
5. *Open `where.html` in a browser to visualize all the locations around the globe*.  

<p>&nbsp;</p>

OBS: Créditos para [dr-chuck](https://py4e-data.dr-chuck.net/) por prover `where.data` e `where.html`, necessários para este projeto.
---
*OBS: Credits to [dr-chuck](https://py4e-data.dr-chuck.net/) for providing `where.data` and `where.html` so this project could be made*.
