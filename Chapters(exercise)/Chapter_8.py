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

def city_country(city, country):
    return f"{city}, {country}"


city_country("Karachi" ,"Pakistan")
city_country("Tokyo" ,"Japan")
city_country("California" ,"USA")

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title, number_of_songs=None):
    album:dict[str,str, int] = {
        "artist": artist_name,
        "title" : album_title,
    }

    if number_of_songs:
        album["songs"] = number_of_songs
    return album

album1 = make_album("Atif Aslam", "Doorie")
album2 = make_album("Arijit Singh", "Soulful voice")
album3 = make_album("KK", "Tujha sochta hun", 12)

print(album1)
print(album2)
print(album3)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title):
    album = {
        "artist" : artist_name,
        "album" : album_title,
    }
    return album

while True:
    print("Enter 'quit' at any time to exit.")
    
    artist = input("Enter your favourite artist:")
    if artist.lower() == 'quit':
        break

    title = input("Enter your favourite album tilte:")
    if title.lower() == 'quit':
        break

    album = make_album(artist, title)
    print("Album info:", album)

# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

def show_message(messages):
    for message in messages:
        print(message)

text_message:list[str] = [
    "How are you",
    "How was your day going so far so good",
    "what's your plan for weekend",
    "And what about work",
    "And what about assignment"
]

show_message(text_message)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

def send_message(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message", {current_message})
        sent_messages.append(current_message)

text_message:list[str] = [
    "How are you",
    "How was your day going so far so good",
    "what's your plan for weekend",
    "And what about work",
    "And what about assignment"
]

sent_messages:list[str] = []

send_message(text_message, sent_messages)

print(f"\nOrignal message list ('should be empty now:'), {text_message}")
print(f"\nSent message list , {sent_messages}")

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func-
# tion send_messages() with a copy of the list of messages. After calling the func-
# tion, print both of your lists to show that the original list has retained its messages.


def send_message(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message", {current_message})
        sent_messages.append(current_message)

text_message:list[str] = [
    "How are you",
    "How was your day going so far so good",
    "what's your plan for weekend",
    "And what about work",
    "And what about assignment"
]

sent_messages:list[str] = []

send_message(text_message[:], sent_messages)

print(f"\nOrignal message list ('should be empty now:'), {text_message}")
print(f"\nSent message list , {sent_messages}")

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many

# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.

def sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!\n")

# Calling the function with different number of arguments
sandwich('cheese', 'tomato', 'lettuce')
sandwich('chicken', 'mayo')
sandwich('beef', 'onion', 'mustard', 'pickles')

# 8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a
# profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.

def build_profile(first_name, last_name, **user_info):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile("Taimoor", "Kamran",age = 18, city = "Karachi", goal = "Become a programmer")

print(my_profile)


# 8-14. Cars: Write a function that stores information about a car in a diction-
# ary. The function should always receive a manufacturer and a model name. It

# should then accept an arbitrary number of keyword arguments. Call the func-
# tion with the required information and two other name-value pairs, such as a

# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def make_info(manufacture , model, **car_info):
    cars = {}
    cars ['manufacture'] = manufacture
    cars ['model'] = model
    for key, value in car_info.items():
        cars[key] = value
    return cars

my_car = make_info("subaru", "outback", color="blue", two_package=True)

print(my_car)

# 8-15. Printing Models: Put the functions for the example printing_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of printing_models.py, and modify the file to use the imported functions.



# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *



# 8-17. Styling Functions: Choose any three programs you wrote for this chapter,
# and make sure they follow the styling guidelines described in this section.