# source

https://www.w3schools.com/python/


# notes

- relesaed in 1991 by Dutch programmer
- can be written as procedural, OOP and functional
- new line means end of command for this line
- print("hey", end=" ") => you can end the print with any character. in this example it is white space.
- print(2+2, "2 + 2", 2*3) => prints: 4 2 + 2 6        (see that it puts white space between them)
- cast by str(), int(), float(). check the type by type(x)
- cannot use these as variable names: 2myvar = "John"       my-var = "John"          my var = "John"

- pascal case: MyNameIsYusuf
- snake case: my_name_is_yusuf (mostly used in python)
- you can define a global value also in a function by global x; x = 5;  But that function must be called before that value is used.

- built-in data types:
- str, int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType
- there is no char type, it is simply a str with length 1
- "str1" in "str2" returns true if str1 is in str2  or false
- "str1" not in "str2"
- slicing: x[2:5] means start from 2 to 5 but 5 is not inclusive
- slicing counting backwards: x[-5:-2] means from last 5th to last 2
- in python, we cannot combine string and int like in java
- can do formating like f"my name is {name}",  f"the price is {price:.2f} dollars"
- some values are false: "", 0, (), [], {}, None
- isinstance(x, int) returns true or false

- / always return float. for float division use //
- you can chain like 1 < x < 10
- logical operators: and, or, not
- x is y: return True if x and y pointing to the same object
- in python x == y is True even these are two different object with same list content
- x in y: returns True if x is included in y.

- list: changable, ordered, allows duplicate
- tupple: unchangable, ordered, allows duplicate
- set: unchangable(* you cannot modify item, but add or remove), unordered, no duplicate
- dictionary: changable, ordered, no duplicate

- some_list[2:5] => returns a new list from item 2 to item 5 (exclusive)
- some_list.insert(index, item), some_list.append(item)
- some_list.extend(another_list | tupple | dict): add given items to our list
- some_list.remove(item): removes the first occurence
- some_list.pop(index): remove the item with this index         same as del some_list[index]
- some_list.pop() remove the last item
- del some_list: delete the entire list
- some_list.clear(): clear the entire list
- list comprehension:   y = [item for item in list if "a" in item]
- some_list.reverse(): reverse the list
- some_list.copy(): to copy a list      or use another_list = list(some_list)
- some_list.sort(): sort a list
- some_list.sort(reverse=True): sort descending
- some_list.sort(key = my_func): sort according to my_func
- sort function first sorts capitalized chars, to avoid this you can use some_list.sort( key = str.lower)

- you can merge lists by + operator
- tuples mostly used by returning multiple values even though list can be used too.
- tuples are unchangable version of lists, but they are faster. To be on the safe side if the data will not change use tuple then
- my_tuple * 2, appends itself to the end


- True and 1 is consideres as same value in sets, be careful! Samewise, False and 0 treated as same value.
- my_set.update(another_set | tuple | list): include them to the set
- my_set.add(item): add an item
- my_set.remove(item) to remove an item, this will raise an error if the value is not in the set, use discard() instead
- my_set.union(another_set+): take the union, you can also do this by union_set = my_set | another_set
- my_set.intersection(another_set): returns the intersection, you can also use & operand
- my_set.intersection_update(another_set): this does not return, directly updates the set
- my_set.difference(another_set): returns only different items in my_set, or you can use - operand
- my_set.smyetric_difference(another_set): returns only different items in both sets, you can use ^ operand
- frozenset is the immutable version of normal sets

- dicts are changable, ordered (after 3.7) and no duplicate. If you have duplicate, last one will overrite the prvious value
- the len of a dict is number of key-value pairs
- data types in dict are: str, int, bool, list, tuple, set etc. (json cannot have some of them, need coverting)
- you can access the value whether by my_dict["key"] or by my_dict.get("key")
- my_dict.keys(): returns all kinds of keys as list, if the dict updated, this value is also updated (pointer)
- my_dict.values(): returns all values as a list, if the dict updated, this value is also updated (pointer)
- my_dict.items(): returns key value pairs as tuples as list
- my_dict.pop("key"): pop a key value pair
- my_dict.popitem(): pop the last inserted pair


- one line if else: dosomething if condition else dosomething2
- use pass to fill empty if content, generally used in TODO for the content
- for loop is used iterating through a sequence, use while if you dont have a sequence list
- you can use range(stop) to iterate over a sequence from starting 0 to stop (exlusive). you can start also what you want: range(start, stop) You can also set increment value: range(start, stop, increment_value)

- total = sum(x * x for x in range(10000000000)): this is a generator expression, which means it does not create all numbers in the memory, it create one and sum immediately. This saves you from out of memory problems.
- however if you try this:total = sum([x * x for x in range(100000000)]) you will be out of memory since python try to create a list with these items.

- you can also create generator like this: 
def gen_seq():
    
    i = 0
    while i < 100:
        yield i
        i +=2


- here yield keyword is similar to return, but it only pauses the code until next() function is called. So it does not store these values altogether.
- so generators are like a function definition in math

- for _ in range(x): when you dont need the iterator value, for readibility use "_" char
- range is a special data type. You cannot display it directly, you can by print(list(range_object))
- you can do slice operations like range_object[2:67], range_object[2]
- 6 in range_object: returns True or False to check membership
- lists are iterable but not iterator: which means it does not have next() function. to use next() function you should first make it iterator iter(some_list), then you can use next()
- or you can use generators because calling a generator function returns an iterator.
- or you can create your own iterator by creating a class with __init__() and __next__() functions

-in python, there are modules which means .py files. If you want to use it, write import module_name Then, you can use a function or variable in that module by module_name.function_name() or module_name.variable_name
- you can also make an alias for that module_name while importing: import module_name as alias_name Then you can use it as alias_name.function_name() etc.
- you can also only import what you want by using: from module_name import class_or_function_or_variable_name, after this you dont have to write module name while accessing.
- dir(module_name) shows all functions and variables in that module

- you can get date and time by: x = datetime.datetime.now(), then you can access specifically by x.hour, x.minute etc.
- from datetime import datetime: here, first one is module name, and the second one is a class. you create and object/instance of that class by calling its construction function: x = datetime(2001, 1,1) Then you can print that object as what format you want by using the x.strftime("format_symbols")


- using import json, you can convert json (string) to dict: y = json.loads(some_string)    or  you can convert dict to json (string): y = json.dumps(some_dict)
- when you convert dict to json: True => true, None => null, tuple,set,list => list
- so it is easy to load or write dict data types from/to files. the thing is it is not straigthforward to load/write and object! To do that implement to_dict() and from_dict() in that class. Then you can use above method now. So you can now store and object as json. This is called SERIALIZATION. And inverse is called DESERIALIZATION. Be careful, if you have non-friendly json data in the object like datetime, you should make it JSON-friendly while implementing to_dict() function. For example you can convert datetime object to string.

- in python, you can install packages using pip. For security reasons, Debian based OS does not let system wide python packages installed. Therefore we have to create virtual environment: which means project specific environment. write this: python3 -m venv venv, then vscode will see the venv and ask you to change python interpreter to that folder and done. Every time you create a new terminal, you'll see (venv) text at the beginning of the terminal. If you dont see it, write source venv/bin/activate and done.
- make sure python interpreter is selected as ./venv/bin/python
- do not forget to add __pycache__ and venv folder to gitignore. Do not commit them. Instead you can create a requirements.txt so other users can download necessary python packages using pip install -r requirements.txt

- a function without a return statement returns None.
