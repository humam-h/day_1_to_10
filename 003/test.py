# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    bell = 15
    if add_pepperoni == "Y":
        bell += 2
        if extra_cheese == "Y":
            bell += 1
            print(f"your final bell is {bell} $")
        else:
            bell -= 1
            print(f"your final bell is {bell} $")
    else:
        bell -= 2
        print(f"your final bell is {bell} $")
#else:
#    print(f"your final bell is {bell} $")
elif size == "M":
    bell = 20
    if add_pepperoni == "Y":
        bell += 3
        if extra_cheese == "Y":
            bell += 1
            print(f"your final bell is {bell} $")
        else:
            bell -= 1
            print(f"your final bell is {bell} $")
    else:
        bell -= 3
        print(f"your final bell is {bell} $")
#else:
#    print(f"your final bell is {bell} $")
elif size == "L":
    bell = 25
    if add_pepperoni == "Y":
        bell += 3
        if extra_cheese == "Y":
            bell += 1
            print(f"your final bell is {bell} $")
        else:
            bell -= 1
            print(f"your final bell is {bell} $")
    else:
        bell -= 3
        print(f"your final bell is {bell} $")
#else:
#    print(f"your final bell is {bell} $")