from lib import yacc
from meccaLexer import tokens

precedence = (
	('right', 'EQUALS'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'MOD')
)

def p_explist(p):
    '''explist : 
    | explist expression'''
    if(len(p) < 3):
        p[0] = ('EXPLIST', [])
    else:
        p[1][1].append(p[2])
        p[0] = p[1]

def p_expression_number(p):
	'expression : NUMBER'
	p[0] = ('NUMBER', p[1])

def p_expression_string(p):
	'expression : STRING'
	p[0] = ('STRING', p[1])

def p_expression_identifier(p):
	'expression : IDENTIFIER'
	p[0] = ('IDENTIFIER', p[1])

def p_expression_binaryop(p):
	'''expression : expression PLUS expression
	| expression MINUS expression
	| expression TIMES expression
	| expression DIVIDE expression
	| expression MOD expression
	'''
	if (p[2] == '+'):
		p[0] = ('PLUS', p[1], p[3])
	elif (p[2] == '-'):
		p[0] = ('MINUS', p[1], p[3])
	elif (p[2] == '*'):
		p[0] = ('TIMES', p[1], p[3])
	elif (p[2] == '/'):
		p[0] = ('DIVIDE', p[1], p[3])
	elif (p[2] == '%'):
		p[0] = ('MOD', p[1], p[3])

def p_expression_echo(p):
	'expression : ECHO LPAREN expression RPAREN'
	if (p[1] == 'echo'):
		p[0] = ('ECHO', p[3])

def p_expression_parenthesized(p):
	'expression : LPAREN expression RPAREN'
	p[0] = p[2]

def p_idlist(p):
	'''idlist : 
	| idlist IDENTIFIER'''
	if (len(p) < 3):
		p[0] = ('IDLIST', [])
	else:
		p[1][1].append(p[2])
		p[0] = p[1]

def p_expression_block(p):
	'block : COLON explist BLANKLINE'
	p[0] = ('BLOCK', p[2])

def p_expression_function(p):
	'expression : DEF LPAREN idlist RPAREN block'
	p[0] = ('DEF', p[4], p[6])

def p_expression_range(p):
	'expression : NUMBER ARROW NUMBER'
	p[0] = ('RANGE', p[1], p[3])

def p_error(e):
	print('error: %s' %e)

parser = yacc.yacc()

while True:
	try: stream = raw_input('meccaParser > ')
	except EOFError: break
	if not stream: continue
	result = parser.parse(stream)
	print result