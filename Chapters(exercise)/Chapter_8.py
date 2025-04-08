# 8-1. Message: Write a function called display_message() that prints one sen-
# tence telling everyone what you are learning about in this chapter. Call the

# function, and make sure the message displays correctly.

def display_message():
    print("I'm learning about functions in this chapter.") 

display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(title):
    print(f"One of my favourite books is {title}")

favorite_book("Alice in Wonderland")

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print a
# sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"The shirt size is '{size}' and the message on it says: '{message}'" )


make_shirt("Meduim", "Code like a pool.")
make_shirt(size="Meduim", message="Code like a pool.")


# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size="Large", message="I love python"):
    print(f"The Shirt size is '{size}'and the message on it says: '{message}'")

make_shirt()

make_shirt(size="Medium")

make_shirt(size="Small", message="Never give up.")

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

def describe_city(city, country="United State America" ):
    print(f"such as {city} is in {country}")

describe_city("Texas")
describe_city("Karachi", "Pakistan")
describe_city("Berlin", "Germany")

# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values
# that are returned.

