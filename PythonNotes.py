https://www.python.org 

Describtions of standard objects and models:
	Pyhthon Standard Library
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
			code.  (Analagolous to C using assembly as intemediary)

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

   - Create:
            a_list = [] #empty list
            oneToTen = list(range(10)) #[0,1,2,3,4,5,6,7,8,9]
   -Can contain multiple types, but usually do not
   - can be insexed and sliced
         (as all built0in sequence types)
   -mutable
   -changed IN PLACE - return value after a method is None.  Cant asign to 
        variablwe without copying
        eg:
          sort() method - sorts in place, returns None
          sorted() function will return a new list
   - copying a list:
        Shallow Copy
            new_list = my_list.copy()
            new_list = my_list[:]
            new_list = list(my_list)
        Deep Copy
            .deepcopy()
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
        shown with dir(list())
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
    Using lists as quues (fifo)
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
         EG:
            numbers = [1,2,3,4,5]
            squares = [x**2 for x in numbers] #[1,4,9,16,25]
            even_squares = [x**2 for x in numbers if x % 2 == 0] #[4,16]

    ...
______________________________________________________________________________________________

TUPLES AND SEQUENCES
    Sequence Types: lists, tuples and range

    Tuples:
        -number of values seperated by a comma
        -immutable
        -not possible to assign individual items of a tuple, but can contain
         mutable objects, such as lists
        -because immutable, only have 2 methods:
            dir(tuple())
                count()
                index()
        -concatenating tuples creates a new tuple:
            a_tuple = (1,2,3,3)
            id(a_tuple)
            140617302751760
            a_tuple += (6,7)
            id (a_tuple)
            140617282270944

        **object id is equivalent to an objects address in memory***

        Extracting Multiple Values in a Tuple while Looping:
            >>>list_of_tuples = [(1,' bananna'), (2, 'apple'), (3, 'pear')]
            >>>for number, fruit in list_of_tuples:
            ...     print(f'{number} - {fruit}')
            ...
            1 - bannana
            2 - apple
            3 - pear
____________________________________________________________________________________________________

DICTIONARIES

    -key, value pairs - similar to hash tables in other languages
    -a mapping that maps keys (hashable objects) with any object
    - ordered since 3.7
    -keyword dict
    -acces by key - if key not in dict KeyError
    - key in dict or key not in dict -----Boolean

    -Methodas:
        d.get()
            defaults to None if not in dictionary and no default given
        d.clear()
        d.copy() shallow copy (need deepcopy if dict contains objects or
            dictionaries)
        d.items() return a new view of dict items
        d.keys() dynamic view of keys
        d.values() dynamic view of values
        d.pop() key and default, if no default and key not found KeyError
        d.popitem() remove key, value pair LIFO if dicyt empty -> KeyError
        d.update() update with key, value (will overwrite value with existing
            key) returns None

    -Modifying a Dict:
        add key value pair:
            sample_dict['address'] = '123 Dunn St'
        same to change value (also use d.update())
        delete pairs:
            del sample_dict['addres']
            you can also use d.pop() - remove key and return value

    -Looping Over a Dictionary:
        -will loop over keys
        -can loop over both by using items()
          users = {'mdriscoll': 'password', 'guido':'python'}
          for user, password in users.items():
              print(f"{user}'s password is {password}")
_____________________________________________________________________________________________

LOOPING WITH enumerate
    takes an iterable and returns a tuple in the form (count, item)
    >>>my_str = 'abcdefg'
    >>>for pos, letter in enumerate(my_str):
    ...     print(f'{pos} - {letter}')
    ...
    0 - a
    1 - b
    ...



_______________________________________________________________________________________________
SETS
    -unordered collection of distinct hashable objects 
    -created with curly braces or set() function
    -basic uses:
           -membership testing and eliminating duplicate entries
           -support mathematical operations like union, intersection, difference
             and symmetric difference
    -Two types:
        set -mutable
        frozenset - immutable and hashable
    -Creating a set
        my_set = {"a", "b", "c",}
         - duplicates will be removed automatically
        set()
    -accessing values
        chdck with in operator
        no slicing, but can iterate
    -add items to a set:
        add() or update()
            my_set = {"a", "b", "c", "c"}
            my_set.add("d")
            my_set
            {"d", "c", "a", "b"}
        use update for multiple items
            my_set.update(['d', 'e', 'f'])
            my_set
            {'a', 'c', 'd', 'e', 'b', 'f'}
            - update will take any iterable (list, tuple or set)

    -Remove  .remove(), .discard() or .pop()
        if you use dicard() on an item that doesnt exist, it wont error
        pop will remove and return
            if you use pop without a value, you wont know what is 
                removed since sets are unordered
                also: pop() on an empty set raises an KeyError opposed
                to IndexError in list

     -clear or delete 
        clera() returns an empty set
        del completely removes set

     -Set Operations
        union() - combines two sets and returns new set
        intersection() - returns a new set of common values
        difference() - returns a new set with elements that are not in 
            the new set

     EG:
        first_set = {'one', 'two', 'three'}
        second_set = {'orange', 'banana','peach'}
        first_set.union(second_set)
        {'two', 'banana', 'three', 'peach', 'orange', 'one'}
        first_set
        {'two', 'three', 'one'}
       ***if you want to save unionized set, use a new variale***

     EG:
        second_set.add('one')
        intersection = first_set.intersection(second_set)
        intersection
        {'one'} 
     
     EG:
        second_set = {'three', 'four','one'}
        first_set.difference(second_set)
        {'two'}
        second_set.difference(first_set)
        {'four'}

    Other methods, but very uncommon
_____________________________________________________________________________________________________
BOOL FUNCTIONS

  False maps to zero and True maps to 1
  ****bool() function****
  any value will map to true!
    >>>bool('0')
    >>>True
    >>>bool('')
    >>>False
    >>>bool ([])
    >>>False
    
   -None pythons null value, its data type is NoneType
        -cn asign to a variable, but all instances will point to same object
        >>>x = None
        >>>y = None
        >>>id(x)
        >>>4478513256
        >>>id(y)
        >>>4478513256

Special Operators
    special operators to be used in conditional expressions
      IDENTITY
        is = True when operands are identical
        is not True when operands are not identical
      MEMBERSHIP
        in True when value is in a collection
        not in True when value is not in a collection
     EG:
        >>>x = [1,2,3]
        >>>y = [1,2,3]
        >>>x == y
        >>>True
        >>>x is y
        >>>False
        >>>id(x)
        >>>140328193994832
        >>>id(y)
        >>>14038193887760
     EG:  re: strings are immutable
        >>>x = 'hi'
        >>>y = 'hi'
        >>>x == y
        >>>True
        >>>x is y
        >>>True

________________________________________________________________________________________________
LOOPS AND ELSE STATEMENT

    EG
    >>>my_list = [1,2,3]
    >>>for number in my_list:
    ...     if number == 4:
    ...         print('Found number 4!')
    ...         break
    ...      print(number)
    ...else:
    ...      print('Number 4 not found')
    1
    2
    3
    Number 4 not found
___________________________________________________________________________________________________

PYTHON COMPREHENSIONS

    LIST COMPREHENSIONS
        EG - make a new list, doubling values
        >>>sequence = [1,2,3]
        >>>new_list = [x * 2 for x in sequence]
        >>>new_list
        [2,4,6]

        EG Odd numbers
        >>>odd_numbers = [x in range(10) if X % 2]
        >>>odd_numbers
        [1,3,5,7,9]
              %%%%%%%%%%%evaluating truthiness of x % 2 (not X%2 == 0)
                        if x % 2 = 0 0 is false
                        if x % 2 = 1 1 is true

        EG take a dictionary and make a list of tuples
        >>>my_dict = {1: 'dog', 2: 'cat', 3: 'python'}
        >>>[(num, animal) for num in my_dict for animal in my_dict.values() if my_dict[num] == animal]
        [(1, 'dog'), (2, 'cat') (3, 'python')]

                repeat w/o comprehension
                >>>my_dict = {1: 'dog', 2: 'cat', 3: 'python'}
                >>>my_list = []
                >>>for num in my dict:
                ...  for animal in my_dict.values():
                ...     if my_dict[num] == aniaml:
                ...         my_list.append((num, animak))
                ...
                >>>my_list
                [(1, 'dog'), (2, 'cat'), (3, 'python')]

    DICTIONARY COMPREHENSIONS
        
        >>>{key: value for key, value in enumerate('abcde')}
        {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

    SET COMPREHENSIONS

        exact same syntax as list with the exception of curly brackets in place of
        parenthesis


__________________________________________________________________________________________________

Lambda Operator, filter, reduce and map

    lambda function  - small anonmymouse "throw away" functions
        typically used with filter() map() or reduce()
        syntax: lambda argument_list: expression
        eg: 
            sum = lambda x,y : x + y
            sum(3,4)
            output: 7

     map() is a function that takes two arguments  r = map(func, seq)
      map applies the function to all the elements in the sequence

....
_______________________________________________________________________________________________
EXCEPTION HANDLING

 ****NOTE***
        Consider Pyinputplus
 ***********

    Most Commom Exceptions:
        AttributeError - attribute ref or assignment fails
        ImportError - import statement fails
        ModuleNotFoundError - subclass of ImportError when module cant be located
        IndexError - sewquence subscript is out of range
        KeyError - mapping (dict) key is not found in the set of existing keys
        KeyboardInterrupt - user hist interrupt key (ctrl-c)
        NameError - local or global name is not found
        OSError - function returns a system-related error
        RuntimeError - error does fall into any category
        SyntaxError 
        TypeError - function applied to an object of inapropriate type
        ValueError 
        ZeroDivisionError
    
    Handling Exceptions   
        try:
            with open('example.txt') as file_handler:
                for line in file_handler:
                    print(line)
            import something
        except OSError:
            print('An error occurred')
        except ImportError:
            print('Unknown Import!')    

    Raising Exception

        forcing an exception to occur

....

___________________________________________________________________________________

WORKING WITH FILES

    Use the / operator to join paths:
        - one of the fist two values must be a path object or it will error

    The Current Working Directory
        -get pwd as a string with Path.cwd()   *from pathlib import Path
        -os.chdir()  *import os
        -Path.home()
        -os.makedirs

    Getting Parts of a File Path
        /home/mark/spam.txt
            / = anchor
            home = parent
            spam.txt = filename

    Finding File Sizes and Folder Contents
        os.path.getsize(path) returns size of file in bytes
        os.listdir(path) returns a list of filename strings for each file
            in the path argument

    open() function argumants and defaults

        open(file, mode='r', bufferings==1, encoding=None, errors=None, newline=None,
                closefs=True, openr=None)

        only required filname or path (readonly)
        'r' = readonly (default)
        'w' = open for wriring - overwrite if exists
        'a' = open for writing - append file
        'b' = binary mode
        't' = text mode (default)
        '+' = reading and writing

        - files are normally opened in text mode - append 'b' to mode to open 
          in binary  (cannot specify encoding when opening in binary mode)

        - using with to open files will auto close them


    Multiple ways to open a file:

        file_handler = open('example.txt')
        #do somehting with the file
        file_handler.close()

      exception may occur - can use try/except finally 
      best way is to use special with statement.  With will activate 
      context manager (used when you want to set something up and 
         tear somthing down)

        with open('example.txt') as file_handler:
            #do somthing with handler here
            data = file_handler.read()

        with - generic framework for creating runtime contexts and telling
               objects theyre entering and exiting a runtime context - if the 
               object is a stream object, then it does useful things, like
               auto closing - but that behavior is defined in the stream, not 
               the with statement

    Methods of File Objects:
        f.read(size)  - reads a quantity of file contents (all if size ommitted)
                        f.read() returns an empty string of the end of the file i                       is reached
        f.readline() - reads a single line from file leaving '\n' at end
                       blank lines are denoted by '\n'
                       if end of file is reached - blank line
        f.readlines() - returns a list of strings

        f.write(string) - writes the contents of a string to a file and returns
                          the number of characters written

             ----other types need to be converted to a string or bytes before                     writing them
             EG:
                >>>value = ('the answer', 42)
                >>>s = str(value)
                >>>f.write(s)
                18

        f.tell() - returns an object giving the objects current position in the 
                   file (represented as a number of bytes from beggining in 
                   binary mode and an opaque number in text mode)



    Saving structured data with json:
        -when you need to save more complext data types like nexted lists, dicts,         etc - use data interchange format - JSON (Javascript Object Notation)

        -takes python data hierarchies and converts them to string representation
               - called SERIALIZING, 
               - recontructing the data from strings = DESERIALIZING

        EG: view x string representation 
        >>>import json
        >>>x = [1, 'simple', 'list']
        >>>json.dumps(x)
        '[1, "simple", "list"]'

        -anpother variant of the dumps() functuon, dump() simply serializes the 
         object to a text or binary file depending on mode

         load() - to decode object again




    EXAMPLE  read(), readline() and readlines()_______________________________________________________
    #!/usr/bin/env python3
    import os

    with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
        myFile.write("Some random text\nMore randomtext\nAnd some more")

    #open for reading  - does not require mode, read is default
    with open("mydata.txt", encoding="utf-8") as myFile:
        print(myFile.readlines())


    # Reading files
    # read() - read  file
    # readline() - read until first newline
    # readlines() - return a list of strings 

    __________________________________________________________________________________________________
    EXAMPLE
    #!/usr/bin/env python3
    import os

    with open("mydata2.txt", mode='w', encoding="utf-8") as myFile:
        myFile.write("some random text\nMore random text\nAnd more text")

    with open("mydata2.txt", encoding="utf-8") as myFile:
        lineNum = 1

        while True:
            line = myFile.readline()
            if not line:
                break

            print("Line", lineNum, " : ", line, end="")
            lineNum += 1

    print()

    OUTPUT:
    Line 1  :  some random text
    Line 2  :  More random text
    Line 3  :  And more text

_______________________________________________________________________________________________________




    Readig Files

        with open('example.txt') as file_handler:
            for line in file_handler:
                print(line)

            ****reads file in chunks so you wont run out of memory

        with open('example.txt') as file_handler:
            lines = file_handler.readines()
            for line in lines
                print(line)
             **** reads entire file into memory

        with oprn('example.txt') as file_handler:
            file_contents = file_handler.read()
            *****reads entire file into memory and assigns to a variable    
    
        
        read a file in smaller chunks - specify size, in bytes to read

        while True:
            with open('Example.txt', 'rb') as file_handler:
                data = file_handler.read(1024)
                if not data:
                    break
                print(data)
           ****read 1025 bytes at a time, when read returns an empty string, 
                while loop will break

        Reading Binary files

        with open('example.pdf', 'rb') as file_handler:
            file_contents = file_handler.read()

        ***** the second argument to open is rb - ro binary mode

    Writing Files

        same syntaxt with 'w' in place of 'r'
        WARNING: when using 'w' and 'wb' modes you will overwrite existing 
            files  os module os.path.exists() -> check for files existance

            >>> with open('example.txt', 'w') as file_handler:
            ...     file_handler.write('This is a test')
            ...
            14
            >>> with open('example.txt') as file_handler:
            ...     print(file_handler.read())
            ...
            This is a test
            >>>

    Seeking Within a File

        file handler has another method: seek()
        The seek() method accepts 2 arguments:
            offset - a number of bytes from whence
            whence - The reference point
                whence can be set to one of three values:
                    0 - default, beggining of file
                    1 - The cuyrrent file position
                    2 - The end of the file

        With example file, started at 4th byte:
        >>> with open('example.txt') as file_handler:
        ...     file_handler.seek(4)
        ...     chunk = file_handler.read()
        ...     print(chunk)
        ...
        4
         is a test
        This is line 2
        
     Catching File Exceptions

        usually permissions to create or edit a file:
            OSError   
        try:
            with open('example.tct') as file_handler:
                for line in file_handler:
                    print(line)
        except OSError:
            print('An error has occured')


    More Methods:
        os.rename("mydata.txt", "mydata2.txt")
        os.remove("mydata2.txt")
        os.mkdir("mydir")
        os.chdir("mydir")

        print("Current Directory: ", os.getcwd())

        os.chdir("..")
        os.rmdir("mydir")


____________________________________________________________________________________________________

IMPORTING

    common modules to import:
        argparse - create commandline interfaces
        email - create, send, and process email
        logging - create run time logs of program execution
        pathlib - work with file name and paths
        subprocess - open and interact with other processes
        sys - work with system specific functiond and information
        urllib - work with urls
       -full list
           https://docs.python.org/3/library/index.html

    import <library name>
    from <libray name> import <piece>
            eg:
                from math import sin, cos, tan
     example usinf variables (as)
        import math as m
        >>>m.sqrt(4)
        2.0

    can import everything with from ... import * 
         BEWARE (namespace contamoiniation)
        shadowing - use a variable that overwrites a functiuon you imported

____________________________________________________________________________________________________

FUNCTIONS

    -create functions with the def keyword
    -if no return value default = None
    - Type hinting - specify argunent types, even though it wont be engforced
    - mypy tool can be used to verify that type hinting is followed
    EG
        def welcome(name: str) -> None:
            print(f'Welcome {name}')
    -passing keyward arguments
        -can define defaults in arguments

    *args and **kwargs
        -*args - an arbitrary number of arguments
        -**kwargs - an arbitrary number of keyward argunments

        EG:
            >>> def output(*args, **kwargs):
            ...     print(f'{args}')
            ...     print(f'{kwargs}')
            ... 
            >>> my_tuple = (1,2,3)
            >>> my_dict = {'one': 1, 'two':2}
            >>> 
            >>> output(*my_tuple)
            (1, 2, 3)
            {}
            >>> output(my_dict)
            ({'one': 1, 'two': 2},)
            {}
            >>> 
     -positional-only parameters
        special syntax to tell Python that some parameters have to be
        positional and some have to be keywaord

        >>>def positional(name, age, /, a, b, *, key):
        ...     print(name, age, a, b, key)
        >>>positional('Mike', 17, 2, b=3, key='test')
        Mike 17 2 3 test
_______________________________________________________________________________________________

CLASSES

    OOP - class support
    python can easily be used as a functional language
    real world objects have attributes and capabilities (fields/methods)
        methods - functions that act on objects(action of the class object)
        fields - (data part) ordinary variables bound to namespaces of the  
                classes and objects
                1. class variables
                2. object variables
        ***see robot.py****
              *population belongs to Robot - class variable
              *name belongs to object(assignes with self) object variable
              *WARNING object variable with the same name as a class 
                    variable will hide the class variable
              *how_many is a method that belongs to the class - 
                    define it as a classmethod or staticmethod
              *how_many was marked as a class method using a decorator
              *decorator = shortcut to calling a wrapper function
                    how_many = classmethod(how_many)


    Class Creation:
        class - blueprint to build an object
        class Ball:
            
            def __init__(self, color, size, weight):
                """Initializer"""
                self.color = color
                self.size = size
                self.weight = weight
        EG
        >>> class Ball:
        ...     def __init__(self, color, size, weight):
        ...             self.color = color
        ...             self.size = size
        ...             self.weight = weight
        ...
        >>> beach_Ball = Ball('red', 15, 1)
        >>> print(beach_Ball)
        <__main__.Ball object at 0x72950b173e20>
        >>> print(f'My ball is {beach_Ball.color} and weighs {beach_Ball.weight}lb')
        My ball is red and weighs 1lb
        >>>
    
     -can add type hinting to your class:
            >>>class Ball:
            ...     def __init__(self, color: str, size: float, weight: float) -> None:
            self.color = color
            self.size = size
            self.weight = weight

________________________________________________________________________________________________
# ball.py

class Ball:
    def __init__(self, color:str, size:float, weight: float, ball_type:str) ->None:
        self.color = color
        self.size = size
        self.weight = weight
        self.ball = ball_type

    def bounce(self):
        if self.ball_type.lower() == 'bowling':
            print("Bowling balls can't bounce!")
        else:
            print(f"The {self.ball_type} ball is bouncing!")

if __name__ == "__main__":
    ball_one = Ball('black', 6, 12, 'bowling')
    ball_two = Ball('red', 12, 1, 'beach')

    ball_one.bounce()
    ball_two.bounce()
__________________________________________________________________________________________________________

    Puplic and Private Methods / Attributes
        
        1. public - avaialble to all of Python
        2. private - used only within the class theyre defined
        3. protected - only be used in the class theyre defines or in a sublass

        ***puplic and protected methids/attributes dont technically exists
            convention to use underscore or double underscore to signal that
            the method or attribute should be treated as a private.
        double underscore = dunder methods

        python built in magic methods:
        https://doc.python.org/3/refrence/datamodel.html

    Subclass Creation

        -inherts the attributes and methods of the class it is based on
        -can override methods and attributes of the subclass by using the same names

    EG....use ball.py to make a subclass
    ________________________________________________________________________
    #bowling ball.py
    import ball

    class BowlingBall(ball.Ball):
        def roll(self):
            print(f'You are rolling the {self.ball_type} ball')
    
    if __name__ == "__main__":
        ball = BowlingBall()
        ball.roll()
        ball.bounce()
    _______________________________________________________________________
        

    Polymorphism

        -ploymorphic classes have a shared, commonm interface(methods and attributes)
         possibly from parents via inheritance
        -abc module - Abstract Base Classes (make classes more rigid)
        -Duck Typing - if a python class had the same interface as its
                parent or similar class, then it doesnt matter if the implementation 
                underneath is different
        -__repr__() magic method - creates a nice string representation of the
                object
        eg - ball.py  - ball_printable.py
        _______________________________________________________________________

        class Ball:
            def __init__(self, color:str, size:float, weight: float, ball_type:str) ->None:
                self.color = color
                self.size = size
                self.weight = weight
                self.ball_type = ball_type

            def bounce(self):
                if self.ball_type.lower() == 'bowling':
                    print("Bowling balls can't bounce!")
                else:
                    print(f"The {self.ball_type} ball is bouncing!")

            def __repr__(self):
            return f"<Ball: {self.color} {self.ball_type} ball>"

        if __name__ == "__main__":
            ball_one = Ball('black', 6, 12, 'bowling')
            ball_two = Ball('red', 12, 1, 'beach')

            ball_one.bounce()
            ball_two.bounce()

            print(ball_one)
            print(ball_two)
        ____________________________________________________________________________

OBJECT ORIENTED PROGRAMMING
    -combine data and functionality and wrap inside somthing called an
     object
     -class creates a new type where objects are instances of the class
     -objects that store data using ordinary variables that belong to the object
                -referred to fields
                - 2 types of fields:
                    1. instance variables - belong to instance/object of class
                    2. class variables - belong to the class itself
     -Objects can also have functionality by using functions that belong to a class - referred to as methods
     -functions and methods = attributes
     
     -SELF
       -first value added to the begining of the parameter list, Python provides its value


    four major principles:
        Encapsulation - bundling of data with the methods that operate
                        on them
        Data Abstraction
        Polymorphism
        Inheritance

    Getter and Setter 
        serve important purposes in encapsulation and data validation

    INHERITANCE

        -Technically every class uses inheritance
        
        -EG:
            !/usr/bin/python3

            class Contact:
                all_contacts = []

                def __init__(self, name, email):
                    self.name = name
                    self.email = email
                    Contact.all_contacts.append(self)

            class Supplier(Contact):
                """ If some contacts are also suppliers, we can create a new
                    Supplier class that acts like a Contact but has an additional 
                    order method"""

                def order(self, order):
                    print("If this was a real system we would send {} order to {}".format(order, self.name))


            c = Contact("Some Body", "somebody@example.net")
            s = Supplier("Sup Plier", "supplier@example.net")
            print(c.name, c.email, s.name, s.email)

            s.order("I need pliers")




________________________________________________________________________________________________________
Python Algorithims:

    Bubble Sort
        numList = []
        numList.append(random.randint(1,10))
        i = len(numList) - 1
        while i > 1:
            j=0
            while j < i:
                if numList[j] > numList[j +1]:
                    temp = numList[j]
                    numList[j] = numList[j + 1]
                    numList[j + 1] = temp
                else:
                    print()
                j += 1
            i -= 1

