import random
import re


def simple_roll(die, times):
    '''
    list[die]: list with the numbers that will display the die
    int[times]: number of rolls to perform in the given list
    '''
    result = choice(die, k=times)
    return result


def effect_roll(str_input):
    values = re.findall(r'\d*', str_input)
    values = [x for x in values if x != '']
    dice_roll = simple_roll(xrange(1, int(values[1]) + 1), int(values[0]))
    result = sum(dice_roll)
    if '+' in str_input:
        result += int(values[-1])
    elif '-' in str_input:
        result -= int(values[-1])
    return result, dice_roll


def main():
    '''This regex will give the pattern for the rolls'''
    effect_roll_rx = re.compile('^\d+\s*[d|D]{1}\s*\d+\s*([+]?|[-]?){1}\s*\d+$')
    simple_roll_rx = re.compile('^\d+\s*[d|D]{1}\s*\d+$')
    while True:
        raw_roll = raw_input('What you want to roll?  ')
        if simple_roll_rx.match(raw_roll):
            to_roll = raw_roll.split('d')
            print simple_roll(xrange(1, int(to_roll[1]) + 1),
                              int(to_roll[0]))
        elif effect_roll_rx.match(raw_roll):
            print effect_roll(raw_roll)
        else:
            print "There was an error with the input, please check:  " + raw_roll


main()
