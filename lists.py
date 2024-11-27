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
print(f"my garage: {sorted(motorcycles)}")


