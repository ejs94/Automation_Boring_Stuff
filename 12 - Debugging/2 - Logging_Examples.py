import logging
"""
Log Levels:
debug(lowest)
info
warning
error
critical(highest)
"""

logging.basicConfig(filename='12 - Debugging\\2 - myProgramLog.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)  # Disable all log critical or lower

logging.debug('Start of program')


def factorial(n):
    logging.debug(f'Start of factorial {n}')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.debug(f'return value is {total}')
    return total


print(factorial(5))

logging.debug('End of program')
