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

##Scraping

	page = open('http://www.example.com', {if (error) {return false}})

	scrape(page, {
		links = all('a')
		//links = ['<a href="#">First Link</a>', '<a href="#">Second Link</a>']
		
		linkNames = links.text()
		//linkNames = ['First Link', 'Second Link']
		
		linkHrefs = links.get('href')
		//linkHrefs = ['#', '#']

		pages = []

		for link in all('a').get('href') {
			newPage = open(link, if (error) {return false})
			pages.push(newPage)
		}

		//pages = ['<html></html>', '<html></html>']

		emails = all(r'/^(\w[-._+\w]*\w@\w[-._\w]*\w\.\w{2,3})$/')
		//emails = ['blah@example.com', 'hello@world.com']

		firstEmail = emails.first()
		//firstEmail = ['blah@example.com']
	})