#!/usr/bin/env python3

'''
Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
'''

from time import sleep
import argparse

# Argument parsing
parser = argparse.ArgumentParser(description='Takes input for job scheduler timer')

parser.add_argument('-t', '--time', help='Time to sleep before calling function.'),
parser.add_argument('-f', '--function', help='What function to call, a or b.')

args = vars(parser.parse_args())

def func_a(wait_time):
    sleep(int(wait_time))
    print('a')
    return True

def func_b(wait_time):
    sleep(int(wait_time))
    print('b')
    return True

def main():
    
    # Converting seconds to milliseconds
    temp_time = int(args['time'])
    milli_time = temp_time / 100
    #print(milli_time)

    if args['function'] == 'a':
        func_a(milli_time)
    if args['function'] == 'b':
        func_b(milli_time)

if __name__ == '__main__':
    main()
