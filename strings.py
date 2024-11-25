# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

name = "ada lovelace"
print(name.capitalize())
print(name.title())
name = name.title()
print('=====')
print(name.lower())
print(name.upper())
print("======")
first_name = "john"
last_name = "snow"
print(f"Hello {first_name.title()} {last_name.upper()}!")
full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
print(f"Good bye {full_name}!")
print("======")
java = "     java  "
pythooon = "python   "
kotlin = "   KOTLIN"
print(f"I know following programming languages:\n\t{java.strip().upper()}!!\n\t{pythooon.rstrip().title()}!\n\t!{kotlin.lower().lstrip()}")
