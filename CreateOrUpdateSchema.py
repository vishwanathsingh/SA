import sqlite3
database = 'example.db'
conn = sqlite3.connect(database)
c = conn.cursor()

# Create Order Table
c.execute("CREATE TABLE ORDERS (date text, truck text, client text, gc_num text, loading_quantity real, received_quantity real, rate real)")


