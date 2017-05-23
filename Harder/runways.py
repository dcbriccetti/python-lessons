'''A starting point for doing some things with runway information'''

from random import choice
import csv


class Runway:
    def __init__(self, airport_id, runway_name):
        self.airport_id = airport_id
        self.runway_name = runway_name

    def __str__(self):
        return self.airport_id + ' ' + self.runway_name

airports_by_id = {}

# Data come from from http://ourairports.com/data/
with open("/Users/daveb/Documents/Flying/data/airports.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        airport_id = line[1]
        airport_name = line[3]
        airports_by_id[airport_id] = airport_name

runways = []

with open("/Users/daveb/Documents/Flying/data/runways.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        airport_id = line[2]
        runway_name = line[8]
        runways.append(Runway(airport_id, runway_name))

runway = choice(runways)
airport = airports_by_id[runway.airport_id]
print(airport, runway)
