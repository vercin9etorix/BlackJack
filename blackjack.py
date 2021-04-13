import random

suits = [" ダイヤ ", " ハート ", " スペード ", " クローバー "]
card_numbers1 = [" A"]
card_numbers2 = [" 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9"]
card_numbers3 = ["10", " J", " Q", " K"]
all_cards = [s + "の" + n for s in suits for n in (card_numbers1 + card_numbers2 + card_numbers3)]
player_score = 0
dealer_score = 0
dealer_second_card = ""

def calculate_score(card, total):
    if card[-2:] in card_numbers1:
        total += 1
    if card[-2:] in card_numbers2:
        total += int(card[-2:])
    if card[-2:] in card_numbers3:
        total += 10
    
    return total

def result_announce(result):
    print(f"あなたの得点は{player_score}です")
    print(f"ディーラーの得点は{dealer_score}です")
    if player_score == dealer_score:
        print(f"{result}です！")
    else:
        print(f"あなたの{result}です！")
    print("ブラックジャックまた遊んでね！")
    exit()


for i in range(2):
    player_card = random.choice(all_cards)
    print(f"プレイヤーが引いたカードは{player_card}です")
    all_cards.remove(player_card)

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
    answer = input("カードを引きますか？引く場合はY、やめる場合はNを入力してください\n")

    if answer.lower() == "y":
        player_card = random.choice(all_cards)
        print(f"プレイヤーが引いたカードは{player_card}です")
        all_cards.remove(player_card)

        player_score = calculate_score(player_card, player_score)
        print(f"あなたの現在の得点は{player_score}です")
        if player_score >= 22:
            print(f"ディーラーの2枚目のカードは{dealer_second_card}でした")
            result_announce("負け")
    elif answer.lower() == "n":
        break
    else:
        print("Y または N を入力してください")

print(f"ディーラーの2枚目のカードは{dealer_second_card}でした")
print(f"ディーラーの現在の得点は{dealer_score}です")

while True:
    
    if  dealer_score < 17:
        dealer_card = random.choice(all_cards)
        print(f"ディーラーが引いたカードは{dealer_card}です")
        all_cards.remove(dealer_card)

        dealer_score = calculate_score(dealer_card, dealer_score)
        
        if dealer_score >= 22:
            result_announce("勝ち")
    elif 17 <= dealer_score <= 21:
        break
    elif dealer_score >= 22:
        result_announce("勝ち")

if player_score > dealer_score:
    result_announce("勝ち")  
elif player_score < dealer_score:
    result_announce("負け")
else:
    result_announce("引き分け")