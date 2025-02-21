#!/usr/bin/python3
"""
Main module for testing the `top_ten` function.

This script takes a subreddit name as a command line argument,
and calls the `top_ten` function to display the top 10 hot posts
for the given subreddit. If no argument is passed, it will prompt
the user to provide a subreddit name.
"""
import sys

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

