#Satellite Programming Language

Satellite is a programming language I'm writing for fun. It's designed to be concurrent and all that jazz.

##Syntax

	# single line comments use the hash
	
	###
	block comments look like this
	###

	# assignment
	str = 'hello ' + "world"
	num = 1
	
	# math
	1 + 1   # 2
	8 - 1   # 7
	10 * 2  # 20
	2 ^ 3   # 8
	35 / 5  # 7
	35 / 4  # 8.75
	5 << 3  # 40
	40 >> 3 # 5 

	# boolean primitives
	true
	false

	# boolean operations
	!true  # false
	!false # true
	1 == 1 # true
	1 != 1 # false
	1 < 10 # true
	1 > 3  # false
	1 <= 1 # true
	1 >= 5 # false
	
	# strings
	'This is a string.'
	"So is this."
	'Concatenation ' + "is cool!"
	'Indexing'[0]    # 'I'

	# conditionals
	if a == b || b != c {
		a++
		b--
		c ^ 2
	} 
	else if a == c && a <= b {b++}
	else {c++}

	# loops
	for i in 0->100 {echo(i)}
	while true {if condition{break}}

	# lists
	list = [1, 'apple', {name: 'blah', age:23}]
	for obj in list {echo(obj)}

	# hash tables
	hash = {a: 1, b: 2}
	for (key, value) in hash {echo(key, value)}

	#list comprehension
	['a', 'b', 'c'] + [1, 2, 3]    # ['a', 'b', 'c', 1, 2, 3]
	[x*2 | x <- [1->5]]            # [2, 4, 6, 8, 10]
	[x*2 | x <- [1->5] if x*2 > 4] # [6, 8, 10]

	# question mark for existence
	if elvis? {echo('he lives')}
	
	# functions
	max(x, y) {return x > y ? x : y}
	echo(max(a, b))

	# classes
	Cube {
		init() {
			self.length = 1
			self.width  = 1
			self.height = 1
		}		
		# overloaded constructor
		init(l, w, h) {
			self.length = l
			self.width  = w
			self.height = h
		}
		getVolume() {
			return self.length * self.width * self.height
		}
	}

	defaultCube = new Cube()
	myCube      = new Cube(1, 2, 3)
	
	defaultCube.getVolume() # 1
	myCube.getVolume()      # 6
	
	myCube.description = 'New attribute on myCube!'
	
	echo(myCube) 
	###
	{
		length: 1,
		width: 2,
		height: 3,
		description: 'New attribute on myCube!'
	}
	###

Concurrency example!

	# use << >> to fire off background threads
    <<
    	Universe {
			calibrate() {
				# long calculations
				self.physics = physics
			}
    	}
		
		universe = new Universe()
		<<		
			universe.calibrate()
			echo('This is printed second!')
			echo(universe.physics)
		>>
		echo('This is printed first!')
	>>