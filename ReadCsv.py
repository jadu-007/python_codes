import csv

with open('Combine_News.csv', newline='') as f:
    reader = csv.reader(f)
    for data in reader:
        print(data[0])
