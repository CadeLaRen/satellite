#Glacier Programming Language

Glacier is a programming language I'm writing for fun. It's designed to be a sleek and sexy web scraping slanguage.

##Syntax

	str = 'hello' + " world"

	/*
		str[0] => 'h'
		str[-1] => 'd'
		str[-1 -> 0] => 'dlrow olleh'
	*/

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
	else {echo('howdy')}

	max(x, y) {return x > y ? x : y}
	echo(max(a, b))
