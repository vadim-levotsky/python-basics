## tuples are immutable. like immutable list
## use them when you want to store a set of values that souldn't be changed
tuple_with_one_element = ("single",)
incorrect = ("single")
print("tuple with one element: ", tuple_with_one_element)
print("not a tuple with ONE element: ", incorrect)
names = ("Roger", "Syd", "Anna", "bob")
print(f"tuple: {names}")

print(names[0])
print(names.index("Syd"))

print('lenght = ' + str(len(names)))

print("Roger" in names)

sorted_names = sorted(names, key=str.lower)
print(f"sorted: {sorted_names}")
print(f"original: {names}")

## BUFFET
print("\n*** BUFFET ***\n")
buffet = ("scrumbled eggs", "souseges", "pancakes", "coffe", "muffin")
for value in buffet:
    print(value)

# buffet[1] = "bacon"; -> TypeError: 'tuple' object does not support item assignment

new_buffet = list(buffet[0:3])
new_buffet.append("tea")
new_buffet.append("crousaint")
new_buffet = tuple(new_buffet)
print("type", type(new_buffet))
for value in new_buffet:
    print(value)
