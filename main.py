import random 


def roll(die, times):
    '''
    list[die]: list with the numbers that will display the die
    int[times]: number of rolls to perform in the given list
    '''
    result = []
    for i in xrange(times):
        roll = random.choice(die)
        result.append(roll)
    return result


def main():
    while True:
        raw_roll = raw_input('What you want to roll?  ')
        to_roll = raw_roll.split('d')
        print roll(xrange(1, int(to_roll[1]) + 1),
                   int(to_roll[0]))


main()
