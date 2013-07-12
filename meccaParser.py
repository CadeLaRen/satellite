from lib import yacc
from meccaLexer import tokens

precedence = (
	('right', 'EQUALS'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'MOD')
)

class Expr: pass

class Variable(Expr):
	def __init__(self, type, value):
		self.type = type
		self.value = value

class Int(Expr):
	def __init__(self, value):
		self.type = 'int'
		self.value = value

class Double(Expr):
	def __init__(self, value):
		self.type = 'double'
		self.value = value

class String(Expr):
	def __init__(self, value):
		self.type = 'string'
		self.value = value

class Bool(Expr):
	def __init__(self, value):
		self.type = 'bool'
		self.value = value

class List(Expr):
	def __init__(self, value):
		self.type = 'list'
		self.value = value

class BinaryExpr(Expr):
	def __init__(self, left, op, right):
		self.type = 'binary'
		self.left = left
		self.op = op
		self.right = right

class UnaryExpr(Expr):
	def __init__(self, value, op):
		self.type = 'unary'
		self.value = value
		self.op = op

def p_type(p):
	'''type : INT
			| DOUBLE
			| STRING
			| BOOL
			| LIST'''

	p[0] = p[1]

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
			| DOUBLE
			| STRING
			| BOOL
			| LIST'''

	p[0] = p[1]

def p_expr_int(p):
	'''expr : NUMBER'''
	p[0] = vars(Int(p[1]))

def p_expr_double(p):
	'''expr : NUMBER DOT NUMBER'''
	val = str(p[1]) + '.' + str(p[3])
	p[0] = vars(Double(val))

def p_expr_string(p):
	'''expr : STRING'''
	p[0] = vars(String(p[1]))

def p_expr_bool(p):
	'''expr : TRUE
			| FALSE'''
	p[0] = vars(Bool(p[1]))

def p_expr_list(p):
	'''expr : LBRACKET parameters RBRACKET'''
	p[0] = vars(List([p[2]]))

def p_expr_identifier(p):
	'''expr : IDENTIFIER'''
	p[0] = vars(Variable(p[1]))

def p_expr_binary(p):
	'''expr : expr PLUS expr
			| expr MINUS expr
			| expr TIMES expr
			| expr DIVIDE expr
			| expr MOD expr
			| expr POWER expr'''
	if len(p) == 4:
		p[0] = vars(BinaryExpr(p[1], p[2], p[3]))

def p_expr_unary(p):
	'''expr : expr INCREMENT
			| expr DECREMENT
			| NOT expr'''
	p[0] =  vars(UnaryExpr(p[1], p[2]))

def p_expr_comparison(p):
	'''expr : expr LESSTHAN expr
			| expr GREATERTHAN expr
			| expr LESSTHANEQUAL expr
			| expr GREATERTHANEQUAL expr
			| expr ISEQUAL expr
			| expr NOTEQUAL expr
			| expr AND expr
			| expr OR expr'''
	p[0] = ('COMPARE', p[1], p[2], p[3])

def p_expr_initialize(p):
    '''expr : type IDENTIFIER EQUALS expr'''
    p[0] = ('INITIALIZE', vars(Variable(p[1], p[2])), p[4])

def p_expr_assign(p):
	'''expr : IDENTIFIER EQUALS expr'''
	p[0] = ('ASSIGN', p[1], p[3])

def p_return_statement(p):
	'''return_statement : RETURN expr
						| RETURN'''
	if len(p) == 3:
		p[0] = ('RETURN', p[2])
	else:
		p[0] = p[1]

def p_parameter(p):
	'''parameter : IDENTIFIER
				 | STRING
				 | NUMBER
				 | expr'''
	p[0] = p[1]

def p_parameters(p):
	'''parameters : parameters COMMA parameter
  				  | parameter'''
	if len(p) == 4:
		p[0] = p[1] + [p[3]]
	else:
		p[0] = [p[1]]

def p_function_declaration(p):
	'''expr : type IDENTIFIER LPAREN parameters RPAREN COLON explist return_statement'''
	p[0] = (p[1], p[2], p[4], p[7], p[8])

def p_for(p):
	'''expr : FOR expr IN range COLON explist
			| FOR expr IN expr COLON explist'''
	p[0] = ('FOR', p[2], p[3], p[4], p[6])

def p_while(p):
	'''expr : WHILE expr COLON explist'''
	p[0] = ('WHILE', p[2], p[4])

def p_range(p):
	'''range : NUMBER ARROW NUMBER
			 | NUMBER ARROW NUMBER ARROW NUMBER'''
	if len(p) == 4:
		p[0] = ('RANGE', p[1], p[3])
	else:
		p[0] = ('RANGE', p[1], p[3], p[5])

def p_expr_paranthesized(p):
	'''expr : LPAREN parameters RPAREN'''
	p[0] = p[2]

def p_echo_statement(p):
	'''expr : ECHO LPAREN parameters RPAREN'''
	p[0] = ('ECHO', p[3])

def p_if(p):
	'''expr : IF expr COLON explist
			| IF expr COLON explist ELSE COLON explist'''
	if len(p) == 5:
		p[0] = ('IF', p[2], p[4])
	else:
		p[0] = ('IF', p[2], p[4], 'ELSE', p[7])

def p_error(e):
	print('error: %s' %e)

parser = yacc.yacc()

while True:
	try: stream = raw_input('meccaParser > ')
	except EOFError: break
	if not stream: continue
	result = parser.parse(stream)
	print result