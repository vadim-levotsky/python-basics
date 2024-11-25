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
print(f'''I know following programming languages:
\t{java.strip().upper()}!!
\t{pythooon.rstrip().title()}!
\t!{kotlin.lower().lstrip()}''')

## sting is False when it's empty
empty_string = ""
if empty_string:
    print("Is NOT empty")
else:
    print("Is empty")

print("is not empty? -> " + str(empty_string.isalpha()))

file_name = "python_notes.py"
print(file_name.removesuffix(".py"))
site_url = "https://bla-bla.com"
print(site_url.removeprefix("https://"))