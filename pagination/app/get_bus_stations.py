import csv

def get_bus_stations(file: csv):
    with open(file, encoding='cp1251', newline='') as bs:
        list_of_stations = [row for row in csv.DictReader(bs)]
        return list_of_stations