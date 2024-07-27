import sqlite3

with sqlite3.connect('base_inventario.db') as conn:
	def create_table():
		conn.execute("CREATE TABLE IF NOT EXISTS inventario(codigo TEXT,producto TEXT ,laboratorio TEXT,cantidad TEXT,precio_und TEXT)")
		conn.execute("CREATE TABLE IF NOT EXISTS ventas (producto TEXT,cantidad TEXT,unidades TEXT,precio_und TEXT,importe TEXT)")
		conn.execute("CREATE TABLE IF NOT EXISTS ventas_dia (vendedor TEXT,cliente TEXT,tipo_pago TEXT,fecha_venta TEXT,monto_total TEXT)")
		conn.commit()
		print("Tablas_creadas")
	
create_table()