print("RUUMIDE TÄITUVUSE KALKULAATOR")
print("----------------------------")

print("Ruumi tüübid:")
print("1. Toitlustus")
print("2. Kaubandus")
print("3. Teenindus")
print("4. Sport")
print("5. Üritus")

ruum = input("Mis tüüpi ruumiga on tegemist? ").lower()

suurus = float(input("Kui suur ruum on (m2)? "))
teenindajad = int(input("Mitu teenindajat ruumis on? "))

if ruum == "toitlustus":
    protsent = 50
    maksimum = float("inf")

elif ruum == "kaubandus":
    protsent = 50
    maksimum = float("inf")

elif ruum == "teenindus":
    protsent = 25
    maksimum = float("inf")

elif ruum == "sport":
    protsent = 25
    maksimum = 100

elif ruum == "üritus":
    protsent = 50
    maksimum = 200

else:
    print("Sellist ruumi tüüpi ei ole!")
    exit()

# Arvutame lubatud inimeste arvu
lubatud = suurus * protsent / 100 / 4

# Kontrollime maksimaalset inimeste arvu
lubatud = min(lubatud, maksimum)

# Lahutame teenindajad
vastus = lubatud - teenindajad

if vastus < 0:
    vastus = 0

print("----------------------------")
print("TULEMUS:")
print(f"{suurus} m2 ruumis on lubatud maksimaalselt {vastus:.2f} külastajat.")
