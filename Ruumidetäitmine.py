ruum = input('Mis tüüpi ruumiga on tegemist? (toitlustus, kaubandus, teenindus, sport, üritus): ')
if ruum == 'sport':
    pindala = round(float(input('Sisesta ruumi pindala (m2): ')), 2)
    inimeste_arv = int(input('Sisesta inimeste arv: '))

print (str(pindala) + ' m2 ruumi on lubatud maksimaalselt ' + str(inimeste_arv) + ' inimest, kuna ruumi pindala on ' + str(pindala) + ' m2 ja ruumi tüüp on ' + str(ruum) + '.')
