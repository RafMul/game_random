import sys
import random
print('Witaj w grze w orzeł i reszka')


class Gra():
    def __init__(self):

        self.tablica = []  # tablica wybrana liczba
        self.tablica1 = []  # tablica ilość przejść
        self.tablica2 = []  # tablica wyniku komputera
        self.tablica3 = []  # tablica wygranych i przegranych
        #self.i = int(input('Podaj ilość rund \n'))
        while 1:
            try:
                self.i = int(input('Podaj ilość rund \n'))
                break
            except ValueError:
                print("Uch! to nie jest liczba! Spróbuj jeszcze raz...")

        for x in range (self.i):
            self.tablica1.append(x)

            while 1:
                try:
                    self.liczba = int(input("Wprowadz liczbe 1 reszka 2 orzel \n"))
                    if(self.liczba > 0 and self.liczba <=2):
                        break
                    else:
                        print('Podałeś złą liczbę poprawny wybór to 1 lub 2')

                except ValueError:
                    print("Uch! to nie jest poprawna liczba! Spróbuj jeszcze raz...")
            self.losowa = random.randint(1, 2)
            self.tablica.append(self.liczba)
            self.tablica2.append(self.losowa)
            if self.liczba == self.losowa:
                self.tablica3.append(self.liczba)

            else:
                continue
class Wyniki(Gra):
    def __init__(self):
        super().__init__()


    def wypisanie_wynikow(self):
        print('Koniec gry prezentacja wyników\n')

        print(self.tablica1.__len__(),'     Ilość przejść w grze ')


        for b in self.tablica:
            print(b, end=' ')

        print(' Wybrana liczba')

        for c in self.tablica2:
            print(c, end=' ')
        print(' Wynik komputera')


    def podsumowanie(self):
        for d in self.tablica3:             #tablica poprawnych wyników
            print(d, end=' ')

        print(self.tablica3.__len__(), '     Trafione wyniki \n')

wyniki = Wyniki()
wyniki.wypisanie_wynikow()
wyniki.podsumowanie()