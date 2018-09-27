#!/bin/bash

###
# Name: Morgan Holve
# Student ID: 2281337
# Email: holve100@mail.chapman.edu
# Course: MATH220 Fall 2018
# Assignment: CW3
###

if [ ! -f fibs.csv ] #Checks to see if a file already exists
then 
 for i in $(seq 10); do #if it does not exist, file is created
 ./fib.py $i | tr '\n' ','>> fibs.csv
 done

else
 if [ ! -f fibs.csv.bak ] #checks if the backup file exists
 then
 cp ./fibs.csv  ./fibs.csv.bak #creates backup from previous file

  echo File already exists. Backup created. 
 else
 echo Back up and original already exist. Command unable to execute. #both files exist, exits code
 exit 
fi

fi
