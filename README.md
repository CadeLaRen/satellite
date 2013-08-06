#Glacier Programming Language

Glacier is a programming language I'm writing for fun. It's designed to be concurrent and all that jazz.

##Syntax

	//intro.gl
	str = 'hello ' + "world"
	
	a = 1
	b = 2.3
	c = 45

	if a == b || b != c {a++} 
	else if a == c && a <= b {b++}
	else {c++}

	for i in 0->100 {echo(i)}

	list = [1, 'apple', {name: 'blah', age:23}]
	for obj in list {echo(obj)}

	if elvis? {echo('he lives')}

	max(x, y) {return x > y ? x : y}
	echo(max(a, b))

use << >> to designate concurrency. Top level brackets are optional if no background threads are needed.

	//concurrency.gl
    << 
    	Universe() {
			public:
				calibrate() {
					//long calculations
					return (god, physics)
				}
			private:
				god = 0
				physics = 0
    	}
		
		universe = new Universe()
		<<
			universe.calibrate()
			echo('This is printed second!')
		>>
		echo('This is printed first!')
	>>