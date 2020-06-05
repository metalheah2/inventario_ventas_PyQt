'''
	Autor : Marco Jhoel Churata Torres
	Fecha : 04 - 06 - 2020
	Nombre : Inventario_venta_PyQt.py
	Descripcion : Estuve haciendo este programa ... por algunos dias
					se los dejo aqui por si les sirve de algo.Gracias
'''

from Inventario_venta_UI import *
from datetime import date
import sqlite3

def eliminar_filas_venta():
	conn=sqlite3.connect('base_inventario.db')
	c=conn.cursor()
	c.execute('DELETE  FROM ventas ')
	conn.commit()

def base_datos(fila,columna):
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute('SELECT * FROM inventario')
	rows=cursor.fetchall()
	return rows[fila][columna]

def base_ventas(fila,columna):
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute('SELECT * FROM ventas')
	rows=cursor.fetchall()
	return rows[fila][columna]
	
def escribir_base_datos(producto,cantidad,unidades,precio_und,importe):
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute("INSERT INTO ventas values (\'"+producto+"\',\'"+cantidad+"\',\'"+unidades+"\',\'"+precio_und+"\',\'"+importe+"')")
	con.commit()
	cursor.close()
	con.close()
	
def lista_ventas(vendedor,cliente,tipo_pago,fecha_venta,monto_total):
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute("INSERT INTO ventas_dia values (\'"+vendedor+"\',\'"+cliente+"\',\'"+tipo_pago+"\',\'"+fecha_venta+"\',\'"+monto_total+"')")
	con.commit()
	cursor.close()
	con.close()
	
def monto_total(catd_elem):
	monto_total_venta=0
	for valor in range(0,catd_elem):
		monto_total_venta=int(base_ventas(valor,4))+monto_total_venta
		#print(monto_total_venta)
	#print(monto_total_venta)
	return monto_total_venta
	
def elemtos_ventas():
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute('SELECT * FROM ventas')
	rows=cursor.fetchall()
	catd_elem=len(rows)
	return catd_elem
	
class MainWindow(QtWidgets.QMainWindow,Ui_VENTANA):
	def __init__(self,*args,**kwargs):
		QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
		_translate=QtCore.QCoreApplication.translate
		self.setupUi(self)
		eliminar_filas_venta()
		today=date.today()
		item=self.tabla_int.item(1,3)
		self.fecha.setText(str(today))
		item=self.tabla_int.item(0,0)
		item.setText(_translate("VENTANA",base_datos(0,0)))
		for fil in range(0,10):
			for colum in range(0,5):
				item=self.tabla_int.item(fil,colum)
				item.setText(_translate("VENTANA",str(base_datos(fil,colum))))
				if(colum==5):
					cantidad=int(base_datos(fil,colum-1))
					precio=int(base_datos(fil,colum-2))
					monto_total=cantidad*precio
					item.setText(_translate("VENTANA",str(monto_total)+'.00'))
					
		
		self.bot_agregar.clicked.connect(self.accion)
		self.generar_venta.clicked.connect(self.gen_vent)
		self.terminar.clicked.connect(self.terminar_venta)
		
	def accion(self):
		#aea=self.cod_bus.text()
		for valor in range(0,10):
			if(base_datos(valor,0)==self.cod_bus.text()):
				self.nom_pro.setText(base_datos(valor,1))
				self.Lab.setText(base_datos(valor,2))
				self.p_unit.setText(base_datos(valor,4))
				cant=self.spinBox.text()
				monto_und=int(base_datos(valor,4))*int(cant)
				if(int(cant)>0):
					self.monto_t.setText(str(monto_und)+".00")
				else:
					self.monto_t.setText(".00")
	
	def gen_vent(self):
		_translate=QtCore.QCoreApplication.translate
		producto=self.nom_pro.text()
		cantidad=self.spinBox.text()
		unidades="und"
		precio_und=self.p_unit.text()
		importe=int(cantidad)*int(precio_und)
		escribir_base_datos(producto,cantidad,unidades,precio_und,str(importe))
		cnd_elem=elemtos_ventas()
		item=self.boleta.item(cnd_elem-1,0)
		item.setText(_translate("VENTANA",producto))
		item=self.boleta.item(cnd_elem-1,1)
		item.setText(_translate("VENTANA",cantidad))
		item=self.boleta.item(cnd_elem-1,2)
		item.setText(_translate("VENTANA",unidades))
		item=self.boleta.item(cnd_elem-1,3)
		item.setText(_translate("VENTANA",precio_und))
		item=self.boleta.item(cnd_elem-1,4)
		item.setText(_translate("VENTANA",str(importe)+'.00'))
		self.total_general.setText(str(monto_total(cnd_elem))+'.00')
			
	def terminar_venta(self):
		vendedor=self.vendedor.text()
		cliente=self.cliente.text()
		tipo_pago=self.tipo_pago.currentText()
		fecha_venta=self.fecha.text()
		aea=elemtos_ventas()
		monto_t=monto_total(aea)
		lista_ventas(vendedor,cliente,tipo_pago,fecha_venta,str(monto_t)+'.00')
		eliminar_filas_venta()
	
if __name__=="__main__":
	#crear_tabla
	app=QtWidgets.QApplication([])
	window=MainWindow()
	window.show()
	app.exec_()