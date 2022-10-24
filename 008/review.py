# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hello")
    print("It's a nice day")
    print("All is mine")
greet()
# function with input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"It's a nice day {name}")
    print(f"All is mine {name}")
greet_with_name("Argos")
# function with more than one input
def greet_with(name, location):
    print(f"My name is {name}, and i'm from {location}")
greet_with("ramon", "UK")
#function with keyword argument
def greet_keyword(name="Joe", location="USA"):
    print(f"Hello {name} !")
    print(f"What is it like in {location} ?")
greet_keyword()

