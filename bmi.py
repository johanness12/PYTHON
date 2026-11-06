# Variant 1

length = float(input('sisesta oma pikkus (cm): '))
weight = float(input('sisesta oma kaal (kg): '))

bmi = round(weight / (length / 100) ** 2, 1)
print('Sinu kehamassiindeks on ' + str(bmi))
if bmi < 16:
    print('Tõsine alakaal')
elif 16 <= bmi < 19:
    print('alakaal')
elif 19 <=bmi < 25:
    print('normaalkaal')
elif 25 <= bmi < 30:
    print('Ülekaal')
elif 30 <= bmi < 35:
    print('Rasvumine')
elif 35 <= bmi < 40:
    print('tugev rasvumine')
elif 40 <= bmi:
    print('Tervisele ohtlik rasvumine')

'''
# Variant 2
length = float(input('sisesta oma pikkus (cm): '))
weight = float(input('sisesta oma kaal (kg): '))

bmi = round(weight / ((length / 100) ** 2), 1)
print('Sinu kehamassiindeks on ' + str(bmi))
'''