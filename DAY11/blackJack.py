import random

# Initialize the cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def blackjack_game():
    def player_turn(player_cards, bot_cards):
        total = sum(player_cards)
        print(f"Your cards: {player_cards}, total: {total}")
        print(f"The dealer's visible card: {bot_cards[0]}")

        if total == 21:
            print("BlackJack! You won!")
            return total, True

        while True:
            choice = input(f"Your total is {total}. Do you want to hit ('h') or stand ('s')? ").lower()
            if choice == 's':
                print(f"You chose to stand. Final cards: {player_cards}, total: {total}")
                return total, False
            elif choice == 'h':
                new_card = random.choice(cards)
                player_cards.append(new_card)
                total = sum(player_cards)
                print(f"You drew {new_card}. Your cards are now {player_cards}, total: {total}")

                if total == 21:
                    print("BlackJack! You won!")
                    return total, True
                elif total > 21:
                    print("Bust! You went over 21.")
                    return total, False
            else:
                print("Invalid input. Please type 'h' to hit or 's' to stand.")

    def dealer_turn(bot_cards):
        total = sum(bot_cards)

        print(f"The dealer's initial cards: {bot_cards}, total: {total}")

        if total == 21:
            print("Dealer has a BlackJack and wins!")
            return total

        while total < 17:
            new_card = random.choice(cards)
            bot_cards.append(new_card)
            total = sum(bot_cards)
            print(f"Dealer drew {new_card}. Dealer's cards are now {bot_cards}, total: {total}")

            if total > 21:
                print(f"Dealer went over 21. Dealer's cards: {bot_cards}, total: {total}")
                return total

        print(f"Dealer stands with cards: {bot_cards}, total: {total}")
        return total

    print("Welcome to Blackjack!")

    player_cards = random.choices(cards, k=2)
    bot_cards = [random.choice(cards)]  # Dealer gets one card

    player_total, player_blackjack = player_turn(player_cards, bot_cards)
    if player_blackjack:
        return

    if player_total > 21:
        print("You lost because you went over 21.")
        return

    bot_cards.append(random.choice(cards))
    dealer_total = dealer_turn(bot_cards)

    if dealer_total > 21:
        print("Dealer busts! You win!")
    elif dealer_total == 21:
        print("Dealer wins with a BlackJack!")
    else:
        if player_total > dealer_total:
            print(f"You win! Your total: {player_total}, Dealer's total: {dealer_total}")
        elif player_total < dealer_total:
            print(f"You lose! Your total: {player_total}, Dealer's total: {dealer_total}")
        else:
            print(f"It's a tie! Both you and the dealer have {player_total}.")

blackjack_game()
