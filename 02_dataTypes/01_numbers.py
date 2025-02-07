import math
import random
from decimal import Decimal
from fractions import Fraction

# Basic Arithmetic Operations
x, y, z = 2, 3, 4
print(x + y)  # 5
print(40 + 2.23)  # 42.23
print(int(2.23))  # 2
print(float(40) + 2.23)  # 42.23

# String Concatenation
print('chai' + 'code')  # chaicode
print('chai' + ' code')  # chai code

# Arithmetic Operations
print(x + 1, y * 2)  # (3, 6)
print(y % 2)  # 1
print(z ** 4)  # 256
print(100 ** 2)  # 10000
print(2 ** 100)  # Large number

# Division and Floating Points
result = 1 / 3.0
print(result)  # 0.3333333

# String Representations
print(repr('chai'))  # 'chai'
print(str('chai'))  # chai
print("chai")  # chai

# Boolean Operations
print(1 < 2)  # True
print(True == 1)  # True
print(5.0 == 5.0)  # True
print(4.0 != 5.0)  # True
print(x < y < z)  # True
print(x < y and y < z)  # True
print(1 == 2 and 2 < 3)  # False

# Math Module Functions
print(math.floor(3.5))  # 3
print(math.trunc(2.8))  # 2

# Large Numbers
print(999999999999999999999999999999999999999999999 + 1)
print(2 ** 200)

# Complex Numbers
print(2 + 1j * 3)  # (2+3j)
print((2 + 1j) * 3)  # (6+3j)

# Number Systems
print(oct(64))  # '0o100'
print(hex(64))  # '0x40'
print(bin(64))  # '0b1000000'
print(int('1000', 2))  # 8

# Bitwise Operations
x = 1
print(x << 2)  # 4
print(x | 2)  # 3

# Random Module
print(random.random())  # Random float
print(random.randint(1, 10))  # Random integer between 1 and 10
l1 = ['lemon', 'mint', 'ginger']
print(random.choice(l1))  # Random choice
random.shuffle(l1)  # Shuffle list
print(l1)

# Floating Point Precision Issue
print(0.1 + 0.1 + 0.1)  # 0.30000000000000004
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))  # Decimal('0.3')

# Fractions
myFra = Fraction(2, 7)
print(myFra)  # Fraction(2, 7)

# Set Operations
setone = {1, 2, 3, 4}
print(setone & {1, 3})  # {1, 3}
print(setone | {1, 3, 7})  # {1, 2, 3, 4, 7}
print(setone - {2, 4})  # {1, 3}

# Boolean Type
print(type(True))  # <class 'bool'>
print(True == 1)  # True
print(False == 0)  # True
print(True + 5)  # 6
