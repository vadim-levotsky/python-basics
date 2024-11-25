name = "Beau"
age = 39
year = "2000"

print(f"{name} {age}")

# data types
print(type(name))
print(type(age))
print(isinstance(age, int))
print(isinstance(age, float))
print(isinstance(int(year), int))

print("=== operators ===")
print(1 + 1)
print(10 - 11)
print(2 * 2)
print(4 / 2)
print(5 // 2)
print(4 % 3)
print(4 ** 2)
temp = 2
temp += 5
print(temp)
temp *= 2
print(temp)

print("=== boolean ===")

condition1 = True
condition2 = False
print(condition1 and condition2)
print(condition1 or condition2)
print("=== OR operator ====")
print(0 or 1)
print(False or 'hi')
print('hi' or 'hey')
print([] or False)
print(False or [])

print("=== AND operator ====")
print(0 and 1)
print(1 and 0)
print(False and 'hi')
print('hi' and 'hey')
print([] and False)
print(False and [])

print("=== ternary ===")
def is_adult(age):
    return True if age > 18 else False

# STRINGS
"john"
'john'
name = "jOhN"
phrase = name.title() + " is my name"
age = str(44)
print(f'''
{name.title()} {age}
''')
print(name.isalnum())
print(str().isalnum()) #is empty
print("jo" in name.lower())
### reverse
print(phrase[::-1])
print("".join(reversed(phrase)))


# BOOLEANS

book1_read = True
book2_read = False
print(any([book1_read, book2_read]))
print(all([book1_read, book2_read]))

# NUMBER DATA TYPES
#### int, float, complex
complex_number = 2 + 3j
num = complex(2, 3)
print(num.real, num.imag)

print(abs(-5.5))
print(round(5.49, 1))

THIS_IS_CONSTANT = 10
THIS_IS_CONSTANT += 1
print(THIS_IS_CONSTANT)
