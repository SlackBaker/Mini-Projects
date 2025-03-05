import math

def solve_quadratic(a,b,c):
    D = (b**2) - (4*a*c)
    if D > 0:
        x1 = (-b+math.sqrt(D)/2*a)
        x2 = (-b-math.sqrt(D)/2*a)
        print("x1 = ", x1, " x2 = ", x2)
    else:
        print("error")