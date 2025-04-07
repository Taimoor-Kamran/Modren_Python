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