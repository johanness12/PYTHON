from turtle import *

cube_count = int(input('Sisestage kuubikute arv: '))

for N in range(cube_count):
    for i in range(4):
        forward(100)
        left(90)
    N += 1 
    right(70)
    forward(50)

done()