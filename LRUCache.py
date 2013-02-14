import collections

class LRUCache(collections.OrderedDict):
	"""LRUCache adds methods to OrderedDict to make it work like a LRU ordered dict with a bound"""

	def __setitem__(self, key, value):
		if key in self:
			del self[key]
		if len(self.keys()) == self.bound:
			self.popitem(False)
		collections.OrderedDict.__setitem__(self, key, value)

	def setbound(self, bound=1000000):
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

# Start Reading standard input
number_of_lines = int(raw_input())
bound = raw_input().split()
bound = int(bound[1])

# Instantiate new list to hold standard input and LRU cache object
a = []
d1 = LRUCache()
d1.setbound(bound)

# Read remaining lines of standard input
for i in range(1, number_of_lines):
	a.append(raw_input())

# For each line, perform one of the operations.
for i in a:
	temp = i.split()
	if temp[0] == "SET":
		d1[temp[1]] = temp[2]
	elif temp[0] == "GET":
		d1.get(temp[1])
	elif temp[0] == "DUMP":
		d1.dump()
	elif temp[0] == "PEEK":
		d1.peek(temp[1])
