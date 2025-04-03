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