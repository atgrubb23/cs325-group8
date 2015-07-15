#!/usr/bin/python
#usage: python changeslow.py
###############################################################################
from sys import maxint
#similar to var_dump in PHP
import pprint
#function:	changeslow
#args:		integer array, integer
#returns:	2 element list - first element is the number of coins, the second is an array that repressents the coins used.
###############################################################################

### Work in progress - calculates min number, but I can't seem to get the min coins used =(  Feel free to fix it up
def changeslow(v, A):
	coins_used = [0 for x in range(len(v))] 
	if A == 0:
		return 0
	min_num = maxint
	for i in range(0, len(v)):
		if (v[i] <= A):
			min_num = min(min_num, changeslow(v, A - v[i]) + 1)
	return min_num


test = [1, 2, 4, 8]
coins_used = [0 for x in range(len(test))] 
pprint.pprint(changeslow(test, 15))