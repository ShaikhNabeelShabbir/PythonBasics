class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
        print("I am a constructor")

    def display(self):
        print("I am a method\n",self.name,self.age)

nabeel = Person("Nabeel",19)
nabeel.display()