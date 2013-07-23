from lib import yacc
from scanner import tokens
from ast import Node
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
	p[0] = Node('IDENTIFIER', p[1])

def p_string(p):
	'''expr : STRING'''
	p[0] = Node('STRING', p[1])

def p_number(p):
	'''expr : NUMBER
			| NUMBER DOT NUMBER'''
	if len(p) == 2:
		p[0] = Node('NUMBER', p[1])
	else:
		str_num = str(p[1]) + p[2] + str(p[3])
		p[0] = Node('NUMBER', float(str_num))

def p_bool(p):
	'''expr : TRUE
			| FALSE'''
	p[0] = Node('BOOL', p[1])

def p_list(p):
	'''expr : LBRACKET parameters RBRACKET'''
	p[0] = Node('LIST', p[2])

def p_comment(p):
	'''expr : COMMENT'''
	p[0] = Node('COMMENT', p[1])

def p_binary(p):
	'''expr : expr PLUS expr
			| expr MINUS expr
			| expr TIMES expr
			| expr DIVIDE expr
			| expr MOD expr
			| expr POWER expr'''
	p[0] = Node('BINARY', p[1], p[2], p[3])

def p_unary(p):
	'''expr : expr INCREMENT
			| expr DECREMENT
			| NOT expr'''
	p[0] = Node('UNARY', p[1], p[2])

def p_assign(p):
	'''expr : IDENTIFIER EQUALS expr'''
	p[0] = Node('ASSIGN', p[1], p[3])

def p_binary_assign(p):
	'''expr : IDENTIFIER PLUSEQUAL expr
			| IDENTIFIER MINUSEQUAL expr
			| IDENTIFIER MULTIPLYEQUAL expr
			| IDENTIFIER DIVIDEEQUAL expr
			| IDENTIFIER MODEQUAL expr
			| IDENTIFIER POWEREQUAL expr'''
	p[0] = Node('BINARY_ASSIGN', p[1], p[2], p[3])

def p_comparison(p):
	'''expr : expr ISEQUAL expr
			| expr NOTEQUAL expr
			| expr LESSTHAN expr
			| expr LESSTHANEQUAL expr
			| expr GREATERTHAN expr
			| expr GREATERTHANEQUAL expr
			| expr AND expr
			| expr OR expr'''
	p[0] = Node('COMPARE', p[1], p[2], p[3])

def p_ternary(p):
	'''expr : expr QUESTION expr COLON expr'''
	p[0] = Node('TERNARY', p[1], p[2], p[3], p[4], p[5])

def p_echo(p):
	'''expr : ECHO LPAREN parameters RPAREN'''
	p[0] = Node('ECHO', p[3])

def p_open(p):
	'''expr : OPEN LPAREN parameters RPAREN'''
	p[0] = Node('OPEN', p[3])

def p_scrape(p):
	'''expr : SCRAPE LPAREN parameters RPAREN'''
	p[0] = Node('SCRAPE', p[3])

def p_block(p):
	'''block : LCURLY explist RCURLY'''
	p[0] = Node('BLOCK', p[2])

def p_parameters(p):
	'''parameters : parameters COMMA parameter 
				  | parameter'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		p[0] = Node('PARAMETERS', p[1], p[3])

def p_parameter(p):
	'''parameter : expr
				 | block'''
	p[0] = Node('PARAMETER', p[1])

def p_function(p):
	'''expr : IDENTIFIER LPAREN parameters RPAREN block'''
	p[0] = Node('FUNCTION', p[1], p[3], p[5])

def p_return(p):
	'''expr : RETURN expr'''
	p[0] = Node('RETURN', p[2])

def p_range(p):
	'''range : NUMBER ARROW NUMBER'''
	p[0] = Node('RANGE', p[1], p[3])

def p_for(p):
	'''expr : FOR IDENTIFIER IN range block
			| FOR IDENTIFIER IN IDENTIFIER block'''
	p[0] = Node('FOR', p[2], 'IN', p[4], p[5])

def p_while(p):
	'''expr : WHILE expr block'''
	p[0] = Node('WHILE', p[2], p[3])

def p_if(p):
	'''expr : IF expr block
			| IF expr block else_ifs'''
	if len(p) == 4:
		p[0] = Node('IF', p[2], p[3])
	else:
		p[0] = Node('IF', p[2], p[3], p[4])

def p_else(p):
	'''else : ELSE block'''
	p[0] = Node('ELSE', p[2])

def p_else_if(p):
	'''else_if : ELSE IF expr block'''
	p[0] = Node('ELSE IF', p[3], p[4])

def p_else_ifs(p):
	'''else_ifs : else_if
				| else_ifs else_if
				| else'''
	p[0] = p[1]

def p_throw(p):
	'''expr : THROW LPAREN expr RPAREN'''
	p[0] = Node('THROW', p[3])

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