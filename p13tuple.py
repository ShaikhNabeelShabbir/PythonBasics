#tuple immutable

t=(5,1,7,9,3)
print(t)

print(t[0])
print(t[2:])
print(t[:3])

u=(500,100,700,900,300)+t[:2]
print(u)

v=(t,u)
print(v)

cars=["BMW","Ford","Audi","Fujitsu","Honda"]
z=(t,cars)
print(z)

z[1][3]="Fiat"
print(z)