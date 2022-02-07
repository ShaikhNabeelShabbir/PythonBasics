#dictionary
names={1:"Nabeel", 2:"Osaid", 3:"Faizan", 4:"Afzal"}
print(names)

names[1]="Yasser"
names[5]="Nabeel"

print(names)

del names[1]

print(names)

for k,v in names.items():
    print(k,v)

