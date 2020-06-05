import sqlite3

conn=sqlite3.connect('base_inventario.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS inventario(codigo TEXT,producto TEXT ,laboratorio TEXT,cantidad TEXT,precio_und TEXT)")
	conn.commit()
	c.execute("INSERT INTO inventario values ('1f21','Lansoprazol','basico','120','2')")
	conn.commit()
	c.close()
	conn.close()

create_table()