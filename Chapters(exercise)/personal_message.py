# 2-3. Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

name : str = "Eric"

print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.

person_name: str = "dr apj abdul kalam"
print(person_name.upper())
print(person_name.title())
print(person_name.lower())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never
# tried anything new.”

author:str = "Albert Einstein"
quote: str = "A person who never made a mistake never"

print(f"{author} once said, {quote}")


# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous

# person’s name using a variable called famous_person. Then compose your mes-
# sage and represent it with a new variable called message. Print your message.

famous_person: str = "Albert Einstein"

message: str = f"{famous_person} once said, A person who never made a mistake never tired anything new."

print(message)

# 2-7. Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

famous_person1 : str = "\t  Albert Einstein   \n"

print(repr(famous_person1))

print(repr(famous_person1.lstrip())) 
print(repr(famous_person1.rstrip()))
print(repr(famous_person1.strip()))

# 2-8. File Extensions: Python has a removesuffix() method that works exactly
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called
# filename. Then use the removesuffix() method to display the filename without
# the file extension, like some file browsers do.

file_name:str = "python_notes.txt"

name_without_extension: str = file_name.removesuffix("txt")

print(name_without_extension)

# 2-9. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your operations
# in print() calls to see the results. You should create four lines that look like this:

print(5 + 3)
print(10 - 2)
print(2 * 4)
print(16 / 2)

# 2-10. Favorite Number: Use a variable to represent your favorite number. Then,
# using that variable, create a message that reveals your favorite number. Print
# that message.

favorite_number: int = 5

message: str = f"this is my favorite number {favorite_number}"

print(message)

# 2-11. Adding Comments: Choose two of the programs you’ve written, and
# add at least one comment to each. If you don’t have anything specific to write
# because your programs are too simple at this point, just add your name and the
# current date at the top of each program file. Then write one sentence describing
# what the program does.

# Author: str = "Taimoor Kamran"
# Date = 22-Feb-2025

# print(Author)
# print(Date)

# 2-12. Zen of Python: Enter import this into a Python terminal session and skim
# through the additional principles.

# he Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# >>>

