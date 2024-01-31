numbers = [ 4,4, 6 ,6, 12 , 3, 5 ,7 , 3 , 15]

# wiek = float(input("podaj swoj wiek "))
# if wiek > 17:
#       print("jestes pełnoletni")
# else:
#       print("nie jestem pełnoletni")

# inp = input("ile znakow ")
# ile = len(inp)
# print(ile)

# imie = input("podaj imie ")
# nazwisko = input("podaj nazwisko ")

# ile = len(imie + nazwisko)
# print(ile)


# inp = int(input("podaj wartosc liczbowa"))
# c = ((inp - 5)*2)
# print(c)

# a= int(input("podaj liczbe:"))
# a = float(a)
# print(a)

# temp = float(input("podaj temperature powieterza w stopniach celcujsza "))
# Fah = float(temp *2 + 30)
# print(Fah)


# inp = input("podaj ciag znakow")
# print(inp[0])
# print(inp[-1])

# 1. Napisz program, który poprosi użytkownika o wprowadzenie swojego imienia i przechowa je w zmiennej. Następnie wyświetl komunikat "Witaj, [imię]!".


# inp = input("podaj imie ")
# print("witaj " + inp)


# 2. Stwórz dwie zmienne liczbowe i przypisz im wartości. Następnie wykonaj operację dodawania tych zmiennych i wyświetl wynik.

# inpa = float(input("podaj liczbe a "))
# inpb = float(input("podaj liczbe b "))
# print(inpa + inpb)


# 4. Zadeklaruj zmienną tekstową, która będzie przechowywać dowolny ciąg znaków. Następnie wyświetl długość tego ciągu.

# inp = input("podaj ciag znakow ")
# print(len(inp))

# 5. Zadeklaruj dwie zmienne tekstowe przechowujące imię i nazwisko. Połącz te zmienne w jeden ciąg znaków i wyświetl wynik.

# imie = input("podaj imie")
# nazw = input("podaj nazwisko")
# print(len(imie + nazw))


# 7. Zadeklaruj zmienną przechowującą wartość logiczną (True lub False). Następnie wykonaj negację tej wartości i wyświetl wynik.

# a = float(input( "a: "))
# b = float(input( "b: "))

# if a == b:
#       print(True)
# else:
#       print(False)

# 1. Utwórz pustą listę o nazwie "numbers".
# numbers = list()

# 2. Poproś użytkownika o podanie 5 liczb i dodaj je do listy.
# list = []
# i = 0 
# while i < 5:
#     liczby = int(input("podaj 5 liczb "))
#     list.append(liczby)
#     i += 1
# print(list)`

# 3. Oblicz sumę liczb znajdujących się w liście "numbers".

# i = 0 
# suma = 0 
# while i < len(numbers):
#       suma = float(numbers[i]) + (suma)
#       i+= 1
# print(suma)



# 4. Znajdź największą liczbę w liście "numbers".

# i = 0
# maxl = list[0]
# while i < len(list):
#       if maxl < list[i]:
#             maxl = list[i]
#       i += 1
# print(maxl)

            
 
# 5. Znajdź najmniejszą liczbę w liście "numbers".

# i = 0 
# maxl = list[0]
# while i > len(list):
#       if maxl < list[i]:
#             maxl = list[i]
#       i += 1
# print(maxl)



# 6. Znajdź średnią arytmetyczną liczb w liście "numbers".
# suma = 0 
# i = 0 
# while i < len(list):
#       suma += list[i]
#       i += 1
# print(suma/len(list)) 



# 7. Znajdź ilość liczb parzystych w liście "numbers".
# i = 0 
# ile = 0 
# while i < len(list):
#       if list[i] % 2 == 0:
#             ile += 1
#       i += 1 
# print(ile)


# 8. Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers".
# duplicates = []
# i = 0
# while i < len(numbers):
#       if numbers.count(numbers[i]) > 1 and numbers[i] not in duplicates:
#             duplicates.append(numbers[i])
#       i += 1 
# print(duplicates)
      

