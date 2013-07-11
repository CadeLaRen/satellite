from lib import yacc
from meccaLexer import tokens

precedence = (
	('right', 'EQUALS'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'MOD')
)

def p_explist(p):
    '''explist : 
    | explist expr'''
    if(len(p) < 3):
        p[0] = ('EXPLIST', [])
    else:
        p[1][1].append(p[2])
        p[0] = p[1]

def p_type(p):
	'''type : INT
			| FLOAT
			| DOUBLE
			| STRING
			| BOOL'''

	p[0] = p[1]

def p_expr_number(p):
	'''expr : NUMBER'''
	p[0] = p[1]

def p_expr_string(p):
	'''expr : STRING'''
	p[0] = p[1]

def p_expr_identifier(p):
	'''expr : IDENTIFIER'''
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

def p_expr_initialize(p):
    '''expr : type IDENTIFIER EQUALS expr'''
    p[0] = ('INITIALIZE', p[1], p[2], p[4])

def p_expr_assign(p):
	'''expr : IDENTIFIER EQUALS expr'''
	p[0] = ('ASSIGN', p[1], p[3])

def p_return_statement(p):
	'''return_statement : RETURN expr
						| RETURN'''
	p[0] = ('RETURN', p[2])

def p_parameter(p):
	'''parameter : IDENTIFIER'''
	p[0] = p[1]

def p_parameters(p):
	'''parameters : parameters COMMA parameter
  				  | parameter'''
	if len(p) == 4:
		p[0] = p[1] + [p[3]]
	else:
		p[0] = [p[1]]

def p_function_declaration_statement(p):
	'''statement : type IDENTIFIER LPAREN parameters RPAREN COLON explist return_statement'''
	p[0] = ('FUNCTION', p[2], p[4], p[7], p[8])

def p_for_statement(p):
	'''statement : FOR expr IN range COLON explist COLON'''
	p[0] = ('FOR', p[2], p[4], p[6])

def p_range(p):
	'''range : NUMBER ARROW NUMBER'''
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