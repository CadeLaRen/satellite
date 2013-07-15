from lib import yacc
from meccaLexer import tokens
import sys

precedence = (
	('right', 'EQUALS'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'MOD'),
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

data = open(sys.argv[1], 'r').read()

result = parser.parse(data)
print(result)

# while True:
# 	try: stream = raw_input('meccaParser > ')
# 	except EOFError: break
# 	if not stream: continue
# 	result = parser.parse(stream)
# 	print result