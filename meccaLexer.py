from lib import lex

reserved = {
	'echo' : 'ECHO',
	'def'  : 'DEF',
	'if'   : 'IF',
	'else' : 'ELSE',
	'for'  : 'FOR',
	'while': 'WHILE',
}

tokens = [
	'IDENTIFIER',
	'STRING',
	'NUMBER',
	'EQUALS',
	'LPAREN',
	'RPAREN',
] + list(reserved.values())