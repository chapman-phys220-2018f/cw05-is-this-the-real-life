#!/usr/bin/env python3
 #-*- coding: utf-8 -*-

###
# Name: Gage Kizzar and Natanel Alpay
# Student ID: 2291700
# Email: kizzar@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW03
###

def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print (b);
        c=a+b
        a=b
        b=c
