from algorithms import Sort
from utils import TimeCalculator as timer
import random

def test():
    print('Sort methods \n')
    list = random.sample(range(-10, 10), 10)

    print('Select sort range:', list)
    print('Result sort:', Sort.select_sort(list))