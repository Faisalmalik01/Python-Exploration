# Mutable and Immutable Objects –

In Python, mutability determines whether an object can be modified after its creation. You explored reference counting, assignment, reclamation, and garbage collection, as well as how names in Python point to objects dynamically.
# 1️⃣ Reference Counting

Every object in Python has a reference count, which tracks how many variables (names) are pointing to it.

Example:

a = [1, 2, 3]  # A list is created
b = a          # 'b' now references the same list

    The list [1, 2, 3] has two references: a and b.
    If a and b both stop referencing the list, Python will delete it.

Check reference count:

import sys
x = [1, 2, 3]
print(sys.getrefcount(x))  # Usually 2 (one for 'x' and one for function argument)

# 2️⃣ Assignment & Dynamic Reference

Python variables are just labels (names) referencing objects. The object type is stored within the object, not in the variable name.

Example:

a = 3        # 'a' points to an integer object 3  
a = "hello"  # Now 'a' points to a string  
a = [1, 2]   # Now 'a' points to a list  

    The old objects (3, "hello") are discarded if not referenced elsewhere.

Dynamic reference also applies to mutable vs immutable types:

x = [1, 2, 3]
y = x  
x = "new value"  

print(y)  # [1, 2, 3] (old list is still referenced by 'y')
print(x)  # "new value" (x now refers to a string)

    y retains the old list because x was reassigned to "new value".

# 3️⃣ Object Reclamation & Garbage Collection

When an object’s reference count drops to zero, it becomes a candidate for garbage collection.

x = [1, 2, 3]  
x = None  # The list [1,2,3] loses its reference and is deleted

    Python’s Garbage Collector automatically reclaims memory for unreferenced objects.
    However, garbage collection in Python runs a bit late for immutable types (like strings and numbers).

To manually trigger garbage collection:

import gc
gc.collect()

# 4️⃣ Mutable vs Immutable Assignment Behavior
(a) Assigning Immutable Objects (Integer, String, Tuple)

a = 3
b = a  
a = 5  

print(a)  # 5  
print(b)  # 3  (b is unchanged)

    Since a = 5 creates a new integer object, b remains 3 because integers are immutable.

(b) Assigning Mutable Objects (Lists, Dictionaries, Sets)

l1 = [1, 2, 3]
l2 = l1  
l1[0] = 44  

print(l1)  # [44, 2, 3]
print(l2)  # [44, 2, 3]  (Both l1 and l2 point to the same list!)

    Since lists are mutable, modifying l1 also affects l2.

To avoid this, use copying:

l1 = [1, 2, 3]
l2 = l1[:]  # Creates a new copy
l1[0] = 44  

print(l1)  # [44, 2, 3]
print(l2)  # [1, 2, 3] (unchanged)

Or use copy.copy() or copy.deepcopy() for nested lists.
# 5️⃣ Identity (is) vs Equality (==)

    == compares values.
    is compares memory locations (object identity).

Example:

m = [11, 22, 33]
n = m  

print(m == n)  # True (values are same)
print(m is n)  # True (both point to same object)

Now, creating a new list:

m = [11, 22, 33]  
print(m == n)  # True (values are same)  
print(m is n)  # False (m now points to a different object)  

    m and n no longer reference the same list, so is returns False.