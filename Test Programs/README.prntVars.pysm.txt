If you use the command PRNTVARS,
the sandbox will crash with an IndexError exception.

This is also a bug in the sandbox because the PRNTVARS will never work
because the command takes in no arguments and the evaluate function always tokenizes a line
assuming that it will contain at least 2 arguments delimited by a comma.