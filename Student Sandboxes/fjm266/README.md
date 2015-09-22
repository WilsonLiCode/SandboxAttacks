# appSec1

Super simple "sandbox".  The sandbox will run any code in "code.in" and will read in the contents of "data.in" as a string.  Alternatively, you can specify your own files as arguments by typing:

python sandbox.py code data

Leave those options empty to run the test code.

The sandbox is just python with its namespace cleared.  Most of the pre-defined data types still work but import, open and most other built in functions are gone.  
