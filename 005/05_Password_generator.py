#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
l1_password = ""
for l in range(nr_letters):
    pl = random.choice(letters)
    l1_password += pl
    #print(pl, end="")
for n in range(nr_numbers):
    pn = random.choice(numbers)
    l1_password += pn
    #print(pn, end="")
for s in range(nr_symbols):
    ps = random.choice(symbols)
    l1_password += ps
    #print(ps, end="")
print(f" your levle one password: {l1_password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
l2_password = []
for l2 in range(nr_letters):
    pl2 = random.choice(letters)
    l2_password.append(pl2)
    #print(pl2, end="")
for n2 in range(nr_numbers):
    pn2 = random.choice(numbers)
    l2_password.append(pn2)
    #print(pn2, end="")
for s2 in range(nr_symbols):
    ps2 = random.choice(symbols)
    l2_password.append(ps2)
    #print(ps2, end="")
random.shuffle(l2_password)
print(f' your levle two password: {"".join(l2_password)}')