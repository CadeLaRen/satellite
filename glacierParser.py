from lib import yacc
from glacierLexer import tokens
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
    if(len(p) < 3):
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

def p_comment(p):
	'''expr : COMMENT'''
	p[0] = ('COMMENT', p[1])

def p_assign(p):
	'''expr : IDENTIFIER EQUALS expr'''
	p[0] = ('ASSIGN', p[1], p[3])

def p_error(e):
	print('error: %s' %e)

parser = yacc.yacc()

data = open(sys.argv[1], 'r').read()

print('-----------------------------------')
print(data)
print('-----------------------------------')
result = parser.parse(data)
print(result)

# while True:
# 	try: stream = raw_input('glacierParser > ')
# 	except EOFError: break
# 	if not stream: continue
# 	result = parser.parse(stream)
# 	print result