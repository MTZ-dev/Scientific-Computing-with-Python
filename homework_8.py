import numpy as np

#EXERCISE 8.1

#a)
array_a = np.arange(0.0, 1.1, 0.1, dtype=np.float32)
print(array_a)
#b)
array_b = np.zeros((5, 6), dtype=np.int8)
print(array_b)
#c)
array_c = np.power(0+1j, np.arange(9)).astype(np.complex64)
print(array_c)

#EXERCISE 8.2

#a)
v1 = np.random.rand(10)
print(v1)
#b)
v2 = np.copy(v1[1::2])
print(v2)
assert not np.may_share_memory(v1, v2) #sprawdzam czy to faktycznie inny objekt czy widok
#c)
v3 = np.copy(v1[::-1])
print(v3)
assert not np.may_share_memory(v1, v3)

#EXERCISE 8.3

#a)
m1 = np.random.rand(4,5)
print(m1)
#b)
m2 = np.copy(np.flip(m1, axis=1)) #sprawdziłem, że bez copy powstawał widok z użyciem flip()
print(m2)
#c)
m3 = np.copy(np.flip(m1, axis=0))
print(m3)
#d)
m4 = np.copy(m1[1:-1, 1:-1])
print(m4)
