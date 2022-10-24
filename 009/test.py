import art
print(art.logo)
print(" Welcome to the scret auction program.")
bidders = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid} $")
while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    bidders[name] = bid
    restart = input("Are there any bidders? type 'yes' or 'no'").lower()
    if restart == "no":
        bidding_finished = True
        highest_bidder(bidders)
        
    else:
        bidding_finished = False
