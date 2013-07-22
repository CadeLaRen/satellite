class Node(object):
	def __init__(self, t, *args):
		self.args = args
		self.type = t
	def __repr__(self):
		return str(vars(self))