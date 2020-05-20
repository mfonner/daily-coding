#!/usr/bin/env python3

'''
Given a list of numbers and a number, k, return whether any two numbers from
the list provided add up to k.
'''

import itertools

def main():
    
    # Example num list and K
    num_list = [10, 15, 3, 7]
    k = 17
    
    # itertools.combinations will generate every possible r length subsequence 
    # of the list passed, here I'm generating every combination with 2 pairs
    # Those pairs then get added and checked against our k value
    for nums in itertools.combinations(num_list, 2):
        if nums[0] + nums[1] == k:
            print(nums[0],',',nums[1])
            return True

if __name__ == '__main__':
    main()
