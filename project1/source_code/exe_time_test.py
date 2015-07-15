#!/usr/bin/python
#usage: python exe_time_test.py [n]
###############################################################################

from random import randint
import sys, datetime
from sys import maxint

#copy/paste function instead of import to remove print and file operations
###############################################################################

def enum_max_sub(array):
	#make max most negative possible int value
	max = -maxint - 1
	index_low = 0
	index_hi = 0
	#for each combination of i & j bounded by the length of the array
	for i in range(0, len(array)):
		for j in range(0, len(array)):
			#for non-negative ranges
			sum = 0
			if i <= j:
				#summation of all values contained between i & j
				for k in range(i, j+1):
					sum = sum + array[k]
			#if new sum is larger than all previous, save
			#along with the current lo and hi indices
			if sum > max:
				max = sum
				index_lo = i
				index_hi = j					
				
			#reset sum
	#***This return is used in execution time testing***
	return max	

def divide_conquer_max_sub(a):   

	# the following function is to find the crossiing max subarray
    def find_cross_max(a, l, r, m):

        # left Side
        ls_l = m+1
        ls_r = m
        l_max_sum = None
        sub_sum = 0
		# add elements from right to left
        for j in xrange(m,l-1,-1):
            sub_sum += a[j]
            if sub_sum > l_max_sum:
                l_max_sum = sub_sum
                ls_l = j
        
        # right Side             
        rs_l = m+1
        rs_r = m
        r_max_sum = 0
        sub_sum = 0
		# add elements from left to right
        for j in range(m+1,r+1):
            sub_sum += a[j]
            if sub_sum > r_max_sum:
                r_max_sum = sub_sum
                rs_r = j

        #combine sums
        return (ls_l, rs_r, l_max_sum+r_max_sum)
	sum = 0

    def Divide_and_conqur_recursion_classification(a,l,r):   
		
		# Base case
        if r == l:
            return (l,r,a[l])
		# Notice below that we pass array indexed starting at half_array_len
        else:

            m = (l+r)//2                    
            left_max = Divide_and_conqur_recursion_classification(a,l,m)        
            right_max = Divide_and_conqur_recursion_classification(a,m+1,r)     
			# Recursive cases
            cross_max = find_cross_max(a,l,r,m)   
			# check maximum sum left side
            if left_max[2]>=right_max[2] and left_max[2]>=cross_max[2]:
                return left_max
			# check maximum sum right side
            elif right_max[2]>=left_max[2] and right_max[2]>=cross_max[2]:
                return right_max
			# check the crossing sum 
            else:
                return cross_max

    #back to master function
    l = 0
    r = len(a)-1
	
    return Divide_and_conqur_recursion_classification(a,l,r)


def better_enum_max_sub(array):
	max = -maxint - 1
	index_lo = 0
	index_hi = 0
	#for each combination of i & j where i < j
	for i in range(0, len(array)):
		#reset sum
		sum = 0
		#calculate a continuous sum, and check sum at each addition
		for j in range(i, len(array)):
			sum = sum + array[j]
			#if new sum is larger than all previous, save
			if max < sum:
				max = sum
				index_lo = i
				index_hi = j+1 

	#***This return is used in execution time testing***
	return max


def linear_max_sub(array):
	maximum = 0
	sum = 0

	for i in range(0, len(array)):
		if(sum + array[i] > 0):
			sum += array[i]

		else:
			sum = 0

		maximum = max(maximum, sum)

	return maximum




print 'Generating array of size: ', sys.argv[1]

test_array = []
for i in range(0, int(sys.argv[1])):
	test_array.append(randint(-99,99))

#print 'Testing enumeration method...'
#t1 = datetime.datetime.now()
#enum_max_sub(test_array)
#t2 = datetime.datetime.now()
#diff = t2 - t1
#print 'Execution time: ', diff.seconds, 's', int(diff.microseconds/1000), 'ms'

#print 'Testing better enumeration method...'
#t1 = datetime.datetime.now()
#better_enum_max_sub(test_array)
#t2 = datetime.datetime.now()
#diff = t2 - t1
#print 'Execution time: ', diff.seconds, 's', int(diff.microseconds/1000), 'ms'

print 'Testing D&C method...'
t1 = datetime.datetime.now()
divide_conquer_max_sub(test_array)
t2 = datetime.datetime.now()
diff = t2 - t1
print 'Execution time: ', diff.seconds, 's', int(diff.microseconds/1000), 'ms'

#print 'Testing linear method...'
#t1 = datetime.datetime.now()
#linear_max_sub(test_array)
#t2 = datetime.datetime.now()
#diff = t2 - t1
#print 'Execution time: ', diff.seconds, 's', int(diff.microseconds/1000), 'ms'