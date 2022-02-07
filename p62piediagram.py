# we have in total 100 students 23 scored distinction(75+)
# 17 scored first class(60+)
# 15 scored second class(45+)
# 25 scored pass class(35+) and
# remaining failed(35-)[pie diagram]
import matplotlib.pyplot as plt

data = []
grades = ['DISTINCTION', 'FIRST CLASS',
          'SECOND CLASS', 'PASS CLASS', 'FAIL CLASS']
for g in grades:
    student = int(input(f"Enter the number of students in {g} "))
    data.append(student)

color = ['yellow', 'green', 'red', 'blue', 'maroon']
explode = (0.1, 0.1, 0.1, 0.1, 0.1)

fig = plt.figure(figsize=(10, 10))
plt.pie(data, labels=grades, colors=color,
        explode=explode, startangle=90, shadow=True)

plt.legend(loc='best', title='GRADES')
plt.show()
