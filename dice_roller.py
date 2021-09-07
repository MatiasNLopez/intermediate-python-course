import random
def main():
  dice_rolls = 2
  sum_dice = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, 6)
    sum_dice += roll
    if roll == 1: print(f'You rolled a die {roll} !Critical Fail')
    elif roll == 6: print(f'You rolled a {roll}! Critical Success!')  
    else: print(f'You rolled a {roll}')
    print(f'--------------')
    print(f'You have rolled a total of {sum_dice}')

if __name__== "__main__":
  main()