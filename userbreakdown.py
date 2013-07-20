"""
file:   userbreakdown.py
author: NManoogian
desc:   Uses apache log files and .htpasswd file to create a user breakdown
"""
import sys

def getUserLines(userlst, filename):
    # Retrieve Users
    users = []
    f = open(filename)
    for line in f:
        print (
        users.append(line.split()[2])

    userline = {}

    # Generate user to list of lines dictionary
    for user in userlst:
        userline[user] = []

    # If the line contains a user, add the line to the dictionary
    for line in f:
        for user in userlst:
            if user in line:
                userline[user].append(line)
    return userline


def main():
    userline = getUserLines(getUsers(sys.argv[1]),sys.argv[1]);
    for key in userline:
        print(key);
        for line in userline[key]:
            print("\t" + line)

main()
