import csv
from measurements.models import Measurement

def create_measurement(row):
    value, notes = row
    measurement = Measurement.objects.create(
        value=value, notes = notes
    )
    return measurement

def import_measurement():
    with open("data/measurements_data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            create_measurement(row)