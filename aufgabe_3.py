import math

def function(a:float):
    v:float = 4/3*math.pi*math.pow(a,3)
    o:float = 4*math.pi*math.pow(a,2)
    print("Für den Radius ", a, " gilt die Oberfläche ", o, " und das Volumen ", v)

def main():
    print("Bitte gib den Radius ein:")
    x = float(input())
    function(x)

if __name__ == "__main__":
    main()