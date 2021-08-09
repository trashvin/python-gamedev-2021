# intro to python

## basic data types

```
# to determine the type of the variable, use type(..)

type(1)
type('hello')
type(1.4)
type(True)
type(a_variable)
```
```
# converting 1 data type to the other

x = 1
type(x)
# will print int

y = float(x)
type(y)
# will print float

z = bool(123)
print(z)
# will print True

type(z)
# will print boolean

n = bool(0)
print(n)
# will print False

m = bool(-2)
print(m)
# will print True

res = str(12)
print(res)
# will print '12'

type(res)
# will print str
```

## comparison and logic operators
### comparison operators

```
# == checks for equality
res = 5 == 5

# < less than
res = 3 < 5

# > greater than
res = 10 > 2

# >= greater than or equal
res = 5 >=2

# <= less than or equal
res = 2 <= 2

# != not equal
res = 5 != 6
```

### logical operators
```
# and
res = True and True

# or
res = True or False

# not
res = not True
```

## conditional if statements

```
# syntax

if <condition>:
    <action>

if <condition>:
    <action>
else:
    <action>

if <condition>:
    <action>
elif <condition>:
    <action>
else:
    <action>
```

## loops

### while loops

```
# syntax

while <condition>:
    <action>

```
```
# example

counter = 1
while counter < 10:
    print(counter)
    counter +=1
```

### for loops
```
# syntax

for <var> in range(<start>,<end+1>):
    <action>


for <var> in <var>:
    <action>
```

```
# examples

for counter in range(0, 10):
    print(counter)


readings = [1.2 , 4.7, 5.9, 2.6]
for value in readings:
    print(value)

```

## functions

a function is a block of code which only runs when it is called. you can pass data, known as parameters, into a function. a function can return data as a result.

```
# syntax

def <function name>([<paramer list...>]):
    <action>
    return [<return value>]
```
```
# example

def do_nothing():
    # this function does not do anyting, it can serve as a placeholder
    # use the 'pass' keyword to indicate that the function doesnt do anything
    pass


def add_numbers(first_num , second_num):
    return first_num + second_num

sum = add_numbers(3, 6)

# default values 

def multiply(first_num, second_num = 1)
    return first_num * second_num

prod = multiply(4,3)
prod = multiply(5)


# type hinting
# a formal solution to statically indicate the type of a value within your Python code.
# introduced in python 3.5 and specified in PEP 484
# help catch errors , improve linters ability to detect possible errors, improve your code readability

def greet(name: str) -> str:
    return "Hello, " + name

def add_integer( num_1 : int , num_2 : int) -> int:
    return num_1 + num_2

# can you still pass floats to add_integer ? Yes :(

```

## list

lists are used to store multiple items in a single variable.

```
my_list = ["apple", "banana", "cherry"]

print(my_list)

# can allow duplicates
this_list = ["apple", "banana", "cherry", "apple", "cherry"]

print(len(this_list))

# list can contain different data

list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]

# list can be accessed via index
this_list = ["apple", "banana", "cherry"]
print(this_list[1])
print(this_list[-1])
print(this_list[-2])

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[:4])

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:])

# appending data to a list
this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print(this_list)

this_list = ["apple", "banana", "cherry"]
this_list.insert(1, "orange")
print(this_list)

# removing an item

this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list)

# unlike remove, pop returns the item that was removed

this_list = ["apple", "banana", "cherry"]
this_list.pop(1)

this_list = ["apple", "banana", "cherry"]
this_list.pop()
```

## reading assignment
- list comprehension
- dictionary
- tuples


