import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
import argparse


a = open('data.txt')

X = a.readline().split()
X = [float(x) for x in X]

Y = a.readline().split()
Y = [float(y) for y in Y]

parser = argparse.ArgumentParser()
parser.add_argument('x', metavar='x', type=float, nargs='+',
                    help='input number')


print(X)
print(Y)
a.close()
print("Введите число:")
x = float(input("\tx = "))
i = 0
F = []#пустые массивы


while i != len(X) - 1:
    f = Y[i]+(Y[i+1]-Y[i])/(X[i+1]-X[i])*(x-X[i])
    i = i + 1
    F.append(round(f,2))


n = 0
i = 0

while i != len(F) - 1:
    if F[i] == F[i + 1]:
        n = 1
    else:
        n = 0
    i = i + 1


if n == 1:
    print(" y = %.2f" % (F[0]))
else:
    print("Shos ne to")


m = interpolate.interp1d(X, Y)


plt.plot(X, Y, 'o', x, F[0], '-')
plt.show()

args = parser.parse_args()
answer = args[(input("\tx = "))]
print (args)
x = args.x
print (" otvet = %.2f" % (F[0]))



parser = argparse.ArgumentParser()
parser.add_argument("-f", type=argparse.FileType())
args = parser.parse_args(["-f", "data.txt"])


