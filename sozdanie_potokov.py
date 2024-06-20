"""Программа, которая создаёт 2 потока"""
from threading import Thread
from time import sleep

numbers = range(1, 10)
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'j')


def stream(*args):
    for number in numbers:
        print(number, flush=True)
        sleep(1)
    for letter in letters:
        print(letter, flush=True)
        sleep(1)


thread = Thread(target=stream, args=numbers)
thread.start()

stream(letters)

thread.join()
