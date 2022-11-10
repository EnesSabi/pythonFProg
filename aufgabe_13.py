import math

def code_erklaerung():
    x = ['ab', 'cd']
    return list(map(list, x))

def lambda_ausdruck1():
    floatwerte = [3.14, 4.20, 0.69, 1.23, 3.14, 6.27, 6.66]
    z = list(map(lambda b: b * 180 / math.pi, list(filter(lambda x: True if (x > 0 and x < 2*math.pi) else False, floatwerte))))
    return z

def lambda_ausdruck2(): #unfertig
    q = [1, 3, 5, 8, 10, 13, 18, 36, 36, 78]
    z = list(set(map(lambda x: q[::3] == x, q)))
    return z

def lambda_ausdruck3(): #unfertig
    q = [13,7,2]
    z = list(map(lambda x: x in range(q), q))
    return z

def main():
    print(code_erklaerung())
    print(lambda_ausdruck1())
    print(lambda_ausdruck2())
    print(lambda_ausdruck3())

if __name__ == "__main__":
    main()