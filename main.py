import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
#import matplotlib.pyplot as plt
from temperatureanalytics import TemperatureAnalytics

data_path = 'klementinum.xlsx'
data_sheet_name = 'data'
temperature_data = pd.read_excel(data_path, sheet_name=data_sheet_name)

temperature_analytics = TemperatureAnalytics(temperature_data)

def vyber(volba):
  if volba == "1":
    rok = int(input("Zadejte rok: "))
    prumer = temperature_analytics.get_average_temperature(rok)
    print(f"Průměrná teplota v roce {rok}: {prumer} °C")
    pass
  elif volba == "2":
    rok = int(input("Zadejte rok: "))
    min, datemin = temperature_analytics.get_min_temperature(rok)
    max, datemax = temperature_analytics.get_max_temperature(rok)
    print(f"Minimální teplota v roce {rok}: {min} °C, datum: {datemin['den']}.{datemin['měsíc']}.{datemin['rok']}")
    print(f"Maximální teplota v roce {rok}: {max} °C, datum: {datemax['den']}.{datemax['měsíc']}.{datemax['rok']}")
    pass
  elif volba == "3":
    rok = int(input("Zadejte rok: "))
    prumery = temperature_analytics.get_monthly_averages(rok)
    print(f"Měsíční průměry v roce {rok}: {prumery} °C")
    pass
  elif volba == "4":
    zacatek = int(input("Zadejte rok začátku: "))
    konec = int(input("Zadejte rok konce: "))
    print(f"Průměrné roční teploty v rozmezí od {zacatek} do {konec}")
    temperature_analytics.plot_annual_temperature_averages(zacatek, konec)
    pass
  elif volba == "5":
    zacatek = int(input("Zadejte rok začátku: "))
    konec = int(input("Zadejte rok konce: "))
    print(f"Trend ročních teplot v rozmezí od {zacatek} do {konec}")
    temperature_analytics.analyze_temperature_trends(zacatek, konec)
    #5 - Vykreslit trendy
  elif volba == "6":
    day = input("Zadejte den: ")
    month = input("Zadejte měsíc: ")
    year = input("Zadejte rok: ")
    min, max = temperature_analytics.plot_daily_temperature(day, month, year)
    print(f"Minimální teplota v den {day}.{month}.{year}: {min}")
    print(f"Maximální teplota v den {day}.{month}.{year}: {max}")
  elif volba == "0":
    #0 - Konec
    return 0

vybornavolba = temperature_analytics.menu()
vyber(vybornavolba)