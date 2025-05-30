'''
class Restaurant:
   

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("The Fancy Feast", "Italian")

print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nNumber of customers served: {restaurant.number_served}")

restaurant.number_served = 50
print(f"Number of customers served after direct change: {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Number of customers served after using set_number_served(): {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"Number of customers served after incrementing: {restaurant.number_served}")
'''
'''
class User:

    def __init__(self, first_name, last_name, email, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.country = country
        self.login_attempts = 0 

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
        print(f"  Age: {self.age}")
        print(f"  Country: {self.country}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Amit", "Bhowmik", "amit.bhk@example.com", 25, "Dhaka")
user2 = User("Ruhi", "Rashedi", "ruhi.rashedi@example.com", 23, "ctg")
user3 = User("Prema", "Saha", "prema.sa@example.com", 22, "barishal")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

test_user = User("Test", "User", "test.user@example.com", 28, "sylhet")

print(f"\nInitial login attempts for {test_user.first_name}: {test_user.login_attempts}")
test_user.increment_login_attempts()
test_user.increment_login_attempts()
test_user.increment_login_attempts()
print(f"Login attempts after incrementing: {test_user.login_attempts}")

test_user.reset_login_attempts()
print(f"Login attempts after resetting: {test_user.login_attempts}")
'''
'''

'''