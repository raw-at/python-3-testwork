import csv

with open('FL_insurance_sample.csv') as csvfile:
    readCsv = csv.reader(csvfile,delimiter=',')

    
    for row in readCsv:
        print(row[-2])