#!/usr/bin/env python3

'''
Implement an autocomplete system. 
That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string 'de' and the set of strings: 
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

import argparse
import re

# Getting query string from user input
parser = argparse.ArgumentParser(description='Gathering input for query string')

parser.add_argument('-q', '--query', help='Query string to auto complete with.')

args = vars(parser.parse_args())

def main():

    # List of strings to apply our RegEx filter to
    strings = ['dog', 'deer', 'deal', 'speed', 'read']
    
    # Adding a wild card to our search query 
    search_pattern = str('.*' + args['query'])
    
    # Converting user-supplied query to a RegEx object
    r = re.compile(search_pattern)
    
    # match is a new list created via the new 3.8 Walrus operator
    # This new list is filtered by what is matched via our RegEx pattern
    if any(match := list(filter(r.match, strings))):
        print(match)


if __name__ == '__main__':
    main()
