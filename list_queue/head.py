class slist:
	class node:
		def __init__(self,element):
			self.data=element
			self.next=none
	def __init__(self):
		self.head=none
		self.tail=none
		self.count=0
	def isempty(self):
		return self.count==0
	def length(self):
		return self.count
	def first(self):
		if not self.isempty():
			return self.head.data
	def last(self):
		if not self.isempty():
			return self.tail.data
	def add_first(self,val):
		newnode=self.node(val)
		if not self.isempty():
			newnode.next=self.head
			self.head=newnode
		else:
			self.head=self.tail=newnode
		self.count+=1
	def add_tail(self,val):
		newnode=self.node(val)
		if not self.isempty():
			self.tail.next=newnode
			self.tail=newnode
		else:
			self.head=self.tail=newnode
		self.count+=1
	def del_first(Self):
		if not self.isempty():
			data=self.head.data
			self.head=self.head.next
			if self.head is none:
				self.tail=none
			self.count-=1
			return data
	def del_last(self):
		if not self.isempty():
			data=self.tail.data
			if self.count==1:
				self.head=self.tail=none
			else:
				last=self.tail
				cur=self.head
				while cur.next is not last:
					cur=cur.next
				self.tail=cur
				self.tail.next=none
			self.count-=1
			return data
	def is_member(self,key):
		if not self.isempty():
			cur=self.head
			while cur is not none:
				if cur.data==key:
					break
				else:
					cur=cur.next
			return cur!=none