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


# The following exercises are a bit more complex than those in Chapter 2, but
# they give you an opportunity to use lists in all of the ways described.
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

guests: list[str] = ["Sir Ameen Alam", "Sir Zia Khan", "Sir Qasim"]

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.

unavailable_guests: str = "Sir Ameen Alam"

changeing_guests_list:str = "Sir Hamza Alvi"

print(f"\nUnfortunately, {unavailable_guests} can't attend the dinner.")

guests[guests.index(unavailable_guests)] = changeing_guests_list

for guest in guests:
    print(f"Dear {guests}, I would be honored to have you join me for dinner.")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

guests: list[str] = ['Sir Hamza Alvi', 'Sir Zia Khan', 'Sir Qasim']

print("\nGreat news! we found a bigger dinner table, so we are inviting more guests.\n")

guests.insert(0, "Sir Bilal Khan")
guests.insert(len(guests) // 2, "Sir Bilal Attari")
guests.append("Sir Ali Aftab")

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for inviting")

    