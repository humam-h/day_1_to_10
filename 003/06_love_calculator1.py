# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
l_name1 = name1.lower()
l_name2 = name2.lower()
both_names = l_name1 + l_name2
inside_true = both_names.count("t") + both_names.count("r") + both_names.count("u") + both_names.count("e")
inside_love = both_names.count("l") + both_names.count("o") + both_names.count("v") + both_names.count("e")
result = str(inside_true) + str(inside_love)
love_score = int(result)
if love_score <= 10 and love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

