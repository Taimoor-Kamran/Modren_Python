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


