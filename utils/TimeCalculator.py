import time
from datetime import datetime

def start():
    return datetime.now().microsecond

def calcTime(startTime):
    return (datetime.now().microsecond - startTime)/1000
