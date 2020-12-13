import math
n=int(input("Введіть ціле значення n: "))
b=float(input("Введіть b "))
a = [4]
for i in range (1,n+1):
    el = a[i-1]- math.cos((b**i)/12)
    a.append(el)
  

print("Весь список:{0}".format(a))
print("xn={0}".format(el))
