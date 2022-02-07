# demonstrate a project to show a scattered graph
import matplotlib.pyplot as plt
import random
years = [1901, 1911, 1921, 1931, 1941, 1951,
         1961, 1971, 1981, 1991, 2001]
populations = []

# for y in years:
#     data = int(input(f"Enter the population in {y} "))
#     populations.append(data)
for y in years:
    data = random.randint(100000, 1000000)
    populations.append(data)

plt.scatter(years, populations, color='red')

plt.xlabel("years")
plt.ylabel("population")

plt.show()
