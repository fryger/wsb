from .scheduler import scheduler
from bs4 import BeautifulSoup
import requests
import json
from .models import FuelPrices


def currentMeanFuelCost():
    headers = ["PB95", "PB98", "ON", "LPG"]
    data = []

    url = 'https://www.reflex.com.pl/ceny-detaliczne-polska'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")

    table = soup.find("table", attrs={"class": "table-head-grey"})
    table_data = table.tbody.find_all("tr")

    for i in range(1, 5):
        data.append(round(sum([float(row.find_all("td")[i].text)
                               for row in table_data])/16, 2))
    pb95, pb98, on, lpg = data
    FuelPrices.objects.create(pb95=pb95, pb98=pb98, on=on, lpg=lpg)


# scheduler.remove_job('fuelCost')
#scheduler.add_job(currentMeanFuelCost, 'interval', days=1, id="fuelCost")
