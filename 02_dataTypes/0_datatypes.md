# 1️⃣ Object Types / Data Types in Python

Python has several built-in data types, including:
🟢 Numbers:

    Integer (int): 1234
    Floating-point (float): 3.14
    Complex numbers (complex): 3+4j
    Binary (0b111)
    Special types: Decimal(), Fraction()

🟡 Strings:

    Examples: 'spam', "Bob"
    Unicode: u'sp\xc4m'
    Immutable (can’t change individual characters)

🔵 Lists (Mutable, Ordered):

    [1, [2, 'three'], 4.5]
    list(range(10))
    Indexing & slicing possible

🟠 Tuples (Immutable, Ordered):

    (1, 'spam', 4, 'U')
    tuple('spam')
    namedtuple for structured data

🟣 Dictionaries (Key-Value Pairs, Mutable):

    {'food': 'spam', 'taste': 'yum'}
    dict(hours=10)

🟤 Sets (Unordered, Unique Values):

    set('abc')
    {'a', 'b', 'c'}

⚪ Boolean & None:

    True, False
    None → Represents an empty reference

⚫ Files:

    open('eggs.txt')
    open(r'C:\ham.bin', 'wb')

🔶 Advanced Types:

    Functions, Modules, Classes
    Decorators, Generators, Iterators, MetaProgramming


# 2️⃣ Practical Operations & Examples

📌 Basic Arithmetic Operations:

12 + 12  # Output: 24
2.5 * 5  # Output: 12.5
2 ** 4   # Output: 16  (Exponentiation)

📌 Using the math Module:

import math
math.pi  # Output: 3.141592653589793

📌 Generating Random Values:

import random
random.random()        #Random float (0 to 1)
random.choice([1,2,3]) #Picks a random item from the list

# 3️⃣ Strings – Indexing & Slicing

username = "FaisalMallik"
len(username)      # Output: 12
username[0]        # Output: 'F'
username[-1]       # Output: 'k'
username[1:3]      # Output: 'ai'
username[0] = 'A'  # ❌ Error (Strings are immutable)

# Using dir() to explore available string methods:

dir(username)

# 4️⃣ Lists – Mutable & Indexed

myList = [123, 'coffee', 3.14]
len(myList)  # Output: 3

myList_2 = [1, 2, [3, 4], 'a', 'b']
myList_2[2]  # Output: [3, 4]
myList_2[-1] # Output: 'b'

# 5️⃣ Dictionaries – Key-Value Pairs

myD = {'one': 'lemon', 'two': 'ginger', 'comic': 'superman'}
myD['comic']  # Output: 'superman'

# 6️⃣ Tuples – Immutable Sequences

myTup = (1, 2, 3, 4)
len(myTup)  # Output: 4
myTup[0]    # Output: 1

