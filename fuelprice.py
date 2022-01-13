import requests
import json

# Panaudojamas API gauti aviacinio kuro Jet A1 kaina

fuel = requests.get("http://api.eia.gov/series/?api_key=Jc7XaMChUDUcw1q7pTMSiM7QeHf7QHiMhR8iLgd6&series_id=STEO.JKTCUUS.A")
jsonas = fuel.text

info = json.loads(jsonas)

kuras = info["series"][0]["data"][0][1]

converting = 0.00264172052

usd_litre = kuras * converting

eur = 0.88 

usd_to_eur = usd_litre * eur

reikalinga_kaina = usd_to_eur  # 0.484 

price = round(reikalinga_kaina, 3)

consumption = 3.967

kainuoja = round(consumption * price, 3)

kainuoja2 = 1.92


