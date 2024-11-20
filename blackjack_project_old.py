import random

from card_print import cards_art, cards_index

def random_cards():
    cards = {
        "A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
        "9": 9, "J": 10, "Q": 10, "K": 10     
    }

    card = random.choice(list(cards.items()))
    return card

def change_score(calculate):

    if sum(calculate.values()) > 21 and "A" in calculate.keys():
        calculate.update({"A": 1})

    return sum(calculate.values())

def game():
    
    while True:
    
        choice =  input("Play a game of Blackjack? Type 'y' or 'n': ")
        if choice == "y":

            player_total_cards = []
            dealer_total_cards = []

            count_player_card = 0
            count_dealer_card = 0

            player_score = 0
            dealer_score = 0

            for x in range(2):
                player_total_cards.append(random_cards())
                dealer_total_cards.append(random_cards())

            game_over = False
            stand = False
            while not stand:
                player_cards_dict = dict(player_total_cards)           
                count_player_card = len(player_cards_dict)
                player_score = change_score(player_cards_dict)
                

                print(f"Your Cards: {list(player_cards_dict.keys())}")

                for x in range(count_player_card):
                    print(cards_art[cards_index.index(player_total_cards[x][0])])

                print(f"Your Current Score: {player_score}")
                print(f"Dealer Card: {dealer_total_cards[0][0]}")
                print(cards_art[cards_index.index(dealer_total_cards[0][0])])
                

                if player_score == 21 and count_player_card == 2:
                    print("Player Win ! BlackJack ")
                    game_over = True
                    break

                if dealer_score == 21 and count_dealer_card == 2:
                    print(f"Dealer Card: {list(dealer_cards_dict.keys())}")
                    print("Dealer Win ! BlackJack ")  
                    game_over = True
                    break
                
                hit_or_stand = input("Do you want to draw the card: type hit or stand:").lower()
                if hit_or_stand == "hit":
                    player_total_cards.append(random_cards())
                if hit_or_stand == "stand":
                    break

            
            while not game_over:
                dealer_cards_dict = dict(dealer_total_cards)
                count_dealer_card = len(dealer_cards_dict)

                if dealer_score < 17:
                    dealer_total_cards.append(random_cards())
                    dealer_score = change_score(dealer_cards_dict)

                if dealer_score >= 17:
                    print(f"Dealer Card: {list(dealer_cards_dict.keys())}")
                    for x in range(count_dealer_card):
                        print(cards_art[cards_index.index(dealer_total_cards[x][0])])
                    game_over = True    

                
            print(f"Your Score {player_score}")
            print(f"dealer Score {dealer_score}")
            if player_score == dealer_score:
                print ("******** Draw ********** ")
            elif player_score > dealer_score and player_score <= 21:
                print("******* Player Win! **********")
            elif player_score < dealer_score and dealer_score <= 21:
                print("******* You lose *********")
            elif player_score > 21 and dealer_score > 21:
                print("***** draw *********")


        if choice == "n":
            print("goodbye")
            break

game()