from lib import yacc
from meccaLexer import tokens

precedence = (
	('right', 'EQUALS'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'MOD')
)

def p_explist(p):
    '''exprlist : 
    | exprlist expr'''
    if(len(p) < 3):
        p[0] = ('EXPRLIST', [])
    else:
        p[1][1].append(p[2])
        p[0] = p[1]

def p_type(p):
	'''type : INT
			| FLOAT
			| DOUBLE
			| STRING'''

	p[0] = p[1]

def p_number(p):
	'''expr : NUMBER'''
	p[0] = p[1]

def p_string(p):
	'''expr : STRING'''
	p[0] = p[1]

def p_expr_binary(p):
	'''expr : expr PLUS expr
			| expr MINUS expr
			| expr TIMES expr
			| expr DIVIDE expr
			| expr MOD expr'''
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

def p_expr_assign(p):
    '''expr : type IDENTIFIER EQUALS expr'''
    p[0] = ('ASSIGN', p[1], p[2], p[4])

def p_error(e):
	print('error: %s' %e)

parser = yacc.yacc()

while True:
	try: stream = raw_input('meccaParser > ')
	except EOFError: break
	if not stream: continue
	result = parser.parse(stream)
	print result