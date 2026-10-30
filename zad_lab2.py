#------------------------------------------------------ZAD1
liczbaP = int(input("Podaj liczbę punktów: "))
if liczbaP >=80: #sprawdza czy liczba jest większa bądź równa 80
    print("Egzamin został zaliczony w terminie 0")
elif liczbaP > 50 and liczbaP <80: #sprawdza czy liczba jest pomiędzy 50, a 80
    print("Egzamin został zaliczony, istnieje możliwośc poprawy wyniku")
else:
    print("Egzamin został nie zaliczony")
#------------------------------------------------------ZAD2
x = float(input("Podaj liczbę x: "))
y = float(input("Podaj liczbę y: "))
z = float(input("Podaj liczbę z: "))

if x >y:
    x,y = y,x #sprawdza czy x jest większy od y, jeśli tak zmienia kolejność
if x>z: 
    x,z=z,x  #sprawdza czy x jest większy od z, jeśli tak zmienia kolejność
if y>z: #sprawdza czy z jest większy od y, jeśli tak zmienia kolejność
    y,z=z,y

print(f"Liczby w kolejności {x},{y},{z}")


#------------------------------------------------------ZAD3
nazwa_pliku = 'Raport_maj.xlsx'
rozszerzenie = nazwa_pliku.endswith(".xlsx") #sprawdza czy końcówką pliku jest .xlsx
if rozszerzenie == True:    #jeśli tak to drukuje wiadomoś ć
    print("Jest to plik excela") 
else: #jeśli nie jest to drukuje to drukuje wiadomość
    print("Nie jest to plik excela") 

#------------------------------------------------------ZAD4
gol = int(input("Wprowadź liczbę zdobytych bramek: "))
gol_pkt = 10*gol #punkty naliczane za każdego gola
bonus=0

if gol >10: #punkty bonusowe zależnie od liczby bramek
    bonus = 10
    wynik = gol_pkt + bonus    
    print(f"Drużyna zdobywa {bonus} punktów bonusowych i {wynik} punktów całościowo")
elif gol >5:
    bonus = 5
    wynik = gol_pkt + bonus
    print(f"Drużyna zdobywa {bonus} punktów bonusowych i {wynik} punktów bonusowych")

#------------------------------------------------------ZAD4A
gol = int(input("Wprowadź liczbę zdobytych bramek: "))
gol_pkt = 10*gol  
bonus=0

if gol>=5:
    bonus = 5
    wynik = gol_pkt + bonus
    print(f"Drużyna zdobwywa {bonus} punktów bonusowych i {wynik} punktów całościowo")
    if gol >10:
        wynik = gol_pkt + bonus
        bonus = 15
        print(f"Drużyna zdobwywa {bonus} punktów bonusowych i {wynik} punktów całościowo")
else:
    print("Drużyna zdobywa 0 punktów bonusowych")
    
#------------------------------------------------------ZAD4B
gol = int(input("Wprowadź liczbę zdobytych bramek: "))
gol_pkt = 10*gol
bonus=0

def gole(): #stworzenie funkcji, która pozwala na wykonanie zadania
    if gol>=5:
        global bonus #ustawienie zmiennej bonus na globalną, co pozwala na wykorzystanie jej poza funkcją
        bonus = 5
        wynik = gol_pkt + bonus
        if  gol >10:
            bonus += 10  #dodanie punktów do zmiennej bonus
            wynik = gol_pkt + bonus
            print(f"Drużyna zdobwywa {bonus} punktów bonusowych i {wynik} punktów całościowo")
        else:
            print(f"Drużyna zdobwywa {bonus} punktów bonusowych i {wynik} punktów całościowo")
    else:
        print("Drużyna zdobywa 0 punktów bonusowych")

gole() #wywołanie funkcji


#------------------------------------------------------ZAD5A
with open("notowania_gieldowe.txt","r") as plik: #wczytywanie plkiku po linii
    for i in plik:
        print(i,end='')
#------------------------------------------------------ZAD5B
with open("notowania_gieldowe.txt","a") as plik: #dopisywanie do końca pliku
    plik.write("\nALR, 113")
with open("notowania_gieldowe.txt","r") as plik:
    for i in plik:
        print(i,end='')

#------------------------------------------------------ZAD6
litera = input("Podaj litere: ")
if litera.isalpha() and len(litera) ==1: #sprawdzenie czy zmienna jest liczbą oraz czy jej długość równa jest 1
    if litera.upper():
        print(f"Litera {litera} jest duża")
    else:
        print(f"Litera {litera} jest mała")
else: 
    print("Wprowadzony znak nie jest literą")

#------------------------------------------------------ZAD8
text = 'Studiuję-Informatyke'
print("Trzy pierwsze znaki w tekście " + text[:3])   #wyświetla 3 pierwsze znaki w tekście
print("Dwa ostatnie znaki w tekście" + text[-2:])    #wyświetla 2 ostatnie znaki w tekście

#------------------------------------------------------ZAD9
tekst = (input("Wpisz tekst: "))
zmiana = tekst.swapcase() #zmiana wielkości liter w tekście wpisanym przez użytkownika
print(zmiana)
