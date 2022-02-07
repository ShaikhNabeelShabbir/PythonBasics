print("Enter the marks of p,c,m")

p=int(input("Enter the marks of p\t"))
c=int(input("Enter the marks of c\t"))
m=int(input("Enter the marks of m\t"))

avg=(p+c+m)/3
print("Average",avg)

if avg>=75:
    print("A grade")
elif avg>=60:
    print("B grade")
elif avg>=45:
    print("C grade")
elif avg>=35:
    print("D grade")
else:
    print("Fail")



