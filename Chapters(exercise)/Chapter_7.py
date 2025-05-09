# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

rental_car: str = input("what kind of rental car would you like?")

print(f"“Let me see if I can find you a {rental_car}")

# 7-2. Restaurant Seating: Write a program that asks the user how many people

# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

dinner = int(input("How many people are in their dinner group?"))

if dinner <= 8:
    print("they'll have to wait for a table.")
else:
    print("their table is ready.")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = int(input("Enter a Number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10")

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

while True:
    topping : str = input("Enter a pizza topping(or type 'quit' to stop.)")
    
    if topping == 'quit':
        print(f"{topping} Thankyou! We're preparing you pizza.")
        break
    else:
        print(f"I'll add {topping} to your pizza.")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

while True:
    age_input = input("Let me know your age (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        print("Thank you! Enjoy your movie.")
        break

    age = int(age_input)

    if age < 3:
        print("The ticket is free.")
    elif age >= 3 and age <= 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
# each of the following at least once:

# Use a conditional test in the while statement to stop the loop.

age_input = ""

while age_input.lower() != "quit":
    age_input = input("Enter your age (or type 'quit' to exit):")


    if age_input == 'quit':
        print("Goodbye")
        continue

    age = int(age_input)

    if age < 3:
        print("ticket is free")
    elif age >= 3 and age <= 12:
        print("ticket is $10")
    else:
        print("ticket is $15")

# Use an active variable to control how long the loop runs.

active = True

while active:
    age_input = input("Enter your age (or type 'quit' to exit):")

    if age_input.lower() == 'quit':
        active = False
    else:
        age = int(age_input)

        if age < 3:
            print("The ticket is free.")
        elif age >= 3 and age <= 12:
            print("The ticket is 10$.")
        else:
            print("The ticket is 15$.")

# Use a break statement to exit the loop when the user enters a 'quit' value.

while True:
    age_input = input("Enter your age (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        break

    age = int(age_input)

    if age < 3:
        print("The ticket is free.")
    elif age <= 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")

# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
# CTRL-C or close the window displaying the output.)

# while True:
    # print("Press CTRL + C")

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order, such as I made
# your tuna sandwich. As each sandwich is made, move it to the list of finished
# sandwiches. After all the sandwiches have been made, print a message listing
# each sandwich that was made.

sandwich_orders = ["Club sandwich", "Reuben sandwich", "Chicken sandwich"]
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order}.")
    finished_sandwiches.append(sandwich_order)

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ["pastrami", "Club sandwich", "pastrami", "Reuben sandwich", "pastrami", "Chicken sandwich"]

finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)

print("\nall sandwich list:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

# 7-10. Dream Vacation: Write a program that polls users about their dream vaca-
# tion. Write a prompt similar to If you could visit one place in the world, where

# would you go? Include a block of code that prints the results of the poll.

response:dict = {}

polling_active: bool = True

while polling_active:
    name = input("What's' your name? ")
    place = input("could visit one place in the world, where would you go? ")

    response[name] = place

    repeat:str = input("would you like to let someone response? (yes/ no)")
    if repeat.lower() == "yes":
        polling_active = False

print("\n Result")
for name, place in response.items():
    print(f"{name} would you like to visit {place}")

    