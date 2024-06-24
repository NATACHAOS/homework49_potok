"""Программа, которая создаёт 2 потока"""
from threading import Thread
from time import sleep

numbers = range(1, 11)
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')


def stream_1(*args):
    for number in numbers:
        print(number, flush=True)
        sleep(1)


def stream_2(*args):
    for letter in letters:
        print(letter, flush=True)
        sleep(1)


thread = Thread(target=stream_1, args=numbers)
thread.start()

stream_2(letters)

thread.join()
