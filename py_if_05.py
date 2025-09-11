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


# jelka
for i in range(height + 1):
    # ispis praznina -> ' '
    print(' ' * (height - i), end='')
    
    # ispis zvjezdica -> '*'
    # print(symbol * ((i * 2) - 1))
    for j in range(i):
        print(symbol * ((i + 1) - ((j * 2) - 1)), end='')

    print()


# stablo
for k in range(3):
    print(' ' * (height - 2), end='')
    print('|' * 3)