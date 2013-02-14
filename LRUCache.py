import collections

class LastUpdatedOrderedDict(collections.OrderedDict):
	"""docstring for LastUpdatedOrderedDict"""

	def __setitem__(self, key, value):
		if key in self:
			del self[key]
		if len(self.keys()) == self.bound:
			self.popitem(False)
		collections.OrderedDict.__setitem__(self, key, value)

	def setbound(self, bound):
		self.bound = bound

	def peek(self, key):
		if key in self:
			value = self[key]
			print value
		else:
			print "NULL"

	def get(self, key):
		if key in self:
			value = self[key]
			del self[key]
			self.__setitem__(key, value)
			print value
		else:
			print "NULL"

	def dump(self):
		for key in sorted(self.iterkeys()):
			print key, self[key]

# number_of_lines = int(raw_input())
# bound = raw_input().split()
# bound = int(bound[1])
# print bound
# a = []
# b = LRUCache(bound)
# for i in range(1, number_of_lines):
# 	a.append(raw_input())
# for i in a:
# 	temp = i.split()
# 	if temp[0] == "SET":
# 		b.set()

# print a
#a = LRUCache(bound)

d1 = LastUpdatedOrderedDict()
d1.setbound(4)
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'
d1['a'] = 'N'
d1.get('b')
d1.peek('c')
d1.get('e')
print "====================================================================="
d1.dump()
print "====================================================================="