# 9. Usuń wszystkie powtarzające się elementy z listy "numbers".

# new_list = []

# i = 0
# while i < len(numbers):
#     if numbers[i] not in new_list:
#         new_list.append(numbers[i])
#     i += 1
# print(new_list)


# 10. Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers".'

# squares = []
# i = 0
# while i < len(numbers):
#     o = numbers[i]**2
#     squares.append(o)
#     i += 1
# print(squares) 

# Wyświetl wszystkie liczby z listy "numbers" w odwrotnej kolejności
# numbers = [ 4,4, 6 ,6, 12 , 3, 5 ,7 , 3 , 15]
# i = -1
# while i > -len(numbers):
#       print(numbers[i])
#       i -= 1
# Poproś użytkownika o podanie liczby. Sprawdź, czy liczba ta znajduje się w liście "numbers".
# i = 0 
# inp = int(input())
# if inp in numbers:
#       print("tak")
# else:
#       print("nie")

# Wyświetl indeks pierwszego wystąpienia danej liczby w liście "numbers".
# inp = int(input())
# i = 0
# while i < len(numbers):
#     if inp == numbers[i]:
#         print(i)
#         break
#     i += 1

# Znajdź ilość liczb większych niż 10 w liście "numbers".
# i = 0
# ile = 0
# while i < len(numbers):
#       if numbers[i] > 10:
#             ile += 1
#       i += 1 
# print(ile)


# Posortuj listę "numbers" w kolejności malejącej.

# numbers.sort(reverse=True)
# print(numbers)
# Znajdź drugą największą liczbę w liście "numbers".
# numbers = [11,2,10,3,1,2,4,11]

# max1 = float('-inf')
# max2 = float('-inf')

# i = 0
# while i < len(numbers):
#     if numbers[i] > max1:
#         max2 = max1
#         max1 = numbers[i]
#     elif numbers[i] > max2 and numbers[i] != max1:
#         max2 = numbers[i]
#     i += 1


# print(f"max1 {max1}")
# print(f"max2 {max2}")

# Stwórz nową listę o nazwie "doubled_numbers" zawierającą podwojoną wartość każdej liczby z listy "numbers".
# doubled_numbers = []
# i = 0
# while i < len(numbers):
#       two = numbers[i]*2
#       doubled_numbers.append(two)
#       i += 1
# print(doubled_numbers)

# Zlicz ilość wystąpień danej liczby w liście "numbers".`
# i = 0 
# inp = float(input(""))
# ile = 0 
# while i < len(numbers):
#       if numbers[i] == inp:
#             ile += 1
#       i += 1
# print(ile)
      
# Wyświetl wszystkie liczby z listy "numbers" z ich indeksami.
# i = 0
# while i < len(numbers):
#       print(f"  {i}  {numbers[i]}")
#       i += 1
# 1. Wyświetl liczby od 1 do 10.
# 2. Oblicz sumę liczb od 1 do 100.
# 3. Wyświetl wszystkie parzyste liczby od 1 do 50.
# 4. Oblicz iloczyn liczb od 1 do 5.
# 5. Wyświetl odwróconą wersję napisu "Hello World!".
# 6. Wyświetl wszystkie litery z podanego słowa.
# 7. Oblicz sumę elementów listy liczb.
# 8. Wyświetl wszystkie liczby od 20 do 30, które są podzielne przez 3.
# 9. Znajdź największą liczbę w liście.
# 10. Wyświetl wszystkie liczby od 1 do 100, które są podzielne jednocześnie przez 3 i 5.
# 11. Oblicz średnią arytmetyczną z listy liczb.
# 12. Wyświetl wszystkie litery z podanego zdania, pomijając spacje.
# 13. Oblicz silnię liczby podanej przez użytkownika.
# 14. Wyświetl tabliczkę mnożenia (od 1 do 20).
# 15. Sprawdź, czy podane słowo jest palindromem.
# 16. Zamień wszystkie litery w podanym napisie na wielkie litery.
# 17. Wyświetl liczby od 1 do 10 w odwrotnej kolejności.











