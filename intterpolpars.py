import math

x = [i for i in range(101)]
x.remove(50)
y = [math.sin(i) for i in x]
#
h = []# разность х hk = xk - xk-1
l = []# разность у делим на разность х (lk = (yk - yk-1)/hk)
delta = []#δk-1 = - hk/(2hk-1+2hk+hk-1δk-2), k=3,4, ... N (коефициент)
lmbd = []# (коефициент) (3lk - 3lk-1 - hk-1λk-2)/(2hk-1+2hk+hk-1δk-2)

h.append(1)
# считаем h и l
for i in range(x[1], x[49], 1):
    h.append(x[i] - x[i - 1])
    if (h[i] == 0):
        print("\nError, x[%d]=x[%d]\n", i, i - 1)
    l.append((y[i] - y[i - 1]) / h[i])

delta.append(-h[2] / (2 * (h[1] + h[2])))
lmbd.append(1.5 * (l[2] - l[1]) / (h[1] + h[2]))
#считаем delta и lmbd
for i in range(x[2], x[49], 1):
    delta.append(-h[i] / (2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2]))
    k = (3 * l[i] - 3 * l[i - 1] - h[i - 1] * lmbd[i - 2]) / (2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2])
    lmbd.append(k)
    if (len(delta) == 47): break
# индексы для кубического сплайна
c = [None] * 48
c[0] = 0
c[47] = 0
# метод обратной прогонки
for i in range(47, 1, -1):
    c[i - 1] = delta[i - 1] * c[i] + lmbd[i - 1]

#После нахождения ck нужно найти bk и dk по формулам
d = []
b = []


for i in range(1, 48, 1):
    d.append((c[i] - c[i - 1]) / (3 * h[i]))
    b.append(l[i] + (2 * c[i] * h[i] + h[i] * c[i - 1]) / 3)

print("\nA[k]\tB[k]\tC[k]\tD[k]\n",'коефициенты полинома')
for i in range(1, 47, 1):
    print(y[i], b[i], c[i], d[i])

# как вывод имеем интерполируемую функцию (коефициенты)


#testing
A1 = [i for i in range(20)]
B1 = [math.sin(i) for i in A1]

start = B1[0]
end = B1[-1]
step = (end - start)/20;
s = start
for k in A1:
    # find k, where s in [x_k - 1; x_k]
    for j in A1:
        if (s>=A1[k-1]):
            if (s<=A1[k]): break
    F = B1[k] + b[k] * (s - A1[k]) + c[k] * math.pow(s - A1[k], 2) + d[k] * math.pow(s - A1[k], 3)
    # F - значение функции
    #каждый F это значение на промежутках  х1 х2 х3 х4 х5.
    print (k+1, ". F = ", F)
    s = s + step


