
first = input("Enter your first name: ")
last = input("Enter your last name: ")
age = int(input("Enter your age: "))

print("first name: "+first)
print("last name: "+last)
print("full name: "+first+" "+last)
print("age: ",age)

if age<18:
    print("you are not allowed")
else:
    print("you are allowed")

