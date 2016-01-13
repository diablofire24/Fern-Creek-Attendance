
import csv

with open("attendanceData.csv", "r") as file:
    csvFile = csv.reader(file, delimiter = ",", lineterminator="\n")
    for x in range(4):
        a = next(csvFile)
        if x == 3:
            print(a)
