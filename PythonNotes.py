https://www.python.org 

Describtions of standard objects and models:
	Pyhthon Standatd Library
	The Python Language Reference
	Exetending and Embedding the Python Interpreter Python/C API reference
		to write extensions in C/C++

__________________________________________________________________________________________
Paper: Python Garbage Collector Implementations: CPython, PyPy and GaS
	(Jan 2012)

	CPython : refrence implementation 
	Jython(1997) Python compiler writtenm in Java tageting Java VM
	IronPython(2006) for common language infrastructure (.NET)
	PyPy(2007) written in RPyhton(restricted subset of Python)
	
	Garbage Collection In CPython
		-uses reference counting and a generational garbage collector to detect 
		 cycles in the current version
		-file can be written and closed in one statement:
		 Example:
		 	open('test.txt', 'w').write('hello world')	
		 the file is flushed and closed as soon as the refcount of the file
		 object (retunn value of open()) becomes zero
...

____________________________________________________________________________________________


A Python Interpreter

    -if called from CLI - read and executes commands interactively
    -if called with a filename, it will read and execute the script

	-interpreter = last step in the process of executing a python program
	Steps:
		1. Lexing (tokenization)
		2. Parsing
		3. Compiling
		4. Interpreting
	
	-stack virtual machine - manipulate several stacks to perform its operations
	    (register machine - writes to and reads from particular memory locations)
	-bytecode interpreter - input is instruction sets called bytecode
			lexer, pasrser and compiler generate code objects for the interpreter
			to operate on. Each code objects contain a set of instructions - byte
			code.  (Analagolous to C uses assembly as intemediary)

    -ARGUMENT PASSING
        script name and arguments are turned into a list of strings and assigned to
        argv  (sys module

    -ENVIRONMENT
        -encoded in UTF-8 by default)
        -declare an encoding other than default:
            1st line of script after shebang: # -*- coding: encoding -*-  (encoding is a valid 
            codec supported by python)
            eg: Windows-1252

                # -*- coding: cp1252 -*-

______________________________________________________________________________________________

dis - Disassembler for Python bytecode

	dis module supports analysis of Cpython bytecode by disassembling it

...
_______________________________________________________________________________________________
TEXT SEQUENCE TYPE - str

	- represented by str (strings) includes: characters, words, numbers, symbols
	- immutable
	- str.join() or io.StringIO can construct strings from multiple fragments
	- to quote a quote:
			'doesn\'t'
			"doesn't"
			'"Yes", they said.'
			"\"yes,\"they said."

	-raw strings (r before quote)
		>>>print('C:\some\name')
		   C:\some
		   ame
		>>>print(r'C:\some\name')
			C:\some\name

	- triple quotes 
	- two or more string literals next to each other are auto concatenated
		>>> 'Py' 'thon'
		'Python'
	
    -STRING METHODS
        common sequence operations:
            x in s
            x not in s
            s + t
            s * n 0r n *s
            s[i]
            s[i:j]
            s[i:j:k]
            len(s)
            min(s)
            max(s)
            s.index(x[, i[, j]]) index the first occurance of x in s
                                 at or after index i and before j
            s.count(x) total number of occurrences of x in s
        
        

        
	
