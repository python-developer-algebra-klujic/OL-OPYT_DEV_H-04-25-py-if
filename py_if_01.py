'''
Kreirajte listu od 1 do broja 30. Ispišite sve brojeve koji su djeljivi s 3, 6 i 9
    Provjera je li broj djeljiv s nekim drugim radimo pomoću % (modulo) operanda.
        15 % 3 NEMA ostatka, odnosno to je 0 pa je 15 djeljiv s 3.
        16 % 3 je 1, odnosno NIJE jednak 0 pa 16 NIJE djeljiv s 3.
'''

for number in range(1, 31):
    if number % 3 == 0:   
        print(f'Broj {number} JE djeljiv s 3')
    if number % 6 == 0:
        print(f'Broj {number} JE djeljiv s 6')
    if number % 9 == 0:
        print(f'Broj {number} JE djeljiv s 9')
    else:
        print(f'Broj {number} NIJE djeljiv niti s 3, niti sa 6, niti s 9')
