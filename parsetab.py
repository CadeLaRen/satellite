
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'q\x9a\xc2{H\xcds\xa2\x05\xd7\xe5?\xdf>B\xfb'
    
_lr_action_items = {'DIVIDE':([2,3,6,7,11,18,19,20,21,22,23,24,25,27,32,34,],[-4,-3,-5,12,12,-17,12,-12,-9,-8,12,12,-10,-11,-16,-15,]),'RPAREN':([2,3,6,11,18,19,20,21,22,23,24,25,26,27,28,30,32,34,],[-4,-3,-5,20,-17,27,-12,-9,-8,-6,-7,-10,-13,-11,29,-14,-16,-15,]),'STRING':([0,1,2,3,5,6,7,10,12,13,14,15,16,18,20,21,22,23,24,25,27,31,32,33,34,],[-1,2,-4,-3,2,-5,-2,2,2,2,2,2,2,-17,-12,-9,-8,-6,-7,-10,-11,-1,-16,2,-15,]),'TIMES':([2,3,6,7,11,18,19,20,21,22,23,24,25,27,32,34,],[-4,-3,-5,13,13,-17,13,-12,-9,-8,13,13,-10,-11,-16,-15,]),'ARROW':([3,],[9,]),'NUMBER':([0,1,2,3,5,6,7,9,10,12,13,14,15,16,18,20,21,22,23,24,25,27,31,32,33,34,],[-1,3,-4,-3,3,-5,-2,18,3,3,3,3,3,3,-17,-12,-9,-8,-6,-7,-10,-11,-1,-16,3,-15,]),'ECHO':([0,1,2,3,5,6,7,10,12,13,14,15,16,18,20,21,22,23,24,25,27,31,32,33,34,],[-1,4,-4,-3,4,-5,-2,4,4,4,4,4,4,-17,-12,-9,-8,-6,-7,-10,-11,-1,-16,4,-15,]),'PLUS':([2,3,6,7,11,18,19,20,21,22,23,24,25,27,32,34,],[-4,-3,-5,14,14,-17,14,-12,-9,-8,-6,-7,-10,-11,-16,-15,]),'MOD':([2,3,6,7,11,18,19,20,21,22,23,24,25,27,32,34,],[-4,-3,-5,16,16,-17,16,-12,-9,-8,16,16,-10,-11,-16,-15,]),'LPAREN':([0,1,2,3,4,5,6,7,10,12,13,14,15,16,17,18,20,21,22,23,24,25,27,31,32,33,34,],[-1,5,-4,-3,10,5,-5,-2,5,5,5,5,5,5,26,-17,-12,-9,-8,-6,-7,-10,-11,-1,-16,5,-15,]),'COLON':([29,],[31,]),'IDENTIFIER':([0,1,2,3,5,6,7,8,10,12,13,14,15,16,18,20,21,22,23,24,25,26,27,28,30,31,32,33,34,],[-1,6,-4,-3,6,-5,-2,17,6,6,6,6,6,6,-17,-12,-9,-8,-6,-7,-10,-13,-11,30,-14,-1,-16,6,-15,]),'MINUS':([2,3,6,7,11,18,19,20,21,22,23,24,25,27,32,34,],[-4,-3,-5,15,15,-17,15,-12,-9,-8,-6,-7,-10,-11,-16,-15,]),'BLANKLINE':([2,3,6,7,18,20,21,22,23,24,25,27,31,32,33,34,],[-4,-3,-5,-2,-17,-12,-9,-8,-6,-7,-10,-11,-1,-16,34,-15,]),'DEF':([0,1,2,3,5,6,7,10,12,13,14,15,16,18,20,21,22,23,24,25,27,31,32,33,34,],[-1,8,-4,-3,8,-5,-2,8,8,8,8,8,8,-17,-12,-9,-8,-6,-7,-10,-11,-1,-16,8,-15,]),'$end':([0,1,2,3,6,7,18,20,21,22,23,24,25,27,32,34,],[-1,0,-4,-3,-5,-2,-17,-12,-9,-8,-6,-7,-10,-11,-16,-15,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'explist':([0,31,],[1,33,]),'expression':([1,5,10,12,13,14,15,16,33,],[7,11,19,21,22,23,24,25,7,]),'idlist':([26,],[28,]),'block':([29,],[32,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> explist","S'",1,None,None,None),
  ('explist -> <empty>','explist',0,'p_explist','meccaParser.py',11),
  ('explist -> explist expression','explist',2,'p_explist','meccaParser.py',12),
  ('expression -> NUMBER','expression',1,'p_expression_number','meccaParser.py',20),
  ('expression -> STRING','expression',1,'p_expression_string','meccaParser.py',24),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','meccaParser.py',28),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binaryop','meccaParser.py',32),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binaryop','meccaParser.py',33),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binaryop','meccaParser.py',34),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binaryop','meccaParser.py',35),
  ('expression -> expression MOD expression','expression',3,'p_expression_binaryop','meccaParser.py',36),
  ('expression -> ECHO LPAREN expression RPAREN','expression',4,'p_expression_echo','meccaParser.py',50),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parenthesized','meccaParser.py',55),
  ('idlist -> <empty>','idlist',0,'p_idlist','meccaParser.py',59),
  ('idlist -> idlist IDENTIFIER','idlist',2,'p_idlist','meccaParser.py',60),
  ('block -> COLON explist BLANKLINE','block',3,'p_expression_block','meccaParser.py',68),
  ('expression -> DEF IDENTIFIER LPAREN idlist RPAREN block','expression',6,'p_expression_function','meccaParser.py',72),
  ('expression -> NUMBER ARROW NUMBER','expression',3,'p_expression_range','meccaParser.py',76),
]