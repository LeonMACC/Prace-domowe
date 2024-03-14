def dodaj_do_notatki():
    nazwa_pliku = input("Podaj nazwę pliku dla notatek: ")

    try:
        with open(nazwa_pliku + ".txt", "a") as plik:
            while True:
                linijka = input("Wpisz tekst do notatki (wpisz 'koniec', aby zakończyć): ")
                if linijka.lower() == 'koniec':
                    break
                plik.write(linijka + "\n")
        print("Notatka została dodana do pliku", nazwa_pliku + ".txt")
    except IOError:
        print("Wystąpił błąd podczas zapisywania do pliku.")

dodaj_do_notatki()
