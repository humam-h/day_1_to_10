import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)
deal_card()
user_cards = []
computer_cards = []
for deal in range(2):
    #deal_card()
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
def calculate_score(user_cards, computer_cards):
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    if 11 and 10 == user_cards:
        #user_score = 0
        print("GameOver")
        return 0 #user_score
    elif 11 and 10 == computer_cards:
        #computer_score = 0
        print("GameOver")
        return 0 #computer_score
    elif user_score > 21 :
        if 11 in user_score:
            user_cards.remove(11)
            user_cards.append(1)
            user_score = sum(user_cards)
            return user_scor
    elif computer_score > 21:
        if 11 in computer_score:
            computer_cards.remove(11)
            computer_cards.append(1)
            computer_score = sum(computer_cards)
            return computer_score
    elif user_score and computer_score == 0:
        print(f" your score is {user_score} and computer score is {computer_score} game over")
    elif user_score > 21 :
        print(f" your score is {user_score} game over")
    return user_score, computer_score
calculate_score(user_cards, computer_cards)
