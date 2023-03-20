#EXERCISE 3.1

word = "Mikolaj"

for char in word:
    print("+---", end="")
print("+")

print("| " + " | ".join(word) + " |")

for char in word:
    print("+---", end="")
print("+")

#EXERCISE 3.2

n = 0

while n <= 40:
    n += 1
    if n == 13:
        continue
    if n % 5 == 0:
        print("x is divided by 5")
        if n % 7 == 0:
            print("x is divided by 7")
            print("x is divided by 5 and 7")
            continue
        else:
            continue
    if n % 7 == 0:
        print("x is divided by 7")
        continue
    print("x is not important")

print("\n")

for n in range(1,41):
    if n == 13:
        continue
    if n % 5 == 0:
        print("x is divided by 5")
        if n % 7 == 0:
            print("x is divided by 7")
            print("x is divided by 5 and 7")
            continue
        else:
            continue
    if n % 7 == 0:
        print("x is divided by 7")
        continue
    print("x is not important")

print("\n")

#EXERCISE 3.3

import math

n = 2022
x = math.pi
word = "Python"
polish = "książka"

with open("vars.txt", "w") as f:
    for i in (n, f'{x:.5f}', word, polish):
        f.write(f'{i}\n')
        
with open("vars.txt", "r") as f:
    for i in f:
        print(i)