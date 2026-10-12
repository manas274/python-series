<!-- Hour 2 -->
# Object types / Data Types
- Number: 1234, 3.1654, 3+4j, 0b111, decimal(), fraction()

- String: "Hello", 'World', """Multiline String""", f"Formatted {value}"

- list : [1, 2, 3], ['a', 'b', 'c'], list(range(5))
# list Example 
<!-- mylist =[1,2,3,['a','b']]
>>> mylist
[1, 2, 3, ['a', 'b']] -->

- Tuple: (1, 2, 3), ('a', 'b', 'c'), tuple(range(5))
[brackets], (paranthesis), {curly braces}, <angle brackets>

- Dictionary: {'key1': 'value1', 'key2': 'value2'}, dict(a=1, b=2)
Dictionary have their index and value pair, key is unique and value can be duplicate.

- Set: {1, 2, 3}, {'a', 'b', 'c'}, set(range(5)) 

- file: file.txt, open('file.txt', 'r'), open('file.txt', 'w')

- Boolean: True, False, bool(1), bool(0)

- None: None, type(None)

- Function: modules, classes

- Advanced Data Types: Decorators, Generators, Iterators, Metaprogramming, Context Managers, Coroutines, Async/Await

<!-- Hour 3 -->
<!-- >>> import sys
>>> sys.getrefcount(2)
3221225472
>>> sys.getrefcount("Rafid")
3
>>> sys.getrefcount("Hi")
3
>>> sys.getrefcount(90)
3221225472 -->

#Eample 01
Python does not collect the garbage immediately
a=2
a="rafid"
a=3.14
2 and "rafid" foran garbage may nhi jayga kiunke python ko pata hai ke numbers and strings ziada use horahay hotay toh unhe thora late collect karte takay agar dobara kahin reference ajaye toh use karlen.

#Eample 02
>>> myListOne = [1,2,3]
>>> myListTwo = myListOne
>>> myListOne = "rafid"
>>> myListTwo
[1, 2, 3]

#Example 03
>>> myListOne = [1, 2, 3]
>>> myListTwo = myListOne
>>> myListOne = 'chai'
>>> myListTwo
[1, 2, 3]
>>> myListOne = [1, 2, 3] At this point, myListOne is a new list object, and myListTwo still refers to the original list object. Therefore, modifying myListOne will not affect myListTwo.
>>> myListTwo
[1, 2, 3]
>>> myListOne
[1, 2, 3]
>>> myListOne[0] = 33
>>> myListOne
[33, 2, 3]
>>> myListTwo
[1, 2, 3]

#Example 04
<!-- l1 reference sirf ek dafa hi dia hai phir usmei changes kin hain toh L2 bhi vahi changes adapt karlega -->
>>> 11 = [1, 2, 3]
>>> 12 = 11
>>> 11
[1, 2, 3]
>>> 12
[1, 2, 3]
>>> 11[0] = 44
>>> 11
[44, 2,3]
>>> 12
[44, 2,3]

<!-- List mei agar same value bhi assign karo toh vo different reference hi hoga -->
>>> p1 = [1,2,3 ]
>>> p2 = [1,2,3] 


#Slicing [0:2]
<!-- last wala (2) include nai hoga sirf 0(first element) and 1(second element) ayega -->
>>> l1=[1,2,3]
>>> l2=l1[0:2]    
>>> l2
[1, 2]
>>> l1
[1, 2, 3]
>>> 

>>> l2=l1[:]
>>> l2
[1,2,3]
<!-- SLicing mei copies banti hain agar hum l1 mei change karenge toh vo l2 mei nai ayega -->
>>> l1[0] = 33
>>> l1
[33,2,3]
BUT 
>>> l2
[1,2,3] 
<!-- l2 = l1[:] and >>> import copy >>> h2 = copy.copy(l1)  in dono ka same kaam hai bas pehle wala shortcut hai and deepcopy is used to copy internal list if present -->

# Difference b/w == and is

>>> n = [1, 2, 3]
>>> m = n
>>> m
[1,2,3]
>>> n
[1, 2,3]
<!-- to check if the values are same then we use == -->
>>> m == n 
True
<!-- to check the memory reference if they are same object in the memory  -->
>>> m is n
True
<!-- now we assign same value in n -->
>>> n = [1, 2,3]
>>> m == n
True
>>> m = [1, 2,3]
>>> m == n
True
<!-- here values are same but the reference are different now -->
>>> m is n
False

Difference b/w repr(), str() and print()
>>> repr('chai') repr() object ki developer-oriented representation deta hai — aisi representation jo object ko clearly identify kare.
"'chai'"
>>> str('chai') str() object ko human-readable form mein convert karta hai.
'chai' 
>>> print('chai') khalli walli print() function object ko console par print karta hai.
chai 


