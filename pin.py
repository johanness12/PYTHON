# Variant 1
'''
pin = input('Sisesta oma PIN-kood: ')

if pin == '1234':
    print('õige PIN-kood! Tere tulemast!')
else:
    print('Vale PIN-kood! Enesehävitusrežiim aktiveeritud...')
'''
 #Variant 2
print('õige PIN-kood! Tere tulemast!'
      if input('Sisesta oma PIN-kood: ') == '1234' 
      else 'Vale PIN-kood! Enesehävitusrežiim aktiveeritud...')