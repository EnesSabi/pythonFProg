
from datetime import date
from re import M


def christoph_zeller():
    t = 31  #zwischen 1 und 31
    m = 14  #zwischen 3 und 14
    j = 20  #zwischen 0 und 99 für 2022
    h = 22  #zwischen 0 und 99 für 2022

test1 = date(2000,3,1)
test2 = date(2012,3,1)
test3 = date(1999,9,8)

def rechnen(t:int,m:int,j:int,h:int):
    #d = division
    d1 = int(((m+1)*26)/10)
    d2 = int((5*j)/4)
    d3 = int(h/4)
    return int((t+d1+d2+d3-(2*h)-1)%7)

def ausgabe(x):
    match x:
        case 0: 
            return "Sonntag"
        case 1:
            return "Montag"
        case 2:
            return "Dienstag"
        case 3:
            return "Mittwoch"
        case 4:
            return "Donnerstag"
        case 5:
            return "Freitag"
        case 6:
            return "Samstag"
        case _:
            return "Wochentag nicht gefunden!"


def main():
    t = test3.day
    m = test3.month
    j = int(test3.year%100)
    if j == 1:
        j = 13
    if j == 2:
        j = 14
    h = int(test3.year/100)
    print(t,m,j,h)
    w = rechnen(t,m,j,h)
    print(ausgabe(w))


if __name__ == "__main__":
    main()