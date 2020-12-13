n=int(input("Введіть ціле значення n: "))
a = [0,9,9]
i=1

while i<=n:
    el = a[i-1]+a[i-2]+ a[i-3]
    a.append(el)
    i+=1


print("Весь список:{0}".format(a))
print("xn={0}".format(el))
