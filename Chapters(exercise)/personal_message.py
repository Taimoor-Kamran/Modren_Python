# 2-3. Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

name : str = "Eric"

# print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.

person_name: str = "dr apj abdul kalam"
# print(person_name.upper())
# print(person_name.title())
# print(person_name.lower())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never
# tried anything new.”

author:str = "Albert Einstein"
quote: str = "A person who never made a mistake never"

# print(f"{author} once said, {quote}")


# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous

# person’s name using a variable called famous_person. Then compose your mes-
# sage and represent it with a new variable called message. Print your message.

famous_person: str = "Albert Einstein"

message: str = f"{famous_person} once said, A person who never made a mistake never tired anything new."

# print(message)

# 2-7. Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

# famous_person1 : str = "\t  Albert Einstein   \n"

# print(repr(famous_person1))

# print(repr(famous_person1.lstrip())) 
# print(repr(famous_person1.rstrip()))
# print(repr(famous_person1.strip()))

