# find_by_size.py
Python3 code that recursively walks a starting path's sub-paths and prints every file that is within the size window.

Ignores:  Hidden files that start with "." and links.

Why avoid links? - Symlinks can result in loops in the directory structure which either need to be detected
or avoided.  If you do neither, you will loop forever until you end up hitting the 4096 linux default file path length and then raise an exception.

If you wanted to solve that problem:  DFS with a lookup of visited vertices.

# usage
example.  Find all files under ~/src and all of the sub-paths of ~/src between 1 and 100 GB.

You can specify units of KB, MB, or GB.

$./find_by_size.py ~/src 1 100000 MB

$./find_by_size.py ~/src 5 50 GB

$./find_by_size.py ~/src 1 1023 KB

# future improvements
* better error reporting would be more friendly.
* For tooling, you would want to output in a standard format like JSON if you
don't mind that json is byte wasteful.
