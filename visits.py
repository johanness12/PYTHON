from pprint import pprint
file = open('visits.csv', encoding='utf-8')

visits = {}
for row in file:
    pair = row.strip('\ufeff').split(';')
    visits[pair[0].strip()] = int(pair[1].strip())

file.close()

max =0 
max_key = ''

for key in visits:
    if visits[key] > max:
        max_key = key
        max = visits[key]

#pprint(visits)

print('Kõige rohkem ülastusi oli'
 + max_key)
+ ', siis külastas parki ' + str(max) + ' inimest.'
pprint(visits)