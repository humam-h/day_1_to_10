#Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#buy= random.choice(names)
#print(f" {buy} is going to buy the meal today!")
people_num = len(names)
buyer = random.randint(0, people_num - 1)
print(names[buyer] + " is going to buy the meal today!")

