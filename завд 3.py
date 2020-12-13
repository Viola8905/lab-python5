x = float(input("x="))
e = float(input("e="))
import math
z=1
s=x
n=2
while math.fabs (z/math.factorial(2*n-1))>e:
    s=s+(z/math.factorial(2*n-1))
    n+=1
    z=z*(-(x**(2*n-1)))
print(s)
