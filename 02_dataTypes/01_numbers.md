**Python Basics: Numbers, Boolean, and Operations**

## 1. Numeric Types in Python
Python supports different numeric types:
- **Integers** (`int`): Whole numbers (e.g., `2, 100, -5`).
- **Floating Point Numbers** (`float`): Numbers with decimals (e.g., `3.14, -2.5, 40.0`).
- **Complex Numbers** (`complex`): Numbers with imaginary parts (e.g., `2 + 1j`).

### 1.1 Arithmetic Operations
- Addition: `2 + 3` → `5`
- Subtraction: `5 - 2` → `3`
- Multiplication: `4 * 3` → `12`
- Division: `5 / 2` → `2.5`
- Floor Division: `5 // 2` → `2`
- Modulus: `5 % 2` → `1`
- Exponentiation: `2 ** 4` → `16`

### 1.2 Type Conversion
- `int(2.23)` → `2`
- `float(40) + 2.23` → `42.23`
- String concatenation: `'chai' + 'code'` → `'chaicode'`

### 1.3 Comparisons & Boolean Operations
- `1 < 2` → `True`
- `1 == True` → `True`
- `1 is True` → `False` (because `is` checks object identity, not value equality)
- `4.0 != 5.0` → `True`
- `x < y < z` → `True`

## 2. Mathematical Functions (math module)
- `math.floor(3.5)` → `3`
- `math.floor(-3.5)` → `-4`
- `math.trunc(2.8)` → `2`
- `math.trunc(-2.8)` → `-2`

## 3. Large Integer Handling
- Python supports arbitrary precision integers:
  - `999999999999999999999999999999999999999999999 + 1`
  - `2 ** 1000` → Huge number

## 4. Number Representation
- **Octal**: `0o20` → `16`
- **Hexadecimal**: `0xFF` → `255`
- **Binary**: `0b1000` → `8`
- Conversions:
  - `oct(64)` → `'0o100'`
  - `hex(64)` → `'0x40'`
  - `bin(64)` → `'0b1000000'`
  - `int('1000', 2)` → `8`

## 5. Bitwise Operations
- `x << 2` (Left Shift) → Multiplies by `2^n`
- `x | 2` (Bitwise OR) → Performs logical OR operation

## 6. Floating-Point Precision Issues
- `0.1 + 0.1 + 0.1 - 0.3` → Small floating error (`5.551115123125783e-17`)
- Use **Decimal module** for precision:
  - `Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')` → `0.0`

## 7. Fractions
- `from fractions import Fraction`
- `Fraction(2, 7)` → `2/7`

## 8. Sets
- Intersection: `{1, 2, 3, 4} & {1, 3}` → `{1, 3}`
- Union: `{1, 2, 3, 4} | {1, 3, 7}` → `{1, 2, 3, 4, 7}`
- Difference: `{1, 2, 3, 4} - {2, 4}` → `{1, 3}`

## 9. Boolean Data Type
- `type(True)` → `<class 'bool'>`
- `True + 5` → `6`
- `False == 0` → `True`
- `True is 1` → `False`

## 10. Randomization (random module)
- `random.random()` → Generates a random float (0.0 to 1.0)
- `random.randint(1, 10)` → Random integer between 1 and 10
- `random.choice(['lemon', 'mint', 'ginger'])` → Random element
- `random.shuffle(l1)` → Shuffles a list

---
This document summarizes Python's fundamental number operations, types, and key functions with practical examples.

