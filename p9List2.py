#mutable list with hetrogenous data
person=["Nabeel",10,False,True,"Khan"]

for p in person:
    print(p)
    if p=="Khan":
        person[4]="Shaikh"
        print(person)