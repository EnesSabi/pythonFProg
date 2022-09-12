import math

K0 = 1000.00
n = 5
p = -2.0
Kn = K0 * math.pow(1 + p/100, n)

print("K0 = ", K0, ", n = ", n, ", p = ", p, "folgt K", n, " = ", Kn)