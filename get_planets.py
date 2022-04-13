from bs4 import BeautifulSoup
import requests

url = "https://nssdc.gsfc.nasa.gov/planetary/factsheet/"
result = requests.get(url).text

data = BeautifulSoup(result, features="html.parser")
table = data.body.find_all('p')[1].table

# Will contain all the planets but Moon till Mars
planets = {}
planets_order = []
characteristics = ["Distance from Sun", "Diameter", "Orbital Velocity"]
for num_tr, tr in enumerate(table.find_all("tr")[:-1]):
    if num_tr == 0:  # First row contains The Planet Names But the MOON
        for num_td, td in enumerate(tr.find_all("td")[:6]):
            if num_td != 0:  # Cuz the first one is blank
                planets_order.append(td.b.a.text)
                planets[td.b.a.text] = {"range": num_td}
    else:
        if tr.td.b.a.string in characteristics:
            for planet in planets:  # If it is in the characteristics we want
                # Ignore this Useless error
                planets[planet][tr.td.b.a.string] = \
                    float(tr.find_all("td")[1:][planets[planet]["range"]-1].string.replace(',', '').replace('*', ''))

del planets["MOON"]
planets_order.pop(planets_order.index("MOON"))


def get_planets_dict():
    return planets
