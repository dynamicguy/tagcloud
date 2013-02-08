__author__ = 'ferdous'
import random

def run():
    lines = open('/usr/share/dict/words').readlines()
    for line in range(1,301):
        ln = ''.join(['<li><a href="#">', random.choice(lines).rstrip(), '</a></li>'])
        print ln


if __name__ == "__main__":
    run()
