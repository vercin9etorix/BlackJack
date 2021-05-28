import random
import sys

"""
開発するブラックジャックのルール
・初期カードは52枚。
・引く際にカードの重複は無いようにする
・プレイヤーとディーラーの2人対戦。
・プレイヤーは実行者、ディーラーは自動的に実行
・実行開始時、プレイヤーとディーラーはそれぞれ、カードを2枚引く。
  引いたカードは画面に表示する。ただし、ディーラーの2枚目のカードは分からないようにする
・その後、先にプレイヤーがカードを引く。
  プレイヤーが21を超えていたらバースト、その時点でゲーム終了
・プレイヤーは、カードを引くたびに、次のカードを引くか選択できる
・プレイヤーが引き終えたら、その後ディーラーは、自分の手札が17以上になるまで引き続ける
・プレイヤーとディーラーが引き終えたら勝負。より21に近い方の勝ち
・JとQとKは10として扱う
・Aは「1」として扱う
・ダブルダウンなし、スピリットなし、サレンダーなし、その他特殊そうなルールなし
"""
SUITS = ("spades", "hearts", "diamonds", "clubs")
RANKS = (" A", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10", " J", " Q", " K")
VALUES = {" A": 1, " 2": 2, " 3": 3, " 4": 4, " 5": 5, " 6": 6, " 7": 7, " 8": 8, " 9": 9, "10":10, " J": 10, " Q": 10, " K": 10}

class Card:
  def __init__(self, suit, rank): 
    self.suit = suit
    self.rank = rank

  def __repr__(self):
    return f"{SUITS[self.suit]} -{RANKS[self.rank]}"

class Deck:
  CARDS = [Card(i, j) for i in range(4) for j in range(13)]

  def __init__(self):
    self.cards = random.sample(Deck.CARDS, len(Deck.CARDS))
  
  def next_card(self):
    return self.cards.pop()

class PlayerBase:
  def __init__(self):
    self.scores = 0
    self.hands = []
    self.not_bust = True

  def check_bust(self):
    self.not_bust = False if self.scores > 21 else True
    return self.not_bust

  def draw_card(self, card):
    self.hands.append(card)
    self.scores += VALUES[str(card)[-2:]]
  def show_scores(self):
    return self.scores

class Player(PlayerBase):
  def select_draw(self, card):
    while self.not_bust:
      selection = input("Do you want to draw a card? [yes/no]:\n")

      if selection == "yes":
        self.draw_card(card)
        print(f"\nplayer cards: {self.hands}")
        print(f"player score = {self.scores}")
        self.check_bust()
      elif selection == "no":
        break
      else:
        continue
      
      if not self.not_bust:
        print("YOU BUST!")
        print("YOU LOSE!")
        sys.exit()

class Dealer(PlayerBase):
  def select_draw(self, card):
    while True:
      if self.scores >= 17:
        self.check_bust()
        break
      else:
        self.draw_card(card)
    
    if not self.not_bust:
        print(f"dealer cards: {self.hands}")
        print(f"dealer score = {self.scores}")
        print("DEALER BUST!")
        print("YOU WIN!")
        sys.exit()

class Game:
  def __init__(self):
    self.deck = Deck()
    self.player = Player()
    self.dealer = Dealer()

    
  def play_game(self):
    print("☆ ★ " * 3 + "Welcome to BlackJack！" + "☆ ★ " * 3)
    
    self.player.draw_card(self.deck.next_card())
    self.player.draw_card(self.deck.next_card())
    self.dealer.draw_card(self.deck.next_card())
    self.dealer.draw_card(self.deck.next_card())
    
    print(f"player cards: {self.player.hands}")
    print(f"player score = {self.player.scores}\n")
    print(f"dealer cards: {self.dealer.hands[0]}\n")
    
    self.player.select_draw(self.deck.next_card())
    print(self.player.hands)
    print(f"player score = {self.player.scores}")
    self.dealer.select_draw(self.deck.next_card())

    print(f"dealer cards: {self.dealer.hands}")
    print(f"dealer score = {self.dealer.scores}")

    if self.player.scores > self.dealer.scores:
      print("YOU WIN!")
    elif self.player.scores < self.dealer.scores:
      print("YOU LOSE!")
    else:
      print("DRAW!")

game = Game()
game.play_game()
