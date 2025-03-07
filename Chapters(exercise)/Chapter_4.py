# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should

# have one line of output containing a simple statement like I like pep-
# peroni pizza.

# Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

pizzas:list[str] = ["pepperoni", "Greek Pizza", "Cheese pizza"]

print("Pizza Names:")

for pizza in pizzas:
    print(pizza)

print("\nPizza Preferences:")

for pizza in pizzas:
    print(f"I Like {pizza} pizza." )

print("\nI really love pizza!")


# 4-2. Animals: Think of at least three different animals that have a common char-
# acteristic. Store the names of these animals in a list, and then use a for loop to

# print out the name of each animal.

animals:list[str] = ["Rabbit", "Cat", "Dog"]

print("Animals Names")
for animal in animals:
    print(animal)

for animal in animals:
    print(f"A {animal} would like make a great pet.")