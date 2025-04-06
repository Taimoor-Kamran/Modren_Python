# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each piece
# of information stored in your dictionary.

person: dict[str, str, str | int, str] = {"first_name": "Zohan", "last_name": "Zain", "age": 10, "city": "Karachi"}

print(person)

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite

# Dictionaries 99
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favorite_numbers: dict[str, int] = {"Ali" : 7, "Ahmed" : 5, "Bilalwal": 4, "haroon": 3, "Musa": 8}

for name, f_number  in favorite_numbers.items():
    print(f"{name}'s favorite number is {f_number}")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary: dict[str] = {"Variables": "A container to storing a data and value",
                       "functions": "A block of code that runs only when it's called.",
                       "loop": "used to repeat a block of code multiple time.",
                       "dictionary": "A collection of key value pairs in python.",
                       "if_statment": "Used to make decision in code based on conditions."}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n {meaning}")

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary_second: dict[str] = {
    "Variable": "A container to store data and value.",
    "function": "A block of code that runs when it's call.",
    "loop": "used to repeat block of code multiple time.",
    "dictionary": "A collection of key value pairs in python",
    "if_statment": "used to make decision in code based on conditions.",
    "list": "A collection of items in a specific order.",
    "tuple": "An immutable list of items",
    "set": "An unordered collection of unique items",
    "class": "A blueprint for creating objects (a user-defined data structure).",
    "import": "Used to bring in external modules or libraries."
}

for word, meaning in glossary_second.items():
    print(f"{word.title()}:\n {meaning}")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.