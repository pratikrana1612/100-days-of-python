# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# Function with no input
def greet():
    print("To do 1")
    print("To do 2")
    print("To do 3")


greet()


# Function with one input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"What are you doing {name}")


greet_with_name("Pratik")


# function with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Your location is {location} right")


# greet_with("pratik","Ahmedabad")
greet_with(location="Ahmedabad", name="Pratik")
