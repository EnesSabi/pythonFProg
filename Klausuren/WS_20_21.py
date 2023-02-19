# Klausur aus dem Wintersemester 20/21
## Aufgabe 1) Datentypen und Variable
a = 9 // 2 / 2 
b = (~3 + 1) << 2
c = [k % 2 for k in range(5)]
d = [a + a for a in "abc"]
#Loesung
t = "type = "
v = ", value = "
print(t, type(a) , v , a)
print(t, type(b) , v , b)
print(t, type(c) , v , c)
print(t, type(d) , v , d)

## Aufgabe 2) Listen und Tupel
# Gegeben sei eine Liste q mit Zahlen. Erstellen Sie eine neue Liste, die nur diejenigen Elemente aus q enthält, die sowohl gerade Zahlen sind als auch an einer geraden Position (Index) in der Liste stehen
q = [1,3,5,8,10,13,18,36,78]
# Lösung -> [10,18,78]
q1 = [q[i] for i in range(len(q)) if i % 2 == 0 and q[i] % 2 == 0]
print(q1)

## Aufgabe 3)
# Schreiben Sie einen Lambda-Ausdruck, der eine Funktion mit Parameter n darstellt, deren Rückgabewert eine Liste aller Vielfachen von 3 zwischen 1 und n ist. Damit soll folgende Ausgabe erzeugt werden

z = list(map(lambda i: [x for x in range(i) if x % 3 == 0], [13, 7]))
print(z)

## Aufgabe 4) Klassen und dynamische Datenstrukturen
#Es soll eine Python-Klasse implementiert werden, die einen Stack repräsentiert. Diese soll
#über folgende Inhalte verfügen:
#a) Ein privates Attribut vom Typ list, das die Inhalte des Stacks verwaltet
#b) Ein Konstruktor zur Initialisierung mit einer leeren Liste
#c) Eine Methode push(), um einen Eintrag in den Stack einzufügen
#d) Eine Methode pop(), die den letzten Eintrag wieder ausgibt und ihn aus der Liste
#löscht (mit dem Befehl del)
#e) Eine Methode empty(), die prüft, ob Elemente im Stack vorhanden sind

class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, item):
        self.__stack.append(item)
    def pop(self):
        if not self.empty():
            return self.__stack.pop()
        else:
            print("Stack is empty")
            return None
    def empty(self):
        return len(self.__stack) == 0

wort = input("Wort: ")
stapel = Stack()
for zeichen in wort:
    stapel.push(zeichen)
while not stapel.empty():
    print(stapel.pop(), end= " ")