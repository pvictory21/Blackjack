import random

def deal_cards():
    player_cards.extend(random.sample(list(deck.keys()), 2))
    for card in player_cards:
        del deck[card]
  
    dealer_cards.extend(random.sample(list(deck.keys()), 2))
    for card in dealer_cards:
        del deck[card]
      
    player_total = sum(static_deck[card] for card in player_cards)
  
    print('The dealer cards are __ and ' + str(dealer_cards[1]))
    print('Your cards are {} and {} with a total score of {}'.format(player_cards[0], player_cards[1], player_total))

    return player_cards, dealer_cards

print('\nWelcome to the game of Blackjack!\n')


while True:
    chip_count = input('What do you want the buy in to be? ')
    if chip_count.isdigit():
        chip_count = int(chip_count)
        print('\nGood Luck!')
        break
    else:
        print('Invalid input. Please enter a number.')
    continue

while True:
  while True:
    print('Your total chip count is ${}.'.format(chip_count))
    bet = input('How much would you like to bet this round? ')
    if bet.isdigit():
        bet = int(bet)
        if bet <= chip_count:
          break
        else:
          print("\nYou don't have enough chips to bet this amount. Please enter an amount less than or equal to your chip_count.\n")
          continue
    else:
        print('Invalid input. Please enter a number.')
    continue
  
  # Initialize the deck
  suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
  values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
  
  deck = {}
  
  for suit in suits:
      for rank in ranks:
          card = rank + ' of ' + suit
          value = values[rank]
          deck[card] = value

  static_deck = dict(deck)
  
  # Initializing cards
  player_cards = []
  dealer_cards = []
  hidden_card = '__'
  player_hit_card = 1
  dealer_hit_card = 1
  busted = False

  deal_cards()

  player_total = sum(static_deck[card] for card in player_cards)
  dealer_total = sum(static_deck[card] for card in dealer_cards)
  
  while True:
    # Player Actions
    player_action = input('\nWhat would you like to do? You can stay or hit? ')
    if player_action.lower() == 'hit':
      player_hit_card += 1 
      player_cards.extend(random.sample(list(deck.keys()), 1))
      player_total = sum(static_deck[card] for card in player_cards)
      print('You have drawn a ' + player_cards[player_hit_card] + '.')
      print('You now have a total of ' + str(player_total))
      if player_total > 21:
        print('\nYou have busted. The dealer wins!')
        chip_count -= bet
        busted = True
        break
      if player_total < 21:
        continue
      if player_total == 21:
        print('You have a blackjack!')
        break
      continue
    elif player_action.lower() == 'stay':
      print('You have elected to stay.\n')
      print('The dealer has a total of {} with {} and {}.'.format(dealer_total, dealer_cards[0], dealer_cards[1]))

      # Dealer Alg
      if dealer_total > 21:
        print('The dealer has busted. You win!')
        chip_count += bet
        busted = True
        break
      if dealer_total == 21:
        print('The dealer has a blackjack!')
        break
      
      while dealer_total < 18:
        dealer_cards.extend(random.sample(list(deck.keys()), 1))
        dealer_total = sum(static_deck[card] for card in dealer_cards)
        dealer_hit_card += 1
        print('The dealer has elected to hit and has drawn a ' + dealer_cards[dealer_hit_card] + '.')
        print('\nThe dealer now has a total of ' + str(dealer_total))

        if dealer_total > 21:
          print('The dealer has busted. You win!')
          chip_count += bet
          busted = True
        elif dealer_total >= 18:
          print('\nThe dealer has elected to stay')
        elif dealer_total == 21:
          print('The dealer has a blackjack!')

      break
  
    else:
      print('Invalid Input.')
      continue

  # Determining winner
  if busted == True:
    while True:
      end_game = input('\nWould you like to play again? ')
    
      if end_game.lower() == 'yes':
        if chip_count > 0:
          break
        else:
          print("I'm sorry. You have run out of chips to play. You will need to buy in again if you want to play again. Goodbye.")
          exit()
      elif end_game.lower() == 'no':
        print('\nThank you for playing. We hope to see you again soon!')
        exit()
      else:
        print('Invalid input. Please enter yes or no.')
        continue
  else:
    if player_total > dealer_total:
      print('\nYou have won! Congradulations!')
      chip_count += bet
    elif player_total < dealer_total:
      print('\nThe dealer wins! You Lose :(')
      chip_count -= bet
    else:
      print('\nYou both have the same total. This round is a push.')

      # Determining winner
    while True:
      end_game = input('\nWould you like to play again? ')
        
      if end_game.lower() == 'yes':
        if chip_count > 0:
          break
        else:
          print("I'm sorry. You have run out of chips to play. You will need to buy in again if you want to play again. Goodbye.")
          exit()
      elif end_game.lower() == 'no':
        print('\nThank you for playing. We hope to see you again soon!')
        exit()
      else:
        print('Invalid input. Please enter yes or no.')
        continue
