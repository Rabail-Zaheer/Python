# -------------------------
# 1. Parentheses ()
# -------------------------
print("Parentheses:")
print(2 * (3 + 1))    # Do the brackets first → 3+1 = 4, so 2*4 = 8
print()

# -------------------------
# 2. Exponentiation **
# -------------------------
print("Exponentiation (** means power):")
print(2 ** 3)         # 2 to the power 3 → 2*2*2 = 8
print()

# -------------------------
# 3. Unary + and -
# -------------------------
print("Unary + and -:")
print(+5)             # Just a positive number
print(-7)             # A negative number
print()

# -------------------------
# 4. Multiply, Divide, Modulo, Floor Division
# -------------------------
print("Multiply, Divide, Modulo, Floor Division:")
print(3 * 4)          # Multiply → 12
print(10 / 2)         # Divide → 5.0
print(10 % 3)         # Modulo → leftover when dividing (10 % 3 = 1)
print(10 // 3)        # Floor division → whole groups only (3)
print()

# 20 

# -------------------------
# 5. Addition and Subtraction
# -------------------------
print("Addition and Subtraction:")
print(10 + 5)         # Add → 15
print(10 - 4)         # Subtract → 6
print()

# -------------------------
# 6. Right and Left Shift
# -------------------------
print("Right and Left Shift:")
print(4 << 1)         # Shift left → like doubling (4 becomes 8)
print(8 >> 1)         # Shift right → like halving (8 becomes 4)
print()

# -------------------------
# 7. Bitwise AND &
# -------------------------
print("Bitwise AND (&):")
print(6 & 3)          # 6 = 110, 3 = 011 → AND = 010 → 2
print()

# -------------------------
# 8. Bitwise OR | and XOR ^
# -------------------------
print("Bitwise OR | and XOR ^:")
print(6 | 3)          # OR (turns ON if either is ON)
print(6 ^ 3)          # XOR (ON only if they are different)
print()

# -------------------------
# 9. Comparison Operators < > <= >=
# -------------------------
print("Comparison Operators:")
print(5 < 9)          # True
print(10 > 20)        # False
print(3 <= 3)         # True
print(4 >= 10)        # False
print()

# -------------------------
# 10. Equality Operators == !=
# -------------------------
print("Equality Operators:")
print(5 == 5)         # True (same)
print(5 != 3)         # True (different)
print()

# -------------------------
# 11. Assignment Operators
# -------------------------
print("Assignment Operators:")
x = 10                # Put value 10 inside x
print(x)
x += 2                # Add 2 → x becomes 12
print(x)
print(x = x + 2)
x *= 3                # Multiply by 3 → x becomes 36
print(x)
print()

# -------------------------
# 12. Identity Operators (is, is not)
# -------------------------
print("Identity Operators:")
a = [1, 2, 3]
b = a                 # b points to the same list
c = [1, 2, 3]         # c is a separate new list

print(a is b)         # True → same object
print(a is c)         # False → looks same but different object
print()

# -------------------------
# 13. Membership Operators (in, not in)
# -------------------------
print("Membership Operators:")
print("a" in "cat")   # True
print(5 in [1, 2, 3]) # False
print()

# -------------------------
# 14. Logical Operators (and, or, not)
# -------------------------
print("Logical Operators:")
print(True and False) # False (both must be True)
print(True or False)  # True (one must be True)
print(not True)       # False (opposite)
print()

# -------------------------
# Expressions Example
# -------------------------
print("Expressions:")
print(5 + 3)          # Expression that gives value 8
print("hi" * 3)       # Expression that repeats text
age = 10
print(age + 2)        # Expression using a variable
print()
