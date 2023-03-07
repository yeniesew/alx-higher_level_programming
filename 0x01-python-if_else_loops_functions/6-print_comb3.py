#!/usr/bin/python3
8	for digit1 in range(0, 10):
9	    for digit2 in range(digit1 + 1, 10):
10	        if digit1 == 8 and digit2 == 9:
11	            print("{}{}".format(digit1, digit2))
12	        else:
13	            print("{}{}".format(digit1, digit2), end=", ")
