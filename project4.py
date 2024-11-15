# project4.py
#
# ICS 33 Spring 2024
# Project 4: Still Looking for Something

from input import *
from grammar import Grammar
from pathlib import Path



def main() -> None:
    """Asks user for inputs and executes based on the input"""
    """"difficult to unit test due to its reliance on user inputs, 
    and bc the randomness of selecting options changes constantly"""
    path = Path(input())
    num_sentences = input()
    start_var = input()
    liness = read_lines(path)
    g = Grammar(liness, num_sentences, start_var)
    g.execute()


# /Users/lek2/Desktop/grin1.txt
# 5
# HowIsBoo

# /Users/lek2/Desktop/grin.txt
# 5
# PrintStatement


if __name__ == '__main__':
    main()
