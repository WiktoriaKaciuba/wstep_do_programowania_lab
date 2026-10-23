from random import randint
#--------------------------------------------------------------------------ZAD1A
x=1+2 #operator + pozwala na dodanie dwóch liczb 
print(type(x)) #jest to typ INT
x=1+4.5
print(type(x)) #jest to typ float ponieważ 1 jest INT'em, a 4.5 jest FLOAT'em, gdyż zawiera wartość po przecinku 
x=3/2 #operator / pozwala na podzielenie liczb
print(type(x)) #jest to typ FLOAT ponieważ wynik dzielenia może posiadać wartości po przecinku
x= 4/2
print(type(x))
x=3 // 2  #operator // pozwala na dzielenie całkowite
print(type(x)) #jest to typ INT, ponieważ wykonywane jest dzielenie całkowite, a więc nie będą wystepować wartości zmiennoprzecinkowe
x= -3//2
print(type(x))
x=11%2 #operator % pozwala na dzielenie z resztą
print(type(x)) #jest to typ INT, ponieważ wynikiem działania operatora % jest reszta
x=2**10 #operator ** pozwala na potęgowanie
print(type(x)) #jest to typ INT, ponieważ liczbą potęgowaną jest 2, a potegą jest liczba 10
x=8**(1/3)
print(type(x)) #jest to typ FLOAT, ponieważ potęgą jest liczba 1/3, a liczbą potęgowaną 8, więc wynik jest po przecinku
#--------------------------------------------------------------------------ZAD1B
print(int(3.0)) #wynikiem tej funkcji jest 3 ponieważ funkcja INT zamienia 3.0 na wartość całkowitą
print(float(3)) #wynikiem tej funkcji jest 3.0, ponieważ funkcja FLOAT zamienia 3 na wartość zmiennoprzecinkową
print(float("3")) #wynikiem tej funkcji jest 3.0, ponieważ funkcja FLOAT zamienia STR 3 na wartość zmiennoprzecinkową
print(type(str(12.4))) #wynikiem tej funkcji jest 12.4, ale w STR, a nie INT, ponieważ funkcja STR zamienia wartość liczbową na tekstową
print(bool(0)) #wynikiem tej funkcji jest False, ponieważ w funkcji tej 0 oznacza fałsz, a 1 prawdę
#--------------------------------------------------------------------------ZAD2
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)
#--------------------------------------------------------------------------ZAD3
imie = 'Jan'
wiek = 20
wzrost = 178
print("Nazywam się " + imie + " i mam " +str(wiek)+ " lat.")
print("Mój wzrost to "+ str(wzrost) + " cm.")
#--------------------------------------------------------------------------ZAD4
cena = 39.99 
rabat = 0.2
cena_rabat = cena*rabat
cena_koncowa = cena-cena_rabat
print(round(cena_koncowa,2))
#--------------------------------------------------------------------------ZAD5
dlugosc1 = int(input("Wpisz długość 1 boku: "))
dlugosc2 = int(input("Wpisz długość 2 boku: "))
pole = dlugosc1*dlugosc2
obwod = (2*dlugosc1) + (2*dlugosc2)
print("Pole prostokąta wynosi: " + str(pole) + ". Obwód prostokąta wynosi: " + str(obwod) + ".")
#--------------------------------------------------------------------------ZAD6
droga = float(input("Podaj droge pokonaną przez samochód: "))
spalanie = float(input("Podaj średnie spalanie: "))
cena_paliwa = 6.5
zuzycie_paliwa = droga/spalanie
koszty = zuzycie_paliwa*cena_paliwa
print("Zużycie paliwa wynosi: " + str(round(zuzycie_paliwa,2)) + " l. Koszt przejazdu wynosi: " + str(round(koszty,2)) + "zł.")
#--------------------------------------------------------------------------ZAD6A
droga = randint(0,100)
spalanie = float(input("Podaj średnie spalanie: "))
cena_paliwa = float(input("Podaj aktualną cenę spalania za litr: "))
zuzycie_paliwa = droga/spalanie
koszty = zuzycie_paliwa*cena_paliwa
print("Zużycie paliwa za " + str(droga) + " km wynosi: " + str(round(zuzycie_paliwa,2)) + "l. Koszt przejazdu wynosi: " + str(round(koszty,2)) + "zł.")
#--------------------------------------------------------------------------ZAD6B
droga = randint(0,100)
spalanie = float(input("Podaj średnie spalanie: "))
cena_paliwa = float(input("Podaj aktualną cenę spalania za litr: "))
zuzycie_paliwa = droga/spalanie
koszty = zuzycie_paliwa*cena_paliwa
print(f"Zużycie paliwa za {droga} km wynosi: {round(zuzycie_paliwa,2)}l. Koszt przejazdu wynosi {round(koszty,2)} zł")
#--------------------------------------------------------------------------ZAD7
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))

if a!= 0:
    x = -b/a
    print("Równanie ma jedno rozwiązanie: x= " +str(x))
elif b==0:
    print("Równanie ma nieskończenie wiele rozwiązań.")
else:
    print("Równanie jest sprzeczne.")
#--------------------------------------------------------------------------ZAD8
kw_a=float(input("Podaj liczbę a: "))
kw_b=float(input("Podaj liczbę b: "))
kw_c=float(input("Podaj liczbę c: "))
delta = (kw_b**2) - 4*kw_a*kw_c
if delta > 0:
    print("Równanie ma 2 lub więcej rozwiązania.")
elif delta ==0:
    print("Równanie ma tylko 1 rozwiązanie.")
else:
    print("Równanie sprzeczne.") 

#--------------------------------------------------------------------------ZAD9
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
dzialanie = input("Wybierz działanie(+,-,*,:,^): ").lower()

if dzialanie == "+" or dzialanie == "dodawanie":
    suma = liczba1+liczba2
    print(str(suma))
elif dzialanie == "-" or dzialanie =="odejmowanie":
    suma = liczba1-liczba2
    print(str(suma))
elif dzialanie == "*" or dzialanie == "mnozenie":
    suma = liczba1*liczba2
    print(str(suma))
elif dzialanie == ":" or dzialanie == "dzielenie":
    if liczba2 ==0:
        print("Nie można dzielić przez 0")
    else:
        suma = liczba1/liczba2
        print(str(suma))
elif dzialanie == "^" or dzialanie == "potegowanie":
    suma = liczba1**liczba2
    print(str(suma))
else:
    print("NIEPOPRAWNE DZIAŁANIE")