squares=[]

i=1
n=int(input("Enter the number upto which you want squares"))

while i <=n:
    squares.append(i**2)
    i=i+1

print(squares)