from lib import lex

reserved = {
	'echo'  : 'ECHO',
	'def'   : 'DEF',
	'if'    : 'IF',
	'else'  : 'ELSE',
	'for'   : 'FOR',
	'while' : 'WHILE',
	'true'  : 'TRUE',
	'false' : 'FALSE',
	'in'    : 'IN',
}

tokens = [
	'IDENTIFIER',
	'STRING',
	'NUMBER',
	'EQUALS',
	'TIMES',
	'DIVIDE',
	'PLUS',
	'MINUS',
	'MOD',
	'LPAREN',
	'RPAREN',
	'LBRACKET',
	'RBRACKET',
	'LESSTHAN',
	'GREATERTHAN',
	'NOT',
	'AND',
	'OR',
	'INCREMENT',
	'DECREMENT',
	'COLON',
	'ARROW',
	'BLANKLINE',
] + list(reserved.values())

t_EQUALS = r'='
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_MOD    = r'\%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_NOT    = r'\!'
t_AND    = r'&&'
t_OR     = r'\|\|'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_COLON = r':'
t_ARROW = r'->'
t_BLANKLINE = r'^\s*\n$'

def t_IDENTIFIER(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'IDENTIFIER')
	return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_STRING(t):
	r"(?:\"([^\"]+)\"|'([^']+)')"
	t.value = t.value[1:-1]
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()
