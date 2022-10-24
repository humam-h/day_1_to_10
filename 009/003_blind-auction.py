import os
import art
print(art.logo)
print(" Welcome to the scret auction program.")
#blind_auction = []   
reboot = True
new_bidder = {}
while reboot:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    def add_bidder(name, bid):
        new_bidder[name] = bid
    add_bidder(name, bid)
    
    restart = input("Are there any bidders? type 'yes' or 'no'").lower()
    if restart == "no":
        print(max([new_bidder]))
        reboot =False
    else:
        reboot = True
