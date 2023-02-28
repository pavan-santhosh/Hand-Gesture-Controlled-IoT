import tabulate
x = 0
y = 0
f = 1/(1+x+y)
upper_limit_x = 2.8
lower_limit_x = 2
upper_limit_y = 1.4
lower_limit_y = 1
interval = 4
H = (upper_limit_x-lower_limit_x)/interval
K = (upper_limit_y-lower_limit_y)/interval
L = []
while lower_limit_y <= (upper_limit_y+0.1):
    l = []
    l.append(lower_limit_y)
    while lower_limit_x <= (upper_limit_x+0.2):
        f = 1/(1+lower_limit_x+lower_limit_y)
        l.append(f)
        lower_limit_x += 0.2
    L.append(l)
    lower_limit_x = 2
    lower_limit_y += 0.1
L.insert(0, ["X(right)/Y(down)", 2.0, 2.2, 2.4, 2.6, 2.8])
L[3][0] = 1.2
L[4][0] = 1.3
L[5][0] = 1.4
table = tabulate.tabulate(L)
print("The matrix of f(x,y) is:", table)
a, b, B, c = 0, 0, 0, 0
A = (L[1][1])+(L[1][5])+(L[5][1])+(L[5][5])
for i in range(1, len(L)):
    t = L[i]
    if i == 1 or i == len(L)-1:
        B = 0
        A = ((t[1])+(t[len(t)-1]))
        for y in range(2, len(t)-1):
            B += t[y]
        a += A
        b += B
    else:
        b = b+(t[1]+(t[len(t)-1]))
        for e in range(2, len(t)-1):
            c += t[e]
print("The value of A is", a)
print("The value of B is", b)
print("The value of C is", c)
M = (H*K)/4
print("The value of the given integral is given by the equation:")
print("(hk/4)x[A+2B+4C]")
Answer = (M*(a+(2*b)+(4*c)))
print("The solution for the given integral, solved by Trapezoidal rule is", Answer)
