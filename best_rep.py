#!/usr/bin/env python
import json


def load_json(path):
    # open a file and return it as json
    with(open(path)) as f:
        for line in f:
            yield json.loads(line)


def main():
    max_rep = -1
    for user in load_json('users.json'):
        rep = int(user['Reputation'])
        if rep>max_rep:
            max_rep = rep
            print user
    print
    print "The user with the highest reputation has %d points."%max_rep


if __name__ == "__main__":
    main()
