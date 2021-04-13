import random

all_cards = ["ダイヤ の A", "ダイヤ の 2", "ダイヤ の 3", "ダイヤ の 4",
             "ダイヤ の 5", "ダイヤ の 6", "ダイヤ の 7", "ダイヤ の 8",
             "ダイヤ の 9", "ダイヤ の 10", "ダイヤ の J", "ダイヤ の Q", "ダイヤの K",
             "ハート の A", "ハート の 2", "ハート の 3", "ハート の 4",
             "ハート の 5", "ハート の 6", "ハート の 7", "ハート の 8",
             "ハート の 9", "ハート の 10", "ハート の J", "ハート の Q", "ハート の K",
             "スペード の A", "スペード の 2", "スペード の 3", "スペード の 4",
             "スペード の 5", "スペード の 6", "スペード の 7", "スペード の 8",
             "スペード の 9", "スペード の 10", "スペード の J", "スペード の Q", "スペード の K",
             "クローバー の A", "クローバー の 2", "クローバー の 3", "クローバー の 4",
             "クローバー の 5", "クローバー の 6", "クローバー の 7", "クローバー の 8",
             "クローバー の 9", "クローバー の 10", "クローバー の J", "クローバー の Q", "クローバー の K"
             ]
check_numbers1 = [" 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9"]
check_numbers2 = ["10", " J", " Q", " K"]
check_numbers3 = ["A"]
player_total = 0
dealer_total = 0
dealer_second_card = ""

for i in range(2):
    player_card = random.choice(all_cards)
    print(f"プレイヤーが引いたカードは{player_card}です")
    all_cards.remove(player_card)

    if player_card[-2:] in check_numbers1:
        player_total += int(player_card[-2:])
    if player_card[-2:] in check_numbers2:
        player_total += 10
    if player_card[-2:] in check_numbers3:
        player_total += 1

for i in range(2):
    dealer_card = random.choice(all_cards)
    if i == 1:
        dealer_second_card = dealer_card
        print(f"ディーラーが{i + 1}枚目に引いたカードは不明です")
    else:
        print(f"ディーラーが引いたカードは{dealer_card}です")
    all_cards.remove(dealer_card)

    if dealer_card[-2:] in check_numbers1:
        dealer_total += int(dealer_card[-2:])
    if dealer_card[-2:] in check_numbers2:
        dealer_total += 10
    if dealer_card[-2:] in check_numbers3:
        dealer_total += 1

print(f"あなたの現在の得点は{player_total}です")

while True:
    answer = input("カードを引きますか？引く場合はY、やめる場合はNを入力してください")

    if answer == "Y":
        player_card = random.choice(all_cards)
        print(f"プレイヤーが引いたカードは{player_card}です")
        all_cards.remove(player_card)

        if player_card[-2:] in check_numbers1:
            player_total += int(player_card[-2:])
        if player_card[-2:] in check_numbers2:
            player_total += 10
        if player_card[-2:] in check_numbers3:
            player_total += 1

        print(f"あなたの現在の得点は{player_total}です")

        if player_total >= 22:
            print(f"あなたの得点は{player_total}です")
            print(f"ディーラーの得点は{dealer_total}です")
            print("あなたの負けです！")
            print("ブラックジャックまた遊んでね！")
    else:
        break

print(f"ディーラーの2枚目のカードは{dealer_second_card}でした")
print(f"ディーラーの現在の得点は{dealer_total}です")

while True:
    
    if  dealer_total < 17:
        dealer_card = random.choice(all_cards)
        print(f"ディーラーが引いたカードは{dealer_card}です")
        all_cards.remove(dealer_card)

        if dealer_card[-2:] in check_numbers1:
            dealer_total += int(dealer_card[-2:])
        if dealer_card[-2:] in check_numbers2:
            dealer_total += 10
        if dealer_card[-2:] in check_numbers3:
            dealer_total += 1
        
        if dealer_total >= 22:
            print(f"あなたの得点は{player_total}です")
            print(f"ディーラーの得点は{dealer_total}です")
            print("あなたの勝ちです！")
            print("ブラックジャックまた遊んでね！")
            exit()
    else:
        if dealer_total >= 22:
            print(f"あなたの得点は{player_total}です")
            print(f"ディーラーの得点は{dealer_total}です")
            print("あなたの勝ちです！")
            print("ブラックジャックまた遊んでね！")
            exit()
        break

print(f"あなたの得点は{player_total}です")
print(f"ディーラーの得点は{dealer_total}です")

if player_total > dealer_total:
    print("あなたの勝ちです！")
    print("ブラックジャックまた遊んでね！")
    exit()
elif player_total < dealer_total:
    print("あなたの負けです！")
    print("ブラックジャックまた遊んでね！")
    exit()
else:
    print("引き分けです！")
    print("ブラックジャックまた遊んでね！")
    exit()

    
