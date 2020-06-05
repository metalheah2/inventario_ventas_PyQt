import sqlite3

con=sqlite3.connect('base_inventario.db')
cursor=con.cursor()

def crear_tabla():
	cursor.execute("CREATE TABLE IF NOT EXISTS ventas (producto TEXT,cantidad TEXT,unidades TEXT,precio_und TEXT,importe TEXT)")
	con.commit()
	cursor.execute("CREATE TABLE IF NOT EXISTS ventas_dia (vendedor TEXT,cliente TEXT,tipo_pago TEXT,fecha_venta TEXT,monto_total TEXT)")
	con.commit()
	cursor.cloese()
	con.close()
	print("Tablas_creadas")
	
crear_tabla