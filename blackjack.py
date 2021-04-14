import random

suits = [" ダイヤ ", " ハート ", " スペード ", " クローバー "]
card_numbers1 = [" A"]
card_numbers2 = [" 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9"]
card_numbers3 = ["10", " J", " Q", " K"]
all_cards = [s + "の" + n for s in suits for n in (card_numbers1 + card_numbers2 + card_numbers3)]
player_score = 0
dealer_score = 0
dealer_second_card = ""

def calculate_score(card, score):
    if card[-2:] in card_numbers1:
        score += 1
    if card[-2:] in card_numbers2:
        score += int(card[-2:])
    if card[-2:] in card_numbers3:
        score += 10
    
    return score

def announce_result(result):
    print(f"あなたの得点は{player_score}です")
    print(f"ディーラーの得点は{dealer_score}です")
    if player_score == dealer_score:
        print(f"{result}です！")
    else:
        print(f"あなたの{result}です！")
    print("ブラックジャックまた遊んでね！")
    exit()

def select_card(player):
    card = random.choice(all_cards)
    if player == "player":
        print(f"プレイヤーが引いたカードは{card}です")
    else:
        print(f"ディーラーが引いたカードは{card}です")
    all_cards.remove(card)
    return card

print("☆ ★ " * 3 + "ブラックジャックへようこそ！" + "☆ ★ " * 3)

for i in range(2):
    player_card = select_card("player")
    player_score = calculate_score(player_card, player_score)

for i in range(2):
    dealer_card = random.choice(all_cards)
    if i == 1:
        dealer_second_card = dealer_card
        print(f"ディーラーが{i + 1}枚目に引いたカードは不明です")
    else:
        print(f"ディーラーが引いたカードは{dealer_card}です")
    all_cards.remove(dealer_card)

    dealer_score = calculate_score(dealer_card, dealer_score)

print(f"あなたの現在の得点は{player_score}です")

while True:
    answer = input("カードを引きますか？\n引く場合はY、やめる場合はNを入力してください\n")

    if answer.lower() == "y":
        player_card = select_card("player")
        player_score = calculate_score(player_card, player_score)
        print(f"あなたの現在の得点は{player_score}です")

        if player_score >= 22:
            print(f"ディーラーの2枚目のカードは{dealer_second_card}でした")
            announce_result("負け")
    elif answer.lower() == "n":
        break
    else:
        print("Y または N を入力してください")

print(f"ディーラーの2枚目のカードは{dealer_second_card}でした")
print(f"ディーラーの現在の得点は{dealer_score}です")

while True:
    
    if  dealer_score < 17:
        dealer_card = select_card("dealer")
        dealer_score = calculate_score(dealer_card, dealer_score)
        
        if dealer_score >= 22:
            announce_result("勝ち")
            
    elif 17 <= dealer_score <= 21:
        break
    elif dealer_score >= 22:
        announce_result("勝ち")

if player_score > dealer_score:
    announce_result("勝ち")  
elif player_score < dealer_score:
    announce_result("負け")
else:
    announce_result("引き分け")