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
        
        
________________________________________________________________________________________

BUILT IN FUNCTIONS

   Included with the interpreter - can always use with out importing any modules

	abs()           delattr()   hash()      memoryview()    set()
    all()*           dict()      help()      min()       setattr()
    any()           dir()       hex()       next()      slice()
    ascii()         divmod()    id()        object()    sorted()
    bin()           enumerate() input()     oct()       staticmethod()
    bool()          eval()      int()       open()      str()
    breakpoint()    exec()      isinstance()ord()       sum()
    bytearray()     filter()    issubclass()pow()       super()
    bytes()         float()     iter()      print()     tuple()
    callable()      format()    len()       property()  type()
    chr()           frozenset() list()      range()     vars()
    classmethod()   getattr()   locals()    repr()      zip()
    compile()       globals()   map()       reversed()  __import__()
    complex()       hasattr()   max()       round()

    def all(iterablea):         #if all elemenets are true
        for element in iterable:
            if not element:
                return False
        return True
    
    def any(iterable):          #if any element is true
        for element in iterable
            if element
                return True
        return False

_______________________________________________________________________________________________

PYTHON KEYWORDS

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

__________________________________________________________________________________________________

REVERSING A STRING  (EASY IN PYTHOM!!)

    greeting = "Hello, World!"
    print(greeting[::-1])


__________________________________________________________________________________________________
LISTS

   -Can contain multiple types, but usually do not
   - can be insexed and sliced
         (as all built0in sequence types)
   -mutable
   -simple assignments do not copy*********
      any changes made to a list through one variable will be reflected in all
      variables that refer to it

      EG: a = [1,2,3,4]
          b = a
          a[2] = 10
          print(b)
          [1,2,10,4]
    -lists can be nested 

    -List Methods:
        list.append(x)
        list.extend(iterable) 
            extend the list by appending all items from the iterable
        list.insert(i,x)
        list.remove(x)
        list.pop(i) - if no index is given , will remove the end
        list.clear() - similar to del a[:]
        list.index(x[, start[, end]])   
	    list.count(x) - returns the number of time x appears
        list.sort(*, key-None, reverse=False)
        list.reverse() - reverses elements in place
        list.copy - returns a shallow copy of a list
        

        **some methods like insert, remove or sort only modify the list
          but return None
          only same type data can be sorted

   What is Shallow Copy:
    import copy

    a = [1, 2, [3, 4]]
    b = a.copy()  # Shallow copy (same as `b = a[:]` or `b = list(a)`)
    c = copy.copy(a)  # Another way to shallow copy

    a[2][0] = 99  # Modify a nested element

    print(a)  # [1, 2, [99, 4]]
    print(b)  # [1, 2, [99, 4]] → Nested list is shared!
    print(c)  # [1, 2, [99, 4]] → Also affected!

    Using lists as stacks (lifo)
        easily through append and pop without indexes
    Usinf lists as quues (fifo)
        not efficient
        use collections.deque
        Eg
        from collections import deque

        queue = deque(['Eric', 'John', 'Michael'])
        queue.append('Terry')
        queue.append('Grahm')
        queue.popleft()
        'Eric'
        queue popleft()
        'John'
        queue
        deque(['michael', 'Terry', 'Grahm'])


    List Comprehensions
        -concise way to create lists
        -commonly: make new lists where each element is the result of some 
         operation applied to each member of another sequence or iterable
         or, create a subsequence of those elements that satisfy a certain 
         condition

    ...

TUPLES AND SEQUENCES
    Sequence Types: lists, tuples and range

    Tuples:
        -number of values seperated by a comma
        -immutable
        -not possible to assign individual items of a tuple, but can contain
         mutable objects, such as lists

SETS
    -unordered collection with no duplicate elements
    -created with curly braces or set() function
    -basic uses:
           - membership testing and eliminating duplicate entries
            -support mathematical operations like union, intersection, difference
             and symmetric difference
