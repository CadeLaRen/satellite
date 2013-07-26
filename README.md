#Glacier Programming Language

Glacier is a programming language I'm writing for fun. It's designed to be a sleek and sexy web scraping language.

##Syntax
No semi colons needed. Use echo to print to standard out.

####Strings

Either single or double quotes can be used for strings.

	str = 'Hello ' + "World"

####Numbers
	x = 1
	y = 2.3

####Lists
	list = [a, 'hello', 23]

####Operators
	+, -, *, /, %, **, ++, --

####Comparisons
	==, !=, <, <=, >, >=, ||, &&

####Booleans
all empty things are treated as false, non-empty things are true

	'', 0, nil, [], false, true

####Conditionals
	
	if a < b {
		a++
	}
	else {
		b++
	}
	
	if a < b {a++}
	else {b++}

Ternary statement
	
	a < b ? a++ : b++

####Loops
	
	x = 0
	while x < 100 {
		x++
	}

use start->end to designate a range.
	
	for i in 0->100 {
		echo(i)
	}

	for i in 100->0 {echo(i)}

	//even numbers
	for i in 0->100->2 {echo(i)}
	

####Functions

	max(a, b) {
		return a > b ? a : b
	}

	echo(max(23, 42))

##Scraping

	page = open('http://www.example.com', {if (error) {throw(error)}})

	scrape(page, {
		links     = this.all('a')      // => ['<a href="google.com">Google</a>', '<a href="amazon.com">Amazon</a>']	
		linkNames = links.text()       // => ['Google', 'Amazon']
		linkHrefs = links.get('href')  // => ['google.com', 'amazon.com']

		pages = []

		for link in linkHrefs {
			newPage = open(link)
			pages.push(newPage)
		}


		emails     = this.all(r'/^(\w[-._+\w]*\w@\w[-._\w]*\w\.\w{2,3})$/') 
									// => ['blah@gmail.com', 'hello@world.com', 'foo@bar.com']
		firstEmail = emails.first() // => 'blah@gmail.com'
		lastEmail  = emails.last()  // => 'foo@bar.com'
	})