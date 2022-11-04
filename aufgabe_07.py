from datetime import date

def inp():
    print("Bitte Jahr eingeben")
    j = int(input())
    print("Bitte Monat eingeben")
    m = int(input())
    print("Bitte Tag eingeben")
    t = int(input())
    r = int(1)
    return date(j, m, t), date(j, r, r)

def main():
    datum = inp()
    diff = datum[0] - datum[1]
    print(diff.days + 1)

if __name__ == "__main__":
    main()