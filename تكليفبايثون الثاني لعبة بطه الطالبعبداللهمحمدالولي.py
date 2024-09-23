
import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"
    
    def get_value(self):
        return Card.values.index(self.value)

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.deal())

    def play_card(self):
        return self.hand.pop(0)

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def __str__(self):
        return f"{self.name} has {len(self.hand)} cards"

def play_war_game():
    deck = Deck()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    
    while len(deck.cards) > 0:
        player1.draw(deck)
        player2.draw(deck)

    round_counter = 0
    while player1.hand and player2.hand:
        round_counter += 1
        print(f"\nRound {round_counter}")

        card1 = player1.play_card()
        card2 = player2.play_card()

        print(f"{player1.name} plays {card1}")
        print(f"{player2.name} plays {card2}")

        if card1.get_value() > card2.get_value():
            print(f"{player1.name} wins the round")
            player1.receive_cards([card1, card2])
        elif card1.get_value() < card2.get_value():
            print(f"{player2.name} wins the round")
            player2.receive_cards([card1, card2])
        else:
            print("War!")
            
            if len(player1.hand) < 4 or len(player2.hand) < 4:
                break  
            cards_at_war = [card1, card2]
            for _ in range(3):  
                cards_at_war.append(player1.play_card())
                cards_at_war.append(player2.play_card())
            war_card1 = player1.play_card()
            war_card2 = player2.play_card()
            print(f"{player1.name} plays {war_card1} for war")
            print(f"{player2.name} plays {war_card2} for war")
            if war_card1.get_value() > war_card2.get_value():
                player1.receive_cards(cards_at_war + [war_card1, war_card2])
            elif war_card1.get_value() < war_card2.get_value():
                player2.receive_cards(cards_at_war + [war_card1, war_card2])
            else:
                player1.receive_cards(cards_at_war + [war_card1])
                player2.receive_cards([war_card2])  

    # Determine the winner
    if len(player1.hand) > len(player2.hand):
        print("\nPlayer 1 wins the game!")
    elif len(player1.hand) < len(player2.hand):
        print("\nPlayer 2 wins the game!")
    else:
        print("\nThe game is a draw!")

if __name__ == "__main__":
    play_war_game