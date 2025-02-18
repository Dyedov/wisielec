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
print(litery)
newhaslo = []

for i in range(len(haslo)):
    newhaslo.append('-')
print(newhaslo)

litera = input('wpisz litere: ')
for l in litery:
    if litera == l:
        newhaslo.append(litera)
        print(newhaslo)
    else:
        print('-')



    #     newhaslo.append(litera)
    #     print(newhaslo)





# for index, litera in enumerate(haslo):
#     print(f"Indeks: {index}, litera: {litera}")

# slowo = ''
#
# for i in range(len(haslo)):
#     slowo+='-'
# print(slowo)
#
# litera = input('wpisz litere: ')
# if litera in haslo:
#     print('tak')
# else:
#     print('nie')









