import Model

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
		

	def save(value_dict):
		#self.entries = {'truck_num': None, 'date': None, 'gc_num': None, 'e_loading': None, 'e_received': None, 'e_client': None, 'e_rate': None, 'e_advance': None, 'e_amount': None}
		print ("save Order")
		values = {'date': (value_dict['date'], "text"), 
					'truck': (value_dict['truck_num'], "text"), 
					'gc_num': (value_dict['gc_num'], "text"), 
					'client': (value_dict['e_client'], "text"),
					'loading_quantity': (value_dict['e_loading'], "real"),
					'received_quantity': (value_dict['e_received'], "real"),
					'rate': (value_dict['e_rate'], "real")
					}

		Model.save(Order.table, values)