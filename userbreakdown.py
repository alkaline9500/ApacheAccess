"""
file:   userbreakdown.py
author: NManoogian
desc:   Uses apache log files to create a user breakdown
"""
import sys

def getUserLines(filename):
    # Open the file
    f = open(filename)

    # Make a dictionary
    # user : list of lines
    userline = {}

    # For each line, find the user
    for line in f:
        user = line.split()[2]
        # If the user is not in the dictionary, make an empty line list
        if user not in userline:
            userline[user] = [];
        # Add line to line list
        userline[user].append(line.strip())

    return userline


def main():
    userline = getUserLines(sys.argv[1]);
    for key in userline:
        print(key);
        for line in userline[key]:
            # Weed out image requests
            if "/icons/" not in line and "favicon" not in line:
                print("\t" + line)

main()
