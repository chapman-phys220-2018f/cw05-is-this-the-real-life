#!/usr/bin/env python3
#-*- coding: utf-8 -*-
###
# Name: Gage Kizzar and Natanel Alpay
# Student ID: 2291700
# Email: kizzar@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW03
###        
     

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
