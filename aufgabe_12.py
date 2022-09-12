import math

def umfangKreis(radius):
    u = 2*radius*math.pi
    return u
def flaecheKreis(radiusListe):
    liste = []
    for r in radiusListe:
        a = math.pi*r**2
        liste.append(a)
    return liste
def summeUmfangKreis(radiusListe):
    summe = 0
    for r in radiusListe:
        q = umfangKreis(r)
        summe += q
    return summe
def summeFlaecheKreis(radiusListe):
    summe = 0
    l = flaecheKreis(radiusListe)
    for i in l:
        summe += i
    return summe

test:list[int] = [2,3,5,7,11]
test1:int = 13

def main():
    print(umfangKreis(test1))
    print(flaecheKreis(test))
    print(summeUmfangKreis(test))
    print(summeFlaecheKreis(test))

if __name__ == "__main__":
    main()