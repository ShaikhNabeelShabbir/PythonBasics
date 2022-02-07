import matplotlib.pyplot as plt
import numpy as np
rollno = []
marks = []
for i in range(1, 6):
    rollno.append(1)
    m = int(input("Enter marks of student" + str(i) + ": "))
    marks.append(m)

xpoints = np.array(rollno)
ypoints = np.array(marks)

plt.plot(xpoints, ypoints)
plt.show()
