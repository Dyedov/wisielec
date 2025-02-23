import os

while True:
    os.system("cls")

    print('Witaj w grze! "Zgadni słowo" \nZasady gry: \njedna osoba wpisuje słowo, druga osoba je zgaduje')
    print('- Start -')
    haslo = input('Wpisz hasło do odgadnięcia: ').lower()

    os.system("cls")

    litery = list(haslo)
    # print(litery)
    newhaslo = []
    liczbaZyc = 5

    for i in range(len(haslo)):
        newhaslo.append('-')
    # print(newhaslo)
    print(''.join(newhaslo))

    while litery != newhaslo:
        litera = input('wpisz litere: ').lower()
        if litera in haslo:
            for l in range(len(haslo)):
                if litera == litery[l]:
                    newhaslo[l] = litera
            print(''.join(newhaslo))
            if litery == newhaslo:
                print('Wygrałeś!')

        else:
            liczbaZyc -= 1
            print('straciłeś życie')
            # print('pozostały tobie %d ' % (liczbaZyc),'życia')
            print(f'pozostały tobie {liczbaZyc} życia')
            if liczbaZyc == 0:
                print('Przegrałeś')
                break
    if input('Czy chcesz zagrać jeszcze raz? tak/nie ').lower() != 'tak':
        print('Gra zakończona')
        break




















