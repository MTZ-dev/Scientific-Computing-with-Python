#EXERCISE 6.1

#W tym zadaniu dodatkowo zabezpieczyłem współrzedne x,y,z wektora pod postacią zmiennych "prywatnych" _x,_y,_z
#Użyłem dekoratorów @property oraz @func.setter, żeby zdefiniować gettera i settera dla zmiennych x,y,z w tej klasie
#Zrobiłem to bo potrzebowałem się sam nauczyć wykorzystania tych metod i stwierdziłem, że to dobra okazja na przetestowanie
#Dodatkowo dzięki temu zaimplementowałem klasę tak, że tylko floaty sa przyjmowane jako dozwolone wartości współrzednych wektora
#Zmodyfikowałem testy dodajac .0, żeby wszytko było instancja float

import math


class Vector:
    "Implements a class of 3D vectors (floats as coordinates) along with an interface for their manipulation"

    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        
        self.x = x
        self.y = y
        self.z = z


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


    

v = Vector(1.0, 2.0, 3.0)
w = Vector(2.0, -3.0, 2.0)
assert v != w
assert v + w == Vector(3.0, -1.0, 5.0)
assert v - w == Vector(-1.0, 5.0, 1.0)
assert v * w == 2.0
assert v.cross(w) == Vector(13.0, 4.0, -7.0)
assert v.length() == math.sqrt(14.0)
S = set([v, v, w])
assert len(S) == 2.0

print("Tests passed")