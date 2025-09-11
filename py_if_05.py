'''
Napisite program koji ispisuje bozicno drvce, a korisnik moze birati znak i visinu

Primjer:
Visina je 8
Znak je *

       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
     | | |
     | | |
'''


# height = int(input('Upisite visinu jelke: '))
# symbol = input('Upisite simbol za crtanje jelke: ')
height = 10
symbol = '*'

# redovi
for i in range(1, height + 1):
    # stupci
    for j in range(1, (height * 2)):
        if 
        print(' ' * int((height / 2) + i), end='')
        print(symbol * ((j * 2) - 1))


# stablo
for k in range(3):
    print(' ' * (height - 2), end='')
    print('|' * 3)