# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of

# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.

# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine_type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} now is open.")

my_restaurant:Restaurant = Restaurant("Tasty Bites", "Italian")

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

class Restaurent:
    def __init__(self, restaureant_name: str, cuisine_type: str):
        self.restaureant_name = restaureant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaureant_name}")
        print(f"Cuisine_type: {self.cuisine_type}")


my_restaurant1: Restaurant = Restaurant("Tasty Bites", "Italian")
my_restaurant2: Restaurant = Restaurant("Spice Hub", "Indian")
my_restaurant3: Restaurant = Restaurant("Sushi World", "Japanese")

my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.

# Create several instances representing different users, and call both meth-
# ods for each user.

class User:
    def __init__(self, first_name: str, last_name: str, age: int, location: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"age: {self.age}")
        print(f"location: {self.location}")
        print(f"email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome Back.")

user1: User = User("Taimoor", "Kamran", 18, "Karachi", "muhammadtaimoor2006@gmail.com")
user2: User = User("AbdulRehman", "Shahid", 19, "Karachi", "rehman444@gmail.com")
user3: User = User("Ahmed", "Tariq", 18, "Karachi", "ahmedx@gmail.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.


# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.

# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day of
# business.

class Restaurent:
    def __init__(self, restaurent_name:str, cuisine_type:str):
        self.restaurent_name = restaurent_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurent_name}")
        print(f"Cuisine_type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurent_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers


restaurant = Restaurent("Tasty Bites", "Italian")

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 25
print(f"Updated customers served: {restaurant.number_served}")


restaurant.set_number_served(100)
print(f"Set number served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"After increment, total customers served: {restaurant.restaurent_name}")

# 9-5. Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name        
        self.last_name = last_name        
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


m1 = User("Taimoor", "Kamran", 0)

m1.increment_login_attempts()
m1.increment_login_attempts()
m1.increment_login_attempts()

print("Login attempts", m1.login_attempts)

m1.reset_login_attempts()

print("Login attempts after reset", m1.login_attempts)

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self, name: str, cuisine_type: str) -> None:
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name}" )
        print(f"Restaurant Type: {self.cuisine_type}")

    
    def open_restaurent(self):
        print(f"{self.name} is now open.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="IceCream"):
        super().__init__(name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mango"]

    def display_restaurent(self):
        print(f"IceCream Flavors available is {self.name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

stand = IceCreamStand("cool cones")
stand.describe_restaurant()
stand.display_restaurent()

# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

class User:
    def __init__(self, first_name: str, last_name: str, login_attemps: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attemps

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")

    def greets(self):
        print(f'Hello, {self.first_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, login_attempts=0):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin Privilleges for {self.first_name} {self.last_name}:")
        for privillege in self.privileges:
            print(f"- {privillege}")

admin_user: Admin = Admin("Taimoor", "Kamran")
admin_user.describe_user()
admin_user.show_privileges()


# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.


class User:
    def __init__(self, first_name: str, last_name: str, login_attemps: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attemps

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")

    def greets(self):
        print(f'Hello, {self.first_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
class Admin(User):
    def __init__(self, first_name, last_name, login_attemps=0):
        super().__init__(first_name, last_name, login_attemps)
        self.privileges = Privileges()

admin_user: Admin = Admin("Taimoor" ,"Kamran")
admin_user.describe_user()
admin_user.privileges.show_privileges()

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 65 if it isn’t already. Make
# an electric car with a default battery size, call get_range() once, and then
# call get_range() a second time after upgrading the battery. You should see an
# increase in the car’s range.

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWH battery.")


    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print(f"Battery upgrade to 65 KWH.")
        else:
            print(f"Battery is already as 65 KWH or higher.")
        
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def describe_car(self):
        print(f"{self.make} {self.model} {self.year}")

class ElectircCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_ecar: ElectircCar = ElectircCar("Tesla", "Model 3", 2024)
my_ecar.describe_car()
my_ecar.battery.get_range()

my_ecar.battery.upgrade_battery()
my_ecar.battery.get_range()


# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod-
# ule. Make a separate file that imports Restaurant. Make a Restaurant instance,

# and call one of Restaurant’s methods to show that the import statement is work-
# ing properly.

from restaurant import Restaurant

my_restaurant: Restaurant = Restaurant("Tasty Bites", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurent()

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
# the classes User, Privileges, and Admin in one module. Create a separate file,
# make an Admin instance, and call show_privileges() to show that everything is
# working correctly.

from user_module import Admin

user_admin: Admin = Admin("Taimoor", "Kamran")
user_admin.describe_user()
user_admin.privileges.show_privileges()

# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.

# run main.py

# 9-13. Dice: Make a class Die with one attribute called sides, which has a

# default value of 6. Write a method called roll_die() that prints a random num-
# ber between 1 and the number of sides the die has. Make a 6-sided die and

# roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times..

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return random.randint(1, self.sides)


print("Rolling a 6-sided die:")
six_sided = Die(6)
for _ in range(10):
    print(six_sided.roll_die())

print("\nRolling a 10-sided die:")
ten_sided = Die(10)
for _ in range(10):
    print(ten_sided.roll_die())

print("\nRolling a 20-sided die:")
twenty_sided = Die(20)
for _ in range(10):
    print(twenty_sided.roll_die())

# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list and print a message saying that
# any ticket matching these 4 numbers or letters wins a prize.

Lottery = [1,2,3,4,5,6,7,8,9,10,"A","B","C","D","E"]

winning_ticket = random.sample(Lottery, 5)

print("any ticket matching these 4 numbers or letters wins a prize")
print("Winning ticket:", winning_ticket)

