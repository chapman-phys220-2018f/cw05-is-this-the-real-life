
#!/usr/bin/env python
# -*- coding: utf-8 -*-

###
# Name: Morgan Holve
# Student ID: 2281337
# Email: holve100@mail.chapman.edu
# Course: MATH 220
# Assignment: CW03
###

"""This programs takes an integer argument n and returns a list of the Fibonacci Sequence up until its nth member. For example, running fibonacci(6) will return
[1,1,2,3,5,8]
The only real application of this is if you need an incredibly high nth term of the Fibonacci sequences and are terrible at adding.
"""

def fibonacci(n):
	"""This function caluclates and returns the Fibonacci sequence up until the nth term
    	arguments:
     	n: the number of terms printed in the Fibonacci sequence
    	returns:
     	fib: a list of the Fibonacci sequence up until the desired nth term.
	"""
	first=0 
	second=1
	if n<0: #Handles nonsensical argument input
		raise ValueError
	else:
		fib=[1] #Trevor helped me with this, as I was under the impression that 1+1=1
		for i in range(0,n-1):
			temp=first
			first=second
			second = temp + second #Above three lines recursively add variables up until the nth term
			fib.append(second) #Appends the nth term to the list
		return fib

