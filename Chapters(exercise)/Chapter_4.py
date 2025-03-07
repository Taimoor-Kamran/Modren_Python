# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should

# have one line of output containing a simple statement like I like pep-
# peroni pizza.

pizzas:list[str] = ["pepperoni", "Greek Pizza", "Cheese pizza"]

print("Pizza Names:")

for pizza in pizzas:
    print(pizza)

print("\nPizza Preferences:")

for pizza in pizzas:
    print(f"I Like {pizza} pizza." )