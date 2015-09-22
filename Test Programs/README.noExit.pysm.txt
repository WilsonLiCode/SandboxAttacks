If you pass in any code that does not end with the EXIT command, 
the sandbox will crash with an IndexError exception.
This is because it still continues to read and tokenize blank lines.