import random

def zufallszahlen():
    x = random.randint(0,100)
    if x < 1:
        zufallszahlen()
    return x

def abfrage():
    print("Welche Nummer habe ich gewählt?")
    t = int(input())
    print(t)
    return t

def main():
    Lösung = zufallszahlen()
    i = 0
    while i < 3:
        x:int = abfrage()
        if Lösung == x:
            return print("Richtig")
        print("falsch")
        if Lösung > x:
            print("Lösung ist größer!")
        if Lösung < x:
            print("Lösung ist kleiner")
        i += 1
        if i == 3:
            print("leider verloren! \nprobiers nochmal")
            print("Lösung war ", Lösung)
            main()


if __name__ == "__main__":
    main()