# find_by_size.py
Python3 code that recursively walks a starting path's sub-paths and prints every file that is within the size window.

# usage
example.  Find all files under ~/src and all of the sub-paths of ~/src between 1 and 100 GB.

You can specify units of KB, MB, or GB.

$./walk.py ~/src 1 100000 MB

$./walk.py ~/src 5 50 GB

$./walk.py ~/src 1 1023 KB

# future improvements
* better error reporting would be more friendly.
* For tooling, you would want to output in a standard format like JSON if you
don't mind that json is byte wasteful.
