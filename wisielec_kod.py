"""
1. musimy podać hasło
2. musimy to hasło wyświetlić jako -----
3. musimy odpytywać użytkownika cały czas o litery
4. musimy zmniejszać życia użytkownika
5. wyświetlić informacje o wygranej lub przegranej

6. uwzglednij male i duze litery

WERSJA 1
Ustawiamy hasło w kodzie

WERSJA 2
Program losuje hasło z listy haseł

WERSJA 3
Podajemy hasło w konsoli, a program wymazuje je z konsoli i zamiast niego wyświetla -----
"""

haslo = 'masło'
litery = list(haslo)
# print(litery)
newhaslo = []
liczbaZyc = 5

for i in range(len(haslo)):
    newhaslo.append('-')
# print(newhaslo)
print(''.join(newhaslo))

while litery != newhaslo:
    litera = input('wpisz litere: ')
    if litera in haslo:
        for l in range(len(haslo)):
            if litera == litery[l]:
                newhaslo[l] = litera
                print(''.join(newhaslo))

    else:
        liczbaZyc -= 1
        print('straciłeś życie')
        # print('pozostały tobie %d ' % (liczbaZyc),'życia')
        print(f'pozostały tobie {liczbaZyc} życia')
        if liczbaZyc == 0:
            print('przegrałeś')
            break
print('Wygrałeś!')













