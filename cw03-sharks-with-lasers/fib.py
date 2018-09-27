#!/usr/bin/env python3

###
# Name: Morgan Holve
#Student ID: 2281337 
#Email: holve100@mail.chapman.edu 
#Course: MATH220 Fall 2018 
#Assignment: CW3
###

import sequences

def main(argv):
    """Takes the Python program fibonacci.py and runs it in a new module. This module will not print an entire list of the Fibonacci sequence, and will instead only return 
    the nth number as an integer."""
    n=int(argv[1])
    if n<0:
        raise ValueError
    else:
       x=sequences.fibonacci(n)
       print(x[len(x)-1]) #Shoutout to Trevor for reminding me that the len function exists

if __name__ == "__main__":
    import sys
    main(sys.argv)
