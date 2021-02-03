# coding: UTF-8
"""
Script: pythonProject0/temp
Création: admin, le 15/01/2021
"""


# Imports
import requests
import mysql.connector

# Fonctions
def get_temperature(ville):
    url="http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&units=metric&lang=fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['temp'])

def set_temperature_bdd(ville, temperature):
     cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bdd_temperaturevilles')
     cursor = cnx.cursor()
     update_val = ("UPDATE temperaturevilles SET temperature = (%s) WHERE ville = (%s)")
     data = (temperature, ville)
     cursor.execute(update_val, data)
     cnx.commit()
     cursor.close()
     cnx.close()



# Programme principal
def main():
    #print(get_temperature("grenoble"))
    toute_ville=["lyon", "grenoble", "paris", "lens"]

    for ville in toute_ville:
        print(get_temperature(ville))
        set_temperature_bdd(ville, get_temperature(ville))


if __name__ == '__main__':
    main()
# Fin
