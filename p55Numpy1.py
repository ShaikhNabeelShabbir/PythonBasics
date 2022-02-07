import numpy as np
even = [2, 4, 6, 8, 10]
odd = (1, 3, 5, 7, 9)

arr_even = np.array(even)
arr_odd = np.array(odd)

print(even, type(even))
print(odd, type(odd))

print(arr_even, type(arr_even))
print(arr_odd, type(arr_odd))

print(arr_even.ndim)
print(arr_odd.ndim)

print(arr_even[1])
print(arr_odd[1:3])

print(arr_even[2:])
print(arr_odd[:4])
