#EXERCISE 2.1

import random as rand

i = rand.randint(10 ** 30, 10 ** 35)
counter = 0

for character in str(i):
    if character == "0":
        counter += 1

print("EXERCISE 2.1\n")

print("Solution 1:")
print(f"Random integer generated: {i} has {counter} zeros!\n")

#alternative solution using build-in-function
print("Solution 2:")
print(f"Random integer generated: {i} has {str(i).count('0')} zeros!\n")


#EXERCISE 2.2

print("EXERCISE 2.2\n")
print('''x = 5                             ---> x == 5 is True and x == 4 is False
x == 5 and 3             # 3      ---> When the first entry of an "and" statement is true the expresion is evaluated to the last value
x == 4 and 3             # False  ---> When the first entry of an "and" statement is false the expresion is false and the second entry is ommited (short-circuit evaluation)
3 and x == 5             # True   ---> 3 is considered as True, so expresion evaluates to x == 5 which is boolean True 
3 and x == 4             # False  ---> 3 is considered as True, so expresion evaluates to x == 4 which is boolean False

isinstance(True, int)    # True   ---> The isinstance() function returns True if the specified object is of the specified type, otherwise False
isinstance(True, bool)   # True   ---> It menas that True can be reagrded both as integer and boolean type
                                       ('bool' class is inherited from 'int' with True beeing 1 and False behaving like 0)\n''')
      
#EXERCISE 2.3

print("EXERCISE 2.3\n")

result = sum(x * x for x in range(2022))

print(f"The sum 1*1 + 3*3 + 5*5 + ... + 2021*2021 is {result}")


#EXERCISE 2.4

print("EXERCISE 2.4 a)\n")

my_name = "Mikołaj"
unicode_list = [ord(character) for character in my_name]

print(f"\"{my_name}\" ---> {unicode_list}\n")


print("EXERCISE 2.4 b)\n")

#from prettytable import PrettyTable

pt = [(1,	"Hydrogen",	"H",	1),(2,	"Helium",	"He",	4),(3,	"Lithium",	"Li",	7),(4,	"Beryllium", "Be",	9),
      (5,	"Boron",	"B",	11),(6,	"Carbon",	"C",	12),(7,	"Nitrogen",	"N",	14),(8,	"Oxygen",	"O",	16),
      (9,	"Fluorine",	"F",	19),(10,	"Neon",	"Ne",	20)]

header = [('No.', 'Name (en)', 'Symbol', 'Weight (u)')]

for row in header:
    print('| {:>3} | {:<20} | {:^6} | {:>10} |'.format(*row))

for row in pt:
    print('| {:>3} | {:<20} | {:^6} | {:>10} |'.format(*row))

print('\n')

#EXERCISE 2.5

print("EXERCISE 2.5)\n")

random_text = '''Far quitting dwelling graceful the likewise received building. An fact
so to that show am shed sold cold. Unaffected remarkably get yet introduced excellence
terminated led. Result either design saw she esteem and. On ashamed no inhabit ferrars it 
ye besides resolve. Own judgment directly few trifling. Elderly as pursuit at regular do parlors. Rank what has into fond she.'''

S = random_text
black_char = 0

for character in S:
    if not S.isspace():
        black_char += 1

print(f"A random string S is: {S}\n")

print(f"Number of black characters: {black_char}\n")

words = S.split()

print(f"Number of words: {len(words)}\n")

print(f"The longest word in S is: {max(words, key=len)}\n")

words.sort()
print(f"Words sorted according to the lexicographic order: {words}\n")

words.sort(key=len)
print(f"Words sorted according to the length: {words}\n")


#EXERCISE 2.6

# Find and explain the results.

print('''t = (2, 4)  ---> assignment of a value to a tuple 
print(t[2]) ---> IndexError: tuple index out of range (there are only 2 elements with index 0 and 1)
t.append(6) ---> AttributeError: 'tuple' object has no attribute 'append' (tuples in Python are immutable in contrast to lists)
a, b = t ; print(a, b) --->  Initialization of a tuple with iterable object (here another tuple) then prints 2, 4''')
      

#EXERCISE 2.7

D = {}
D['I'] = 1 ; D['IV'] = 4 ; D['V'] = 5 ; D['IX'] = 9 ; D['X'] = 10 ; D['XL'] = 40 ; D['L'] = 50 ; D['XC'] = 90 ; \
D['C'] = 100 ; D['CD'] = 400 ; D['D'] = 500 ; D['CM'] = 900 ; D['M'] = 1000

print(f"Method I: {D}")

D = {'I' : 1, 'IV' : 4, 'V' : 5, 'IX' : 9, 'X' : 10, 'XL' : 40, 'L' : 50, 'XC' : 90, 'C' : 100, 'CD' : 400, 'D' : 500, \
      'CM' : 900, 'M' : 1000}

print(f"Method II: {D}")

D = dict([('I', 1), ("IV", 4), ("V", 5), ('IX', 9), ("X", 10), ("XL", 40), ('L', 50), ("XC", 90), ("C", 100), ('CD', 400), \
           ("D", 500), ("CM", 900), ('M', 1000)])

print(f"Method III: {D}")

D = dict(zip(['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M'], [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, \
                                                                                       900, 1000]))

print(f"Method IV: {D}")





















