
from multiprocessing.connection import wait


def einlesen():
    print("numbers for your first tuple")
    print("first value: ")
    x1 = float(input())
    print("second value: ")
    x2 = float(input())
    ersterPunkt = (x1, x2)
    print("your first tuple: ", ersterPunkt)
    print("numbers for your second tuple")
    print("first value: ")
    x3 = float(input())
    print("second value: ")
    x4 = float(input())
    zweiterPunkt = (x3, x4)
    print("your second tuple: ", zweiterPunkt)
    beidePunkte = (ersterPunkt, zweiterPunkt)
    return beidePunkte
    

def rechnen(p1, p2):
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    b = p1[1]-(p1[0]*m)   #(m * p1[0]) + (p2[1] - p2[0] * m)         #(p2[0]*p1[1] - p1[0]*p2[1])/(p2[0]-p1[0])
    print("f(x) = ", m, "x +",b)

def main():
    bP = einlesen()
    rechnen(bP[0], bP[1])

if __name__ == "__main__":
    main()
