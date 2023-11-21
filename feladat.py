import json 


adatbazis = []

with open("database.json", "r", encoding="utf8") as fájl:
    adatbazis = json.loads(fájl)

print(adatbazis)