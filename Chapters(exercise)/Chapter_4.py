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

print("\nAnimals Names\n")
for animal in animals:
    print(animal)

# Modify your program to print a statement about each animal, such as A
# dog would make a great pet.

# Add a line at the end of your program, stating what these animals have in
# common. You could print a sentence, such as Any of these animals would
# make a great pet!

for animal in animals:
    print(f"A {animal.lower()} would like make a great pet.")

print("\nAny of these animals would make a great pet!")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.

for count in range(1, 21):
    print(count)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing CTRL-C or by closing the output window.)

numbers = list(range(1, 1_000_001))

# The underscore (_) is just a readability feature in Python

# for number in numbers:
#     print(number) 

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and
# then use min() and max() to make sure your list actually starts at one and ends
# at one million. Also, use the sum() function to see how quickly Python can add
# a million numbers.

numbers = list(range(1, 1000001))

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = list(range(1, 21, 2))

for odd_number in odd_numbers:
    print(odd_number)

# Even Numbers

even_numbers = list(range(0, 21, 2))

for even_number in even_numbers:
    print(even_number)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
# print the numbers in your list.

threes = list(range(3, 31, 3))

for three in threes:
    print(three)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubes:list[int] = [num**3 for num in range(1, 11)]

for cube in cubes:
    print(cube)

# second method

cubes = []  

for num in range(1, 11):
    cube = num ** 3  
    cubes.append(cube) 

for cube in cubes:  
    print(cube)  


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes:list[int] = [num**3 for num in range(1 ,11)]
print("Cubes",cubes)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to
# print the last three items in the list.

cubes:list[int] = [num**3 for num in range(1, 11)]

print("The first three items in the list are:", cubes[:3])
print("Three items from the middle of the list are:", cubes[3:6])
print("The last three items in the list are:", cubes[-3:])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
# following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.

# • Prove that you have two separate lists. Print the message My favorite piz-
# zas are:, and then use a for loop to print the first list. Print the message My

# friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.

my_pizzas:list[str] = ["pepperoni", "Greek Pizza", "Cheese pizza"]

friend_pizza = my_pizzas[:]

my_pizzas.append("Fajita")
friend_pizza.append("BBQ Chicken")

print("My favorite pizzas are:")

for pizza in my_pizzas:
    print(pizza)

print("\nfriend’s favorite pizzas are:")

for friend in friend_pizza:
    print(friend)

# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing, to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

my_foods:list[str] = ["mango", "banana", "kiwi"]

friend_foods = my_foods[:]

my_foods.append("orange")
friend_foods.append("watermelon")

print("\nmy favorite fruits are:")

for food in my_foods:
    print(food)

print("\nfirend' favorite fruits are:")

for friend_food in friend_foods:
    print(friend_food)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.


buffet_style:tuple = ("banana", "orange", "kiwi", "watermelon", "apple")

print("\nOrignal Buffet menu:\n")

for food in buffet_style:
    print(food)

# • Try to modify one of the items, and make sure that Python rejects the
# change.

