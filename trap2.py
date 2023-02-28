from math import exp
import tabulate
x = 0
y = 0
f = pow((x+y), 0.5)
upper_limit_x = 1
lower_limit_x = 0
upper_limit_y = 2
lower_limit_y = 1
interval = 4
H = (upper_limit_x-lower_limit_x)/interval
K = (upper_limit_y-lower_limit_y)/interval
L = []
while lower_limit_y <= (upper_limit_y):
    l = []
    l.append(lower_limit_y)
    while lower_limit_x <= (upper_limit_x):
        f = pow((lower_limit_x+lower_limit_y), 0.5)
        l.append(f)
        lower_limit_x += 0.25
    L.append(l)
    lower_limit_y += 0.25
    lower_limit_x = 0
L.insert(0, ["X(right)/Y(down)", 0, 0.25, 0.5, 0.75, 1])

matrix_sum = 0
C = 0

for i in range(1, len(L)):
    for j in range(1, len(L)):
        matrix_sum += L[i][j]
        if i in [2,3,4] and j in [2,3,4]:
            C += L[i][j]
A = L[1][1] + L[1][5] + L[5][1] + L[5][5]

B = matrix_sum - C - A

table = tabulate.tabulate(L)
M = (H*K)/4
result = (M*(A+(2*B)+(4*C)))
print("Matrix of f(x,y):")
print(table)
print("A = ", A)
print("B = ", B)
print("C = ", C)

print("The value of the given integral is given by the equation:")
print("(hk/4)x[A+2B+4C]")

print("Integral formulated by Trapezoidal Rule: ", result)