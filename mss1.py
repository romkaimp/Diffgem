from math import cos, pi, sin
from sympy import diff, symbols, cos, sin, exp, sqrt, limit, Matrix, det, simplify
from matplotlib import pyplot as plt

r, theta, phi = symbols("r theta phi")

X = [r, theta, phi]
x = [r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta)]

Q = [[diff(x[i], X[j]) for i in range(3)] for j in range(3)]
print(Q)