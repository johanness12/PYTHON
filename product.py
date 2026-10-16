<<<<<<< HEAD
name = input('Sisesta toote nimi: ').lower()

product = ''
price = 0.0

if name == 'maasikas':
    product = name
    price = 5
elif name == 'vaarikas':
    product = name
    price = 5.2
  
print(product.capitalize() + ' makasb ' + str(price) + ' eurot '
       if product != ''
=======
name = input('Sisesta toote nimi: ').lower()

product = ''
price = 0.0

if name == 'maasikas':
    product = name
    price = 5
elif name == 'vaarikas':
    product = name
    price = 5.2
  
print(product.capitalize() + ' makasb ' + str(price) + ' eurot '
       if product != ''
>>>>>>> a03022b235ac4133ba25a86aa31969d0f0c14bb0
         else 'Meil ei ole sellist toodet')