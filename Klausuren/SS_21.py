# Klausur aus dem Sommersemester 2021
## Aufgabe 1) Datentypen und Variable
a = 11 // 3 / 2
b = 2e+1j # -> mathematische Schreibweise real+imag(j) und 2e5 -> aex = a*10^x
c = [1,2] + [(3,4)]
d = (3,5,7,9)[::-1]
#Loesung
t = "type = "
v = ", value = "
print(t, type(a) , v , a)
print(t, type(b) , v , b)
print(t, type(c) , v , c)
print(t, type(d) , v , d)

## Aufgabe 2) Listen und Tupel
# a) Definieren Sie eine Liste von Tripel (3er Tupeln), die alle Möglichkeiten darstellt, wie man drei Kugeln mit 1, 2 und 3 beschriftet aus einer Urne ziehen kann.
triplets = [(i, j, k) for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3]]
#Lösung
print(triplets)

# b) Schreiben Sie einen lambda-Ausdruck, der eine zweistellige Funktion (mit zwei Parametern x und y) darstellt, deren Rückgabewert eine Liste aller geraden Zahlen zwischen x und y ist. Damit soll folgende Ausgabe erzeugt werden:

z = list(map(lambda x, y: [i for i in range(x, y+1) if not i % 2], [1,3],[7,9]))
print(z)

#Schreiben Sie eine Python-Klasse Messwert. Diese soll folgende Elemente enthalten:
#a) Eine private Variable wert vom Typ float
#b) Einen allgemeinen Konstruktor, mit dem der Wert mit einem übergebenen Parameter
#initialisiert werden kann
#c) Eine Getter- und eine Setter-Methode für den Wert als Property.
#d) Eine Methode __str__() für Print-Ausgaben.
#e) Ein Testskript, das alle Methoden der Klasse nutzt und mit sinnvollen Werten aufruft

class Messwert:
    def __init__(self, wert):
        self.__wert = wert

    @property
    def wert(self):
        return self.__wert

    @wert.setter
    def wert(self, value):
        self.__wert = value

    def __str__(self):
        return str(self.__wert)

m = Messwert(5.5)
print(m.wert) # 5.5
m.wert = 7.5
print(m.wert) # 7.5
print(str(m)) # 7.5

