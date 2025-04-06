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

