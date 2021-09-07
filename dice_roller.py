import random
def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  sum_dice = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    sum_dice += roll
    print(f'----- dice: {i+1} -------')
    if roll == 1: print(f'You rolled a die {roll} !Critical Fail')
    elif roll == 6: print(f'You rolled a {roll}! Critical Success!')  
    else: print(f'You rolled a {roll}')
    
  print(f'You have rolled a total of {sum_dice}')

if __name__== "__main__":
  main()