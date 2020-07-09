# Remember to use coderunner with VSCode and everything will be fine.
import os
import traceback


try:
    raise Exception('This is the error message.')
except:
    errorFile = open('12 - Debugging\\1 - error log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')


"""
This function create a block like that bellow:
*****************
*               *
*               *
*               *
*****************
"""


def boxPrint(symbol, width, height):

    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string of lenght 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2.')
    print(symbol * width)
    for _ in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


# This it will trigger first exception
boxPrint('++', 1, 1)
# This it will trigger second exception
boxPrint('+', 1, 1)

# Assert example
# assert False, 'This is the error message.'

market_2nd = {'ns': 'green', 'ew': 'red'}


def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), f'Neither light is red!' + \
        str(intersection)


switchLights(market_2nd)
