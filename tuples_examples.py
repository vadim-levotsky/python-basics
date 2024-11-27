## tuples are immutable.

names = ("Roger", "Syd", "Anna", "bob")

print(names[0])
print(names.index("Syd"))

print('lenght = ' + str(len(names)))

print("Roger" in names)

sorted_names = sorted(names, key=str.lower)
print(f"sorted: {sorted_names}")
print(f"original: {names}")
