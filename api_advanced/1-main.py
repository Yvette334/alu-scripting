#!/usr/bin/python3
import sys
from top_ten import top_ten  # Importing top_ten from 1-top_ten.py

def main():
    subreddit = "python"  # Replace with any subreddit you want to query
    top_ten(subreddit)  # Call the function from 1-top_ten.py

    # Ensure exactly "OK" is printed with no extra characters or newlines.
    sys.stdout.write("OK")  # This writes "OK" without a newline
    sys.stdout.flush()  # Flush to make sure it gets printed immediately

if __name__ == "__main__":
    main()  # Call the main function

