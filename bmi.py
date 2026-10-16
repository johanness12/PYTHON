# Variant 1
'''
length = float(input('sisesta oma pikkus (cm): '))
weight = float(input('sisesta oma kaal (kg): '))

bmi = round(weight / (length / 100) ** 2, 1)
print('Sinu kehamassiindeks on ' + str(bmi))
'''
# Variant 2
length = float(input('sisesta oma pikkus (cm): '))
weight = float(input('sisesta oma kaal (kg): '))

bmi = round(weight / ((length / 100) ** 2), 1)
print('Sinu kehamassiindeks on ' + str(bmi))