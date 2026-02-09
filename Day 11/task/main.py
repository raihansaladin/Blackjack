import random, art

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = {
    "Ace":11,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "Jack":10,
    "Queen":10,
    "King":10,
}

user_cards = []
com_cards = []

def first_play():
    # 2 kartu pertama com dan player
    print(art.logo)
    two_cards_player_1 = random.choice(list(cards.values()))
    two_cards_player_2 = random.choice(list(cards.values()))
    two_cards_com_1 = random.choice(list(cards.values()))
    two_cards_com_2 = random.choice(list(cards.values()))

    # cek apakah kartu 1 dan 2 adalah Ace
    if two_cards_player_1 == cards["Ace"] and two_cards_player_2 == cards["Ace"]:
        two_cards_player_2 = 1
    elif two_cards_com_1 == cards["Ace"] and two_cards_com_2 == cards["Ace"]:
        two_cards_com_2 = 1

    # hasil kartu user ke list
    user_cards.append(two_cards_player_1)
    user_cards.append(two_cards_player_2)
    com_cards.append(two_cards_com_1)
    com_cards.append(two_cards_com_2)
    # --------------------------------

    user_result = sum(user_cards)
    com_result = sum(com_cards)

    print(f"User cards : {user_cards}")
    print(f"Com first cards : {com_cards[0]}")
    print(f"User total: {user_result}")

    # cek apakah user atau com punya blackjack
    if two_cards_player_1 == cards["10"] and two_cards_player_2 == cards["Ace"]:
        print("You have BlackJack!")
    elif two_cards_player_2 == cards["10"] and two_cards_player_1 == cards["Ace"]:
        print("You have BlackJack!")

def ulang_main_coy():
    again = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    again.lower()
    if again == "y":
        user_cards.clear()
        com_cards.clear()
        print("\n" * 25)
        first_play()
    elif again == "n":
        exit()


def main_lagi():
    draw_lagi = True
    while draw_lagi:
        # tambah kartu
            user_result = sum(user_cards)
            messi = True
            while messi:
                draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                draw_another_card.lower()
                add_card = random.choice(list(cards.values()))
                if draw_another_card == "y":
                    if add_card == cards["Ace"]: # jika card random adalah Ace
                        add_card = 1
                    user_cards.append(add_card)


                    user_result = sum(user_cards)
                    print(f"User cards : {user_cards}")
                    print(f"cards total : {user_result}")
                    com_result = sum(com_cards)
                    print(f"Com cards : {com_cards[0]}")

                    if user_result > 21:
                        messi = False

                elif draw_another_card == "n":
                    def com_draw_another_card():
                        com_add_card = random.choice(list(cards.values()))
                        if com_add_card == cards["Ace"]:
                            com_add_card = 1
                        com_cards.append(com_add_card)
                    for com in com_cards:
                        com_result = sum(com_cards)
                        if  com_result < 17:
                            com_draw_another_card()
                    user_result = sum(user_cards)
                    print(f"Your final card {user_cards} = {user_result}")
                    print(f"Com final card {com_cards} = {com_result}")
                    messi = False

            # apakah nilai kartu user lebih dari 21?
            if user_result > 21:
                print("BUST! You Lose!")
                ulang_main_coy()
            elif com_result > 21:
                print("You win! Computer BUST!")
                ulang_main_coy()
            elif user_result > com_result:
                print("You win!")
                ulang_main_coy()
            elif user_result == com_result:
                print("Draw...")
                ulang_main_coy()
            else:
                print("You lose!")
                ulang_main_coy()

first_play()
main_lagi()
