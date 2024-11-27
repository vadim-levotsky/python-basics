## Dictionaries = like map in Java
## key = any immutable value ()
## value = anything you want
from jinja2.filters import do_format

dog = {"name": "Roger", "age": 8, "color": "brown"}

print(dog)
print(dog["age"])

dog["name"] = "syd"
print(dog)

print(dog.get("city", "pinsk")) ## get value. if didn't find a key than return a default value = pinsk (in example)

print("**** DELETE ****")
print(dog.pop("color"))
print(dog.pop("color", "gold")) ## remove and return value. if didn't find a key than return a default value = gold (in example)
print(dog)

print('removing: ', dog.popitem())
print(dog)

print("\n*** ADD VALUES ***")
dog.update({"color" : "gold"})
dog["city"] = "pinsk"
print('updated: ', dog)

print("*** LIST VALUES ***")
print("print keys: ", dog.keys())
print("print keys: ", dog.values())
keys = list(dog.keys())
print("print keys class: ", type(keys), ", values: ", keys)
print("print keys: ", list(dog.values()))
dog_list = list(dog.items())
print("convert into list: ", dog_list)
print("class: ", type(dog_list[0]), ", value: ", dog_list[0])

