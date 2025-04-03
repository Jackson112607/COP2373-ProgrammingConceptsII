# This program deals a hand of five poker cards. The user is then prompted to enter in numbers for which cards in the
# hand they'd like to replace. The program then displays the new hand.

# Import the random module.
import random

# Create the full deck of cards.
def create_deck():
  suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
  deck = []
  for suit in suits:
    for rank in ranks:
      deck.append((rank, suit))
  return deck

# Get cards for the user's first Poker hand.
def deal_hand(deck, num_cards):
  hand = []
  for _ in range(num_cards):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
  return hand

# Print the user's first Poker hand.
def print_hand(hand):
  for rank, suit in hand:
    print(f"{rank} of {suit}")

# Replace the cards the user entered with new cards.
def replace_cards(hand, deck, positions):
  for position in positions:
    if 1 <= position <= len(hand):
      card = random.choice(deck)
      hand[position - 1] = card
      deck.remove(card)
  return hand

# Get input from the user and display the output.
def main():
  deck = create_deck()
  hand = deal_hand(deck, 5)

  print("Your hand:")
  print_hand(hand)

  position_input = input("Enter card positions to replace (Ex: 1, 3, 5): ")
  position_str = position_input.split(',')
  positions = []
  for s in position_str:
    if s.strip().isdigit():
      positions.append(int(s.strip()))

  hand = replace_cards(hand, deck, positions)

  print("\nYour new hand:")
  print_hand(hand)

# Call the main function to run the program.
main()