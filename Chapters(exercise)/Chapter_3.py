# Try these short programs to get some firsthand experience with Python’s lists.
# You might want to create a new folder for each chapter’s exercises, to keep
# them organized.
# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

names: list[str] = ["Yahya", "AbdulRehman", "Ahmed", "Ali", "Ghasiq"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just

# printing each person’s name, print a message to them. The text of each mes-
# sage should be the same, but each message should be personalized with the

# person’s name.

names: list[str] = ["Yahya", "AbdulRehman", "Ahmed", "ALi", "Ghasiq"]

for name in names:
    print(f"Hy {name}, I hope you are doing good")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

vehicles: list[str] = ["Kawaski Ninja H2r", "Mustang 1967", "Mazda Rx7", "Mark X"]

for vehicle in vehicles:
    print(f"I would like to own a {vehicle}")