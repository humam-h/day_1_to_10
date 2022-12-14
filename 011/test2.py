import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
user_cards = []
computer_cards = []
is_game_over = False
for deal in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards is:{user_cards}, your current score is:{user_score}")
    print(f" Computer first card is:{computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
        print("GameOver")
    else:
        another_card = input("Type 'y' if you want to draw another card, type 'n' to end the game\n")
        if another_card == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(user_cards)
        else:
            is_game_over = True
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)