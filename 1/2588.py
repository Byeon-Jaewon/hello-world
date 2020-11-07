a = input()
b = input()

a= int(a)
b= int(b)

first= a*(b%10)
second = int(a*((b%100)-(b%10))/10)
third = int(a*(b-(b%100))/100)

print(first)
print(second)
print(third)
print(third*100+second*10+first)
