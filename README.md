#Mecca Programming Language

Mecca is a programming language I'm writing for fun. It's designed to be a sleek and sexy object oriented scripting language. 

##Syntax
No semi colons needed. Use echo to print to standard out.

####Strings

Either single or double quotes can be used for strings.

	string str = 'Hello ' + "World"

####Numbers
	int x = 1
	double y = 2.3

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
	
	int x = 0
	while x < 100:
		x++

use start->end to designate a range.
	
	for i in 0->100:
		echo(i)

####Functions

	int max(a, b):
		return a > b ? a : b
		