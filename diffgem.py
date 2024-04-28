from math import cos, pi, sin
from sympy import diff, symbols, cos, sin, exp, sqrt, limit, Matrix, det, simplify
from matplotlib import pyplot as plt


eps = 1
g = symbols("g")#вместо кси - g

x = (1/2)*exp(g)            #МЕНЯТЬ ТОЛЬКО eps, x, y, z
y = g
z = -exp(-g)

#s'
s = sqrt(diff(x, g)*diff(x, g)+diff(y, g)*diff(y, g)+diff(z, g)*diff(z, g))
print("s:", s)
xx = []#списки производных i-го порядка x', x'', x'''
yy = []
zz = []


for i in range(3):
    x = diff(x, g)/s #дифференцируем по кси, потом делим на s (то есть на s')
    #xx.append(simplify(x))
    xx.append(x)

    print("x:", x, "=", limit(x, g, 1).__float__())
    y = diff(y, g)/s
    #yy.append(simplify(y))
    yy.append(y)

    print("y:", y, "=", limit(y, g, 1).__float__())
    z = diff(z, g)/s
    #zz.append(simplify(z))
    zz.append(z)
    print("z:", z, "=", limit(z, g, 1).__float__(), "\n")

k = limit(sqrt(xx[1]*xx[1]+yy[1]*yy[1]+zz[1]*zz[1]), g, 1)
print("k:", simplify(k), "=", float(k), "\nрадиус:", 1/float(k))
M = Matrix(3, 3, [xx[0], yy[0], zz[0], xx[1], yy[1], zz[1], xx[2], yy[2], zz[2],])
print(simplify(M.det()))
print("кручение:", limit(M.det()/k/k, g, 1).__float__())