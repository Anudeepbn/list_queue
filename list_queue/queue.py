class flexiqueue:
	default_capacity=2
	def __init__(self):
		self.size=0
		self.front=0
		self.data=[none]*flexiqueue.default_capacity
	def length(self):
		return self.size
	def isempty(self):
		return self.size==0
	def first(self):
		if not self.isempty():
			return self.data[self.front]
	def dequeue(self):
		if not self.isempty():
			element=self.data[self.front]
			self.data[self.front]=none
			self.front=(self.front+1)%len(self.data)
			self.size-=1
			if 0<self.size<len(self.data)//4:
				self.resize(len(self.data)//2)
			return element
	def enqueue(self,ele):
		if self.size==len(self.data):
			self.resize(2*len(self.data))
		next=(self.front+self.size)%len(self.data)
		self.data[next]=ele
		self.size+=1
	def resize(self,capacity):
		old=self.data
		walk=self.front
		self.data=[none]*capacity
		for k in  len(old):
			self.data[k]=old[walk]
			walk=(walk+1)%len(old)
		self.front=0