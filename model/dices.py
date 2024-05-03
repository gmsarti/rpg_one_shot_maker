from random import randint

def roll(die:int=6,number_of_dice:int=1) -> int:
    res:int=0
    for i in range(number_of_dice):
        res += randint(1,die)
    return res

if __name__ == '__main__':
    roll(die=10,number_of_dice=3)