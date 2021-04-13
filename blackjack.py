import random

suits = [" ダイヤ ", " ハート ", " スペード ", " クローバー "]
card_numbers1 = [" A"]
card_numbers2 = [" 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9"]
card_numbers3 = ["10", " J", " Q", " K"]
all_cards = [s + "の" + n for s in suits for n in (card_numbers1 + card_numbers2 + card_numbers3)]
player_total = 0
dealer_total = 0
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
    print(f"あなたの得点は{player_total}です")
    print(f"ディーラーの得点は{dealer_total}です")
    if player_total == dealer_total:
        print(f"{result}です！")
    else:
        print(f"あなたの{result}です！")
    print("ブラックジャックまた遊んでね！")
    exit()


for i in range(2):
    player_card = random.choice(all_cards)
    print(f"プレイヤーが引いたカードは{player_card}です")
    all_cards.remove(player_card)

    player_total = calculate_score(player_card, player_total)

for i in range(2):
    dealer_card = random.choice(all_cards)
    if i == 1:
        dealer_second_card = dealer_card
        print(f"ディーラーが{i + 1}枚目に引いたカードは不明です")
    else:
        print(f"ディーラーが引いたカードは{dealer_card}です")
    all_cards.remove(dealer_card)

    dealer_total = calculate_score(dealer_card, dealer_total)

print(f"あなたの現在の得点は{player_total}です")

while True:
    answer = input("カードを引きますか？引く場合はY、やめる場合はNを入力してください\n")

    if answer.lower() == "y":
        player_card = random.choice(all_cards)
        print(f"プレイヤーが引いたカードは{player_card}です")
        all_cards.remove(player_card)

        player_total = calculate_score(player_card, player_total)

        print(f"あなたの現在の得点は{player_total}です")

        if player_total >= 22:
            print(f"ディーラーの2枚目のカードは{dealer_second_card}でした")
            result_announce("負け")
    elif answer.lower() == "n":
        break
    else:
        print("Y または N を入力してください")

print(f"ディーラーの2枚目のカードは{dealer_second_card}でした")
print(f"ディーラーの現在の得点は{dealer_total}です")

while True:
    
    if  dealer_total < 17:
        dealer_card = random.choice(all_cards)
        print(f"ディーラーが引いたカードは{dealer_card}です")
        all_cards.remove(dealer_card)

        dealer_total = calculate_score(dealer_card, dealer_total)
        
        if dealer_total >= 22:
            result_announce("勝ち")
    else:
        if dealer_total >= 22:
            result_announce("勝ち")
        break

if player_total > dealer_total:
    result_announce("勝ち")  
elif player_total < dealer_total:
    result_announce("負け")
else:
    result_announce("引き分け")
    

    
