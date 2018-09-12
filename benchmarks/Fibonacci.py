from algorithms import Fibonacci
from utils import TimeCalculator as timer

def test():
    print('Fibonacci methods \n')

    start = timer.start()
    print('Fibonacci - recursive basic method:', Fibonacci.basic_calc(30))
    print('duration in miliseconds: ', timer.calcTime(start), '\n')

    start = timer.start()
    print('Fibonacci - recursive memoize method:', Fibonacci.memoize_calc(30))
    print('duration in miliseconds: ', timer.calcTime(start), '\n')

    start = timer.start()
    print('Fibonacci - bottom_up method:', Fibonacci.bottom_up_calc(30))
    print('duration in miliseconds: ', timer.calcTime(start), '\n')
