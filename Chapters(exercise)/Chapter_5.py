# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:

# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

value = 10
print("\nIs Value == 10 ? I predict True.")
print(value == 10)
print("Is Value == 20 ? I predict False.")
print(value == 20)

print("\nIs Value > 10 ? I predict True")
print(value > 7)
print("Is Value > 20 ? I predict False")
print(value < 7)

colors = ['red', 'blue', 'green']
print("\nIs Color == 'red'? I predict True.")
print('red' in colors)

print("Is Color == 'yellow'? I predict False.")
print('yellow' in colors)

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
# ate to 10. If you want to try more comparisons, write more tests and add them

# to conditional_tests.py. Have at least one True and one False result for each of
# the following:

# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

# • Tests for equality and inequality with strings

city = "karachi"

print("\nIs city == karachi ? I predict True")
print(city == "karachi")
print("Is city == Lahore ? I predict False")
print(city == "lahore")

print("\nIs city != karachi ? I predict True")
print(city != "lahore")
print("Is city != Lahore ? I predict False")
print(city != "karachi")

# • Tests using the lower() method

print("\nIs city.lower == karachi ? I predict True")
print(city.lower() == "karachi")
print("Is city == KARACHI ? I predict False")
print(city.lower() == "KARACHI")

print("\nIs city != karachi ? I predict True")
print(city.lower() != "Karachi")
print("Is city != karachi ? I predict False")
print(city.lower() != "karachi")

# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to

print("\nIs Value > 10 ? I predict True")
print(value > 8)
print("Is Value > 20 ? I predict False")
print(value < 8)


print("\nIs Value > 10 ? I predict True")
print(value >= 8)
print("Is Value > 20 ? I predict False")
print(value <= 8)

# • Tests using the and keyword and the or keyword

age = 18
country = "pakistan"

print("\nIs age > 16 and country == pakistan")
print(age > 16 and country == "pakistan")
print("Is age > 16 and country == lahore")
print(age > 16 and country == "lahore")

print("\nIs age > 16 and country == pakistan")
print(age > 16 or country == "pakistan")
print("Is age > 16 and country == lahore")
print(age < 16 or country == "lahore")

# • Test whether an item is in a list

furits = ["banana", "mango", "apple"]

print("\nIs mango in furits ? I predict True")
print('mango' in furits)
print("Is orange in furits ? I predict False")
print('orange' in furits)

# • Test whether an item is not in a list

print("\nIs watermelon in furits ? I predict True")
print('watermelon' not in furits)
print("Is apple in furits ? I predict False")
print('apple' not in furits)

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)

alien_color = "green"

if(alien_color == "green"):
    print("that the player just earned 5 points.")
else:
    print("The version that fails will have no output.")

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
# and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5
# points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# • Write one version of this program that runs the if block and another that
# runs the else block.

alien_color = "green"

if(alien_color == "green"):
    print("the player just earned 5 points for shooting the alien.")
else:
    print("the player just earned 10 points.")

alien_color = "red"

if(alien_color == "green"):
    print("the player just earned 5 points for shooting the alien.")
else:
    print("the player just earned 10 points.")

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-
# else chain.

# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

alien_color = "green"

if (alien_color == "red"):
    print("the player earned 5 points.")
elif (alien_color == "green"):
    print("the player earned 10 points.")
else:
    print("the player earned 15 points.")

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage
# of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is
# a baby.
# • If the person is at least 2 years old but less than 4, print a message that the
# person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder.

person_age = 18

if age < 2:
    print("the person is baby.")
elif age >= 2 and age <= 4:
    print("the person age is tolder.")
elif age >= 4 and age <= 13:
    print("the person is a kid.")
elif age >= 13 and age <= 20:
    print("the person is a teenager.")
elif age >= 20 and age <= 65:
    print("the person is an adult.")
else:
    print("the person is an elder.")


# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!

favorite_fruits = ["banana", "apple", "mango"]

if  "banana" in favorite_fruits :
    print("You really like banans!")
elif  "apple" in favorite_fruits :
    print("You really like apple!")
elif  "mango" in favorite_fruits :
    print("You really like oranges!")
elif  "orange" in favorite_fruits :
    print("You really like orange")
elif  "grapes" in favorite_fruits :
    print("You really like grapes!")

# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user.
# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.

usernames: list[str] = ["admin", "Yahya", "Ahemd", "Ali", "Ghasiq"]

for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!

# • Remove all of the usernames from your list, and make sure the correct mes-
# sage is printed.

users = ["Admin", "Yahya", "Ahmed"]

if users:
    for user in users:
        if user == "Admin":
            print("Hello Admin, would like to see a status report?")
        else:
            print(f"Hello, {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users")

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)

current_users = ["david", "mark", "patrick", "sarah", "joan"]

new_users = ["joan", "mark", "sarah", "john", "doris"]

new_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    print(f"Sorry, the username '{new_user}' is already taken. Please choose a different one.")
else:
    print(f"The username {new_user} available")