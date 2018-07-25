import csv
import time

start_date = '1986-03-13'
data = {}
data_file = csv.reader(open('../data/01-data_7_categories.csv', 'r'))
stock_file = csv.reader(open('../data/MSFT.csv', 'r'))
dates = set()
write_file = open('data.csv', 'w')

for row in data_file:
    if row[0] < start_date:
        continue
    data[row[0]] = row[1:]
    dates.add(row[0])

for row in stock_file:
    if row[0] in dates:
        if row[1] > row[4]:
            data[row[0]].append(-1)
        elif row[1] < row[4]:
            data[row[0]].append(1)
        else:
            data[row[0]].append(0)

heading = 'date,' + ','.join(data['date']) + ', tag'
# print(heading)
del data['date']
keys = list(data.keys())
keys.sort()
write_file.write(heading + '\n')

for key in keys:
    if len(data[key]) < 8:
        continue
    else:
        line = key+',' + ','.join(str(x) for x in data[key])
        write_file.write(line + '\n')
