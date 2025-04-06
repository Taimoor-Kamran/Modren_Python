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

rivers:dict[str] = {
    "Tocantins" : "Brazil",
    "Brahmaputra" : "India",
    "Lena" : "Russia",
}

for river, country in rivers.items():
    print(f"The {river} run through {country}")

print("\nNames of Rivers:")

for river in rivers:
    print(river)

print("\nNames of Country")

for country in rivers:
    print(country)

# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.


favorite_language: dict[str] = {
    "Taha": "TypeScript",
    "Hassnain": "Ruby",
    "Hassan": "Python",
    "Ghasiq": "C++"
}

people_to_poll: list[str] = ["Ghasiq" ,"Taha", "Suban", "Zohan", "Hassnain", "Hassan", "Mujtaba"]

for person in people_to_poll:
    if person in favorite_language:
        print(f"thankyou for responding. {person.title()}")
    else:
        print(f"{person}, please take the poll.")

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make

# two new dictionaries representing different people, and store all three dictionar-
# ies in a list called people. Loop through your list of people. As you loop through

# the list, print everything you know about each person.

person_1: dict[str, str, str | int, str] = {"first_name": "Zohan", "last_name": "Zain", "age": 10, "city": "Karachi"}
person_2: dict[str, str, str | int, str] = {"first_name": "Mustafa", "last_name": "jalal", "age": 20, "city": "Karachi"}
person_3: dict[str, str, str | int, str] = {"first_name": "Mansukh", "last_name": "sham", "age": 19, "city": "India-delhi"}

people:list[str] = [person_1, person_2, person_3]

for person in people:
    print(f"\nFirst Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")

# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
# ent pet. In each dictionary, include the kind of animal and the owner’s name.

# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet_1: dict[str] = {
    "animal": "cat",
    "owner": "Ali"
}

pet_2: dict[str] = {
    "animal": "dog",
    "owner": "Hashir"
}

pet_3: dict[str] = {
    "animal": "lion",
    "owner": "Ahmed"
}

pet_4: dict[str] = {
    "animal": "leopard",
    "owner": "Shani"
}

pets:list[str] = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Animal: {pet["animal"].title()}")
    print(f"Owner: {pet["owner"].title()}")
    print("\n")

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places for
# each person. To make this exercise a bit more interesting, ask some friends to
# name a few of their favorite places. Loop through the dictionary, and print each
# person’s name and their favorite places.

favorite_places: dict[str] = {
    "Ali" : ["Great wall of china", "Paris", "The great pyramid of giza"],
    "Ahmed": ["Angkor Wat", "Bangkok", "Eiffel Tower"],
    "Hashir": ["Dubai", "Taj Mahal", "Statue of liberty"]
}

for names, places in favorite_places.items():
    print(f"{names}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print()

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers: dict[str, int] = {"Ali" : [7, 4, 5], "Ahmed" : [5,2,1], "Bilalwal": [4, 8, 8], "haroon": [3, 2 ,2], "Musa": [8, 2, 2]}

for name, f_numbers  in favorite_numbers.items():
    print(f"{name}, favorite numbers are:")
    for f_number in f_numbers:
        print(f"- {f_number}")

    print()