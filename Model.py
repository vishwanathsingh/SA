import sqlite3

class Model(object):
	"""docstring for Model"""

	database = "example.db"
	def __init__(self, arg):
		super(Model, self).__init__()
		self.arg = arg

	def connect():
		conn = sqlite3.connect(database)
		c = conn.cursor()
		return c

	def create_table(table, column_tuples):
		c = connect()
		columns = _get_sql_string(column_tuples)
		c.execute("CREATE TABLE " + table  + " " + columns)
		c.close()


	def save(table, values):
		c = connect()
		c.execute("Insert into " + table + "values ( " + values + " )");
		c.close()

	def get_by_id():
		pass

	def select(query):
		pass

	def update(query):
		pass


		