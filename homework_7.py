#EXERCISE 7.1

#kopia mojej klasy z zadania 6 zmodyfikowana o uwagę dotyczącą _x, _y oraz _z

import math


class Vector:
    "Implements a class of 3D vectors (floats as coordinates) along with an interface for their manipulation"

    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        
        self._x = x
        self._y = y
        self._z = z


    @property
    def x(self) -> float:

        return self._x
    

    @x.setter
    def x(self, x_coord) -> None:

        if isinstance(x_coord, float):
            self._x = x_coord
        else:
            raise ValueError("Only floats are accepted as Vector coordinates")


    @property
    def y(self) -> float:

        return self._y
    

    @y.setter
    def y(self, y_coord) -> None:

        if isinstance(y_coord, float):
            self._y = y_coord
        else:
            raise ValueError("Only floats are accepted as Vector coordinates")
        

    @property
    def z(self) -> float:

        return self._z
    

    @z.setter
    def z(self, z_coord) -> None:

        if isinstance(z_coord, float):
            self._z = z_coord
        else:
            raise ValueError("Only floats are accepted as Vector coordinates")


    def __repr__(self) -> str:
        
        return f"Vector({self.x}, {self.y}, {self.z})"
    

    def __eq__(self, other: "Vector") -> bool:
        
        result = self - other
        return not (result.x or result.y or result.z) #true only if all 0
    

    def __ne__(self, other: "Vector") -> bool:

        return not self == other
    

    def __add__(self, other: "Vector") -> "Vector":

        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    

    def __sub__(self, other: "Vector") -> "Vector":

        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    

    def __mul__(self, other: "Vector") -> float:

        return self.x * other.x + self.y * other.y + self.z * other.z
    

    def cross(self, other: "Vector") -> "Vector":

        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    

    def length(self) -> float:

        return math.sqrt(self * self)
    

    def __hash__(self) -> int:
        
        return hash((self.x, self.y, self.z))
    
    #dodana funkcja find_axis(v1, v2) 

    @classmethod
    def find_axis(cls, v1: "Vector", v2: "Vector") -> "Vector":
        cross_product = v1.cross(v2)
        if cross_product == cls(0.0, 0.0, 0.0):
            raise ValueError("Vectors are parallel or zero")
        return cross_product / cross_product.length()
    
    #definiuję metodę dzielenia wektora przez skalar, do wykorzystania w find_axis

    def __truediv__(self, scalar: float) -> "Vector":
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

#testy

try:
    v = Vector(1.0, 2.0, 3.0)
    w = Vector(2.0, -3.0, 2.0)

    print(Vector.find_axis(v,w))

except ValueError:

    print("ValueError is present")

else:

    print("No Exception is present")

finally:

    print("End of test")

#równoległe

try:
    v = Vector(1.0, 2.0, 3.0)
    w = Vector(2.0, 4.0, 6.0)

    print(Vector.find_axis(v,w))

except ValueError:

    print("ValueError is present")

else:

    print("No Exception is present")

finally:

    print("End of test")


#EXERCISE 7.2

#a) wykorzystanie itertools
print("a)")

import itertools

iter_a = itertools.cycle(range(0, 2))

#test za pomocą next()
for i in range(10):
    print(next(iter_a))

#b) wykorzystanie klasy
print("b)")

import random

class Random_Iterator:

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice([0, 1])

iter_b = Random_Iterator()

#wywołanie za pomocą islice z itertools dla testu
for value in itertools.islice(iter_b, 10):
    print(value)

#c) wykorzystanie funkcji generującej
print("c)")

def iterate_0_1_0_neg1():

    values = [0, 1, 0, -1]
    index = 0

    while True:
        yield values[index]
        index = (index + 1) % 4


iter_c = iterate_0_1_0_neg1()

#test za pomocą for
stop = 10
count = 0
for i in iter_c:
    print(i)
    if count >= stop:
        break
    count += 1



