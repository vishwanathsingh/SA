import sqlite3

database = 'example.db'

def connect():
	conn = sqlite3.connect(database)
	c = conn.cursor()
	return c

def create_table(table, column_tuples):
	c = connect()
	columns = _get_sql_string(column_tuples)
	c.execute("CREATE TABLE " + table  + " " + columns)
	c.close()


def save(table, values_dict):
	c = connect()
	columns = []
	values = []
	for item, value in values_dict.items():
		columns.append(item)
		values.append(value)

	insert_query = "Insert into " + table + " ( " + ", ".join(columns) + " )" + " values " + " ( " + ", ".join(values) + " );"
	print (insert_query)
	c.execute(insert_query)
	c.close()

def get_by_id():
	pass

def select(query):
	pass

def update(query):
	pass


	