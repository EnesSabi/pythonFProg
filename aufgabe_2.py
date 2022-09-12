def celcius_to_fahrenheit(a:int):
    return int(a*9/5+32)

def fahrenheit_to_celcius(a:int):
    return int(5/9*(a-32))

def main():
    print("celcius_to_fahrenheit -> 0 or fahrenheit_to_celcius -> 1")
    x:int = int(input())
    if x == 0:
        print("Wie viel Grad Celsius")
        a = int(input())
        print(celcius_to_fahrenheit(a))
    elif x == 1:
        print("Wie viel Grad Fahrenheit")
        a = int(input())
        print(fahrenheit_to_celcius(a))
    else:
        print("bitte korrekte Zahl eingeben")
        main()

if __name__ == "__main__":
    main()