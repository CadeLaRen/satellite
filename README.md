#Mecca Programming Language

Mecca is a programming language I'm writing for fun. It's designed to be a sleek and sexy object oriented scripting language. 

##Syntax
No semi colons needed. Use echo to print to standard out.

####Strings

Either single or double quotes can be used for strings.
	
	echo 'Hello ' + "World"

####Numbers
	x = 1
	y = 2

####Operators
	+, -, *, /, %, **, ++, --

####Comparisons
	==, !=, <, <=, >, >=, ||, &&

####Booleans
all empty things are treated as false, non-empty things are true

	'', 0, nil, [], false, true

####Conditionals
use colons to denote end of if statements
	
	if a < b:
		a++
	else:
		b++

Can be written inline
	
	if a < b: a++
	else: b++

Ternary statement
	
	a < b ? a++ : b++

####Loops
	
	x = 0
	while true:
		x += 1

use start->end->step to designate a range. Step is optional and is 1 if not stated.
	
	for i in 0->100:
		echo i

	//even numbers
	for i in 0->100->2:
		echo i

You can loop through lists.
	
	list = [1, 2, 3]
	for i in list:
		echo i*3

####Lists
Lists can contain any type of object or declaration
	
	list = [1, 1+1, functionThatReturns(3), 'four']

List comprehensions are sexy
	
	list = [2**i for i in 1->10]

####Functions
Return statements are not needed. The last evaluated expression of the funtion is returned automatically.

	def max(a, b):
		a > b ? true : false
