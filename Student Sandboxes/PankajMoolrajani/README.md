# python-sandbox
Turing Complete Python Sandbox


Instructions to run turing complete sandbox:

1.) download source code and navigate to project's root directory

2.) following are the ways to run example programs and exploit programs in sandbox (for testing purposes):
    
    2.1) run default example programs (power of 2, fibonacci) with default values:
        2.1.1) python sandbox.py
        2.2.2) python -i sandbox.py (interactive mode - load interpreter in sandbox environment)
    
    2.2) run default example programs (power of 2, fibonacci) with customized values:
        
        2.2.1) change source code "sandbox.py", edit arguments of following function calls: 
            2.2.1.1) ob_operations.computeFibonacci(10)
            2.2.1.2) ob_operations.computePower(128)
        
        2.2.2) run sandbox in python interactive mode, make object of Opertaions class and call computation functions
            python -i sandbox.py
            >> from operations import Operations
            >> ob = Operations()
            >> ob.computePower(5)
            >> ob.computeFibonacci(15)
    
    2.3) run exploit programs in sandbox with non-interactive mode 
        python sandbox.py -f exploit-program.py
    
    2.4) run exploit program in sandbox with interactive mode
        python -i sandbox.py -f exploit-program.py
        
