# https://edabit.com/challenge/CxxaYAGcuk8TyA9Jt
# 18.02.2025
# Very Hard


class singly_linked_list:

	def __init__(self, data):
		self.data = data
		self.next = None

	def merge(self, node):
		self.last_node().next = node

	def add_last(self, data):
		self.merge(singly_linked_list(data))

	def add_beginning(self, data):
		aid = self.copy()
		self.data = data
		self.next = None
		self.merge(aid)

	def add_in(self, data, i):
		if i == 0:
			self.add_beginning(data)
		else:
			aid2 = singly_linked_list(data)
			aid = self.get(i)
			aid2.next = aid.next
			aid.next = aid2

	def last_node(self):
		last = self
		while last.next != None:
			last = last.next
		return last

	def length(self):
		length = 0
		current = self
		while current:
			current = current.next
			length += 1
		return length

	def copy(self):
		head = singly_linked_list(self.data)
		current = self.next
		while current:
			head.add_last(current.data)
			current = current.next
		return head

	def find(self, data):
		aid = 0
		current = self
		while current != None and current.data != data:
			current = current.next
			aid += 1
		if current:
			return aid
		return -1

	def get(self, i):
		aid = 0
		current = self
		while aid != i:
			current = current.next
			aid += 1
		if current is None:
			raise IndexError("Index out of range")
		return current

	def del_last(self):
		if self.next is None:
			self.data = None
		else:
			self.get(self.length() - 2).next = None

	def del_beginning(self):
		if self.next is not None:
			self.data = self.next.data
			self.next = self.next.next
		else:
			self.data = None

	def del_in(self, i):
		if i == 0:
			self.del_beginning()
		else:
			aid = self.get(i)
			aid2 = self.get(i-1)
			aid2.next = aid.next

class stack:
	def __init__(self):
		self.top = None

	def is_empty(self):
		return self.top is None

	def push(self, data):
		if self.is_empty():
			self.top = singly_linked_list(data)
		else:
			self.top.add_beginning(data)

	def pop(self):
		if self.is_empty():
			raise ValueError("Stack is Empty")
		aid = self.length()
		self.top.del_beginning()
		if aid == 1:
			self.top = None

	def length(self):
		if self.is_empty():
			return 0
		return self.top.length()

d = {
	'(':')',
	'[':']',
	'{':'}'
}

def check_balance_with_my_stack(txt):
	stk = stack()
	aid = None
	j = 0
	for i in txt:
		if i in d.keys():
			stk.push(i)
			aid = d[i]
		elif i in d.values():
			if aid != None and aid == i:
				stk.pop()
				if not stk.is_empty():
					aid = d[stk.top.data]
				else:
					aid = None
			else:
				return j
		j += 1
	if not stk.is_empty():
		return j
	return -1

def check_balance_with_array(txt):
	i = 0
	lst = []
	for arg in txt:
		if arg in d.keys():
			lst.append(arg)
		elif arg in d.values():
			if lst and d[lst[-1]] == arg:
				lst.pop(-1)
			else:
				return i
		i += 1
	if lst:
		return i
	return -1
