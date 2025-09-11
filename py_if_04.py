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


height = int(input('Upisite visinu jelke: '))
symbol = input('Upisite simbol za crtanje jelke: ')


# jelka
for i in range(height + 1):
    # ispis praznina -> ' '
    print(' ' * (height - i), end='')
    
    # ispis zvjezdica -> '*'
    print(symbol * ((i * 2) - 1))


# stablo
for j in range(3):
    print(' ' * (height - 2), end='')
    print('|' * 3)