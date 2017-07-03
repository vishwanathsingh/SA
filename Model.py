import sqlite3

database = 'example.db'

def connect():
	conn = sqlite3.connect(database)
	return conn

def create_table(table, column_tuples):
	c = connect()
	columns = _get_sql_string(column_tuples)
	c.execute("CREATE TABLE " + table  + " " + columns)
	c.close()


def save(table, values_dict):
	conn = connect()
	columns = []
	values = []
	for item, value in values_dict.items():
		columns.append(item)
		v, t = value
		if t == "text":
			values.append("'" + v + "'")
		else:
			values.append(v)

	insert_query = "Insert into " + table + " ( " + ", ".join(columns) + " )" + " values " + " ( " + ", ".join(values) + " );"
	print (insert_query)
	conn.cursor().execute(insert_query)
	conn.commit()
	conn.close()

def get_by_id():
	pass

def select(query):
	pass

def update(query):
	pass


	