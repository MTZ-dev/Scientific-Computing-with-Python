#EXERCISE 4.1

#a)

p = (-0.5,0.5)

test_p_in_circle = lambda x: x[0]*x[0] + x[1]*x[1] <= 1
print(test_p_in_circle(p))

#b)

p_coord_positive = lambda x: (x[0] > 0) and (x[1] > 0)
print(p_coord_positive(p))

#c)

list_of_points = [(1,2), (-2,1), (0,0), (3,-2), (4,-2)]
list_of_points.sort(key=lambda t: (-t[1], t[0]))
print(list_of_points)

#d

list_of_points.sort(key=lambda t: abs(t[0]) + abs(t[1]))
print(list_of_points)


#EXERCISE 4.2

import time

print("\n")

#iterative

def reverse_range_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -=1

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start_time = time.time()
reverse_range_iter(L, 3, 6)
end_time = time.time()
print(f'{L} done iteratively in {end_time - start_time} sec')

print("\n")

#recursive

def reverse_range_recur(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_range_recur(L, left + 1, right - 1)
    else:
        return 1


L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start_time = time.time()
reverse_range_recur(L, 3, 6)
end_time = time.time()
print(f'{L} done recursively in {end_time - start_time} sec')

#EXERCISE 4.3

#a)

print("\n")

def iter_even():
    n = 0
    while True:
        yield n
        n += 2

for i in iter_even():
    print(i)
    if i > 20:
        break

#b)

print("\n")

def iter_odd():
    n = 1
    while True:
        yield n
        n += 2

for i in iter_odd():
    print(i)
    if i > 20:
        break

#c)

print("\n")

def iter_power(k):
    n = 1
    while True:
        yield n
        n *= k

for i in iter_power(2):
    print(i)
    if i > 1024:
        break