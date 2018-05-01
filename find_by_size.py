#!/usr/bin/env python3

"""
find_by_size.py

Python3 code that recursively walks a starting path's sub-paths and prints every
file that is within the size window.

Ignores:  Hidden files that start with "." and symlinks

Done recursively, without using os.walk for academic purposes.

Note:  Recursion is a fun exercise until you blow up the stack.  Consider an
iterative solution anytime the data set can be large enough to threaten this
problem. (i.e. Use a Queue (think bfs...))

Why not use os.walk()?

The problem with os.walk is that it makes O(2N) system calls on just
about every path or file object and that is not ideally performant.

Python 3.5+ has scandir which is optimized versus os.walk makes O(n) system
calls, so that would probably be the most direct solution to this problem.

If you wanted (for example) a bottom up walk without os.walk(topdown=False) you
would consider pushing all sub paths onto a LifoQueue until there were no more
to process, and then process the stack top down.  LifoQueue would be ideal for
a multithreaded approach as its operations are threadsafe.

Avoids hidden files.

Prints output to stdout.

Raises:  Any exception raised while trying to read files/dirs will be raised
directly.


Author:  c.gleeson 2018
"""

import os
import sys

def get_args():
    if len(sys.argv) < 4:
        print("Args needed:  start_path file_size_min file_size_max ['KB','MB','GB']")
        sys.exit(1)
    start = sys.argv[1]
    min_size = int(sys.argv[2])
    max_size = int(sys.argv[3])
    unit = sys.argv[4]
    return (start, min_size, max_size, unit)

#the long way around without using os.walk()
def rec_walk(start, min_size, max_size, unit):
    for child in os.listdir(start):
        #Lets omit hidden files/paths that start with "."
        if child.startswith('.'):
            continue
        #Lets also omit any symlinks, as in certain cases following those
        #can result in endless traversal loops
        path = os.path.join(start, child)
        if os.path.islink(path):
            continue
        #If we find a file...
        if not os.path.isdir(path):
            file_size = os.stat(path).st_size
            if unit == 'MB':
                file_size = file_size / (1024 * 1024)
            elif unit == 'GB':
                file_size = file_size / (1024 * 1024 * 1024)
            if file_size < max_size and file_size > min_size:
                print("FOUND: ")
                print(path, end="\t")
                print("SIZE: ", file_size, end=" ")
                print(unit)
        #Recurse on the sub-directory
        else:
            rec_walk(path, min_size, max_size, unit)

if __name__ == "__main__":
    (start, min_size, max_size, unit) = get_args()

    rec_walk(start, min_size, max_size, unit)
