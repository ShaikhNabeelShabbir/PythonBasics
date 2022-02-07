
cars=["BMW","Ford","Audi","Fujitsu","Honda"]
print(cars)
cars.append("Range Rover")#1
print(cars)
del cars[3]#2
print(cars)
cars.insert(3,"Fujitsu")#3
print(cars)
cars.sort()#4
print(cars)
x = cars.index("Audi")#6
print(x)
del cars[:]#5
print(cars)
cars.clear()#7
print(cars)


