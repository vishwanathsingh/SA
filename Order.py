class Order(object):
	"""docstring for Order"""
	table = "Orders"

	def __init__(self, arg):
		super(Order, self).__init__()
		self.truck = truck
		self.driver = driver
		self.client = client
		self.date = date
		self.gc_num = gc_num
		self.loading_quantity = loading_quantity
		self.received_quantity = received_quantity
		self.rate = rate

	def get_amount(self):
		self.rate*self.received_quantity

	def get_short(self):
		self.loading_quantity - self.received_quantity
		

	def save(dictionary):
		print ("save Order")
		Model.save(Order.table, dictionary)