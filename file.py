file = open('visits.csv', encoding='utf-8')

for row in file:
    print(row)

file.close()