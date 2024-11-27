import time

from debugpy.common.timestamp import current

bicycles = ['treK', 'cannondale', 'specialized', 'mErida', 'scott']
print(bicycles)
print(bicycles[2].title())
## accessing elements from tail
print("LAST ELEMENT: " + bicycles[-1].upper())
print("second elem from the end: " + bicycles[-2].capitalize())
## using f-string
print(f"wanna buy bicycle {bicycles[0].title()}")

## modifying lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"my garage: {motorcycles}")
motorcycles[0] = 'ducati'
print(f"replace first motorcycle. my garage: {motorcycles}")

motorcycles.append('bmw')
motorcycles.sort(reverse=True)
print(f"add a new motorcycle. my garage: {motorcycles}")

del motorcycles[0] ## just remove element
print("remove " + motorcycles.pop(1) + " from garage") ## pop(index) - remove and use and get a value of removed elem
## pop() without index - remove last elem.
print(f"my garage: {motorcycles}")

motorcycles.insert(2, 'HONDA')
print(f"my garage: {motorcycles}")

motorcycles.remove("honda".upper()) ## remove only 1st occurrence of the value
print(f"my garage: {sorted(motorcycles)}")  ## function 'sorted(list)' sort list without modifying it

## List could hold mix different types.
## but sort would not work because of different types
items = ["Roger", 1, "syd", True]

print("Roger" in items) # -> true
print("Jim" in items) # -> false

print(items[1])
# update item
items.append("Jim")
items.extend(["bob", 5])
print(items[2:4]) # -> ['Syd', True]
print(items[4:])  # -> ['Jim', 'Bob', 5]

items += ["Beau", "milky"]

## make a copy
print("\n**** COPY ****")
items_copy = items[:] ## make a slice with nothing in the beginning and nothing in the end
print(f'items copy: {items_copy}')
items_copy = [str(element) for element in items_copy]
print("\n**** SORT WITHOUT MODIFYING LIST****")
sorted_list = sorted(items_copy, key=lambda x: x.lower())
print(f"original list: {items_copy}\nsorted list: {sorted_list}")
sorted_list = sorted(items_copy, key=str.lower, reverse=True)
print(f"original list: {items_copy}\nreverse sorted list: {sorted_list}")
print("\n**** SORT WIT MODIFYING LIST****")
items_copy.sort(key=str.lower)
print(f"sorted items: {items_copy}")

print("*** CREATE A LIST ***")
numbers_list = list(range(1, 10))
print(numbers_list)

for value in range(1, 5):
    print(value)

squares = []
squares_dict = {}
start = time.time()
for v in range (1, 11):
    square = v ** 2
    squares.append(square)
    squares_dict[v] = square

print("squares 1 to 10= ", squares)
print("squares = ", squares_dict)
print(f"min value={min(squares)}, max value={max(squares)}, sum={sum(squares)}")
print("DURATION: ", time.time() - start)

### LIST COMPREHENSIONS
squares_3 = [v ** 2 for v in range(1, 11)]
print("list comprehensive: ", squares_3)

for i in range(1, 21):
    print(i)

million = list(range(1, 1_000_001))
# for value in million:
#     print(value)

print(f"min value={min(million)}, max value={max(million)}, sum={sum(million)}")

odd_numbers = list(range(1, 20, 2))
print(f"odd numbers: {odd_numbers}")

multiply_three = []
for i in range(3, 31):
    multiply_three.append(i * 3)
multiply_three_2 = [value * 3 for value in range(3, 31)]
print(multiply_three)
print(multiply_three_2)
assert multiply_three_2 == multiply_three
print(multiply_three == multiply_three_2)

cubes = [v ** 3 for v in range(1, 11)]
for cube in cubes:
    print(cube)

### SLICING A LIST
print(multiply_three[0:15:3]) ## slice from 0 includes to 15 inclusive with step = 3 (indexes = 0,3,6,9,12)
print(multiply_three[:-3]) # from 0 to 3rd element from end
print(multiply_three[-3:]) # last 3 elements

