# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bell = 0
if size == "S":
    bell += 15
elif size == "M":
    bell += 20
else:
    bell += 25
if add_pepperoni == "Y":
    if size =="S":
        bell += 2
    else:
        bell += 3
if extra_cheese == "Y":
    bell += 2
    
print(f"your final bell is {bell} $")
