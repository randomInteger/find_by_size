# find_by_size.py
Python3 code that recursively walks a starting path's sub-paths and prints every file that is within the size window.

Ignores:  Hidden files that start with "." and links.

Why avoid links? - Symlinks can result in loops in the directory structure which either need to be detected
or avoided.  If you do neither, you will loop forever until you end up hitting the 4096 linux default file path length and then raise an exception.

If you wanted to solve that problem:  DFS with a lookup of visited vertices.

# performance
This implementation was done recursively, without using os.walk for academic purposes.

Note:  Recursion is a fun exercise until you blow up the stack.  Consider an
iterative solution anytime the data set can be large enough to threaten this
problem. (i.e. Use a Queue (think bfs...))

Why not use os.walk()?

The problem with os.walk is that it makes O(2N) system calls on just
about every path or file object and that is not ideally performant.

This solution is also not highly performant, because it relies on calling stat()
just like os.walk() does.

Python 3.5+ has scandir which is optimized versus os.walk makes O(n) system
calls, so that would probably be the most performant solution to this problem.

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
