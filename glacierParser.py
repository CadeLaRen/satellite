from lib import yacc
from meccaLexer import tokens
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

def p_error(e):
	print('error: %s' %e)

parser = yacc.yacc()

# data = open(sys.argv[1], 'r').read()

# result = parser.parse(data)
# print(result)

while True:
	try: stream = raw_input('glacierParser > ')
	except EOFError: break
	if not stream: continue
	result = parser.parse(stream)
	print result