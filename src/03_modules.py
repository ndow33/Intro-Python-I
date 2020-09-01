"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print out the command line arguments in sys.argv, one per line:
print('_________________________________________________')
for command in dir(sys.argv):
    print(command)

# Print out the OS platform you're using:
print('_________________________________________________')
print(sys.platform)

# Print out the version of Python you're using:
print('_________________________________________________')
print(sys.version)

# Print the current process ID
print('_________________________________________________')
print(os.getpid())

# Print the current working directory (cwd):
print('_________________________________________________')
print(os.getcwd())

# Print out your machine's login name
print('_________________________________________________')
print(os.getlogin())
