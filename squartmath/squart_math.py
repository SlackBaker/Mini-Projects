import math

def solve_quadratic(a,b,c):
    D = (b**2) - (4*a*c)
    if D > 0:
        x1 = (-b+math.sqrt(D)/2*a)
        x2 = (-b-math.sqrt(D)/2*a)
        print("x1 = ", x1, " x2 = ", x2)
    else:
        print("error")

def viet_quadratic(x1,x2):
    p = -1*(x1+x2)
    q = x1*x2
    print('p = ', p)
    print('q = ', q)

