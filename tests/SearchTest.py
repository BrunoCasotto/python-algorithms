from algorithms import Search
from utils import TimeCalculator as timer

def test():
    print('Search methods \n')

    # put the target into the > 12.000 items
    elements = list(range(1, 35))
    target = 90

    start = timer.start()
    res = Search.basic_linear_search(elements, target)
    print('Search - basic linear method index:', res)
    print('duration in miliseconds: ', timer.calcTime(start), '\n')

    start = timer.start()
    res = Search.recursive_binary_search(elements, target)
    print('Search - recursive binary method index:', res)
    print('duration in miliseconds: ', timer.calcTime(start), '\n')
