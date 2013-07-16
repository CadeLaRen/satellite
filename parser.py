from lib import yacc
from scanner import tokens
import sys

precedence = (
	('left', 'COMMA'),
	('right', 'ECHO'),
	('left', 'EQUALS', 'PLUSEQUAL', 'MINUSEQUAL', 'MULTIPLYEQUAL', 'DIVIDEEQUAL', 'MODEQUAL', 'POWEREQUAL'),
	('left', 'QUESTION', 'COLON'),
	('left', 'OR', 'AND'),
	('nonassoc', 'ISEQUAL', 'NOTEQUAL'),
	('nonassoc', 'LESSTHAN', 'LESSTHANEQUAL', 'GREATERTHAN', 'GREATERTHANEQUAL'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'MOD'),
	('right', 'NOT'),
	('right', 'INCREMENT', 'DECREMENT')
)

def p_explist(p):
    '''explist : 
    | explist expr'''
    if len(p) < 3:
        p[0] = ('EXPLIST', [])
    else:
        p[1][1].append(p[2])
        p[0] = p[1]

def p_identifier(p):
	'''expr : IDENTIFIER'''
	p[0] = ('IDENTIFIER', p[1])

def p_string(p):
	'''expr : STRING'''
	p[0] = ('STRING', p[1])

def p_number(p):
	'''expr : NUMBER
			| NUMBER DOT NUMBER'''
	if len(p) == 2:
		p[0] = ('NUMBER', p[1])
	else:
		str_num = str(p[1]) + p[2] + str(p[3])
		p[0] = ('NUMBER', float(str_num))

def p_bool(p):
	'''expr : TRUE
			| FALSE'''
	p[0] = ('BOOL', p[1])

def p_list(p):
	'''expr : LBRACKET parameters RBRACKET'''
	p[0] = ('LIST', p[2])

def p_comment(p):
	'''expr : COMMENT'''
	p[0] = ('COMMENT', p[1])

def p_binary(p):
	'''expr : expr PLUS expr
			| expr MINUS expr
			| expr TIMES expr
			| expr DIVIDE expr
			| expr MOD expr
			| expr POWER expr'''
	p[0] = ('BINARY', p[1], p[2], p[3])

def p_unary(p):
	'''expr : expr INCREMENT
			| expr DECREMENT
			| NOT expr'''
	p[0] = ('UNARY', p[1], p[2])

def p_assign(p):
	'''expr : IDENTIFIER EQUALS expr'''
	p[0] = ('ASSIGN', p[1], p[3])

def p_binary_assign(p):
	'''expr : IDENTIFIER PLUSEQUAL expr
			| IDENTIFIER MINUSEQUAL expr
			| IDENTIFIER MULTIPLYEQUAL expr
			| IDENTIFIER DIVIDEEQUAL expr
			| IDENTIFIER MODEQUAL expr
			| IDENTIFIER POWEREQUAL expr'''
	p[0] = ('BINARY_ASSIGN', p[1], p[2], p[3])

def p_comparison(p):
	'''expr : expr ISEQUAL expr
			| expr NOTEQUAL expr
			| expr LESSTHAN expr
			| expr LESSTHANEQUAL expr
			| expr GREATERTHAN expr
			| expr GREATERTHANEQUAL expr
			| expr AND expr
			| expr OR expr'''
	p[0] = ('COMPARE', p[1], p[2], p[3])

def p_ternary(p):
	'''expr : expr QUESTION expr COLON expr'''
	p[0] = ('TERNARY', p[1], p[2], p[3], p[4], p[5])

def p_echo(p):
	'''expr : ECHO LPAREN parameters RPAREN'''
	p[0] = ('ECHO', p[3])

def p_block(p):
	'''block : LCURLY explist RCURLY'''
	p[0] = p[2]

def p_parameters(p):
	'''parameters : parameters COMMA parameter 
				  | parameter'''
	if len(p) == 4:
		p[0] = p[1] + [p[3]]
	else:
		p[0] = [p[1]]

def p_parameter(p):
	'''parameter : expr'''
	p[0] = p[1]

def p_function(p):
	'''expr : IDENTIFIER LPAREN parameters RPAREN block'''
	p[0] = ('FUNCTION', p[1], p[3], p[5])

def p_return(p):
	'''expr : RETURN expr'''
	p[0] = ('RETURN', p[2])

def p_range(p):
	'''range : NUMBER ARROW NUMBER'''
	p[0] = ('RANGE', p[1], p[3])

def p_for(p):
	'''expr : FOR IDENTIFIER IN range block
			| FOR IDENTIFIER IN IDENTIFIER block'''
	p[0] = ('FOR', p[2], 'IN', p[4], p[5])

def p_while(p):
	'''expr : WHILE expr block'''
	p[0] = ('WHILE', p[2], p[3])

def p_if(p):
	'''expr : IF expr block
			| IF expr block else_ifs'''
	if len(p) == 4:
		p[0] = ('IF', p[2], p[3])
	else:
		p[0] = ('IF', p[2], p[3], p[4])

def p_else(p):
	'''else : ELSE block'''
	p[0] = ('ELSE', p[2])

def p_else_if(p):
	'''else_if : ELSE IF expr block'''
	p[0] = ('ELSE IF', p[3], p[4])

def p_else_ifs(p):
	'''else_ifs : else_if
				| else_ifs else_if
				| else'''
	p[0] = p[1]


def p_error(e):
	print('error: %s' %e)

parser = yacc.yacc()

if len(sys.argv) == 2:
	data = open(sys.argv[1], 'r').read()
	print('-----------------------------------')
	print(data)
	print('-----------------------------------')
	result = parser.parse(data)
	print(result)
else:
	while True:
		try: stream = raw_input('glacier > ')
		except EOFError: break
		if not stream: continue
		result = parser.parse(stream)
		print result