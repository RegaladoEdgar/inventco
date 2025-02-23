#!/usr/bin/pyhton3

from tkinter import ttk
from tkinter import *

from interfaz.interfaz_app_inventario import InterfazAppInventario

#importamos la clase pestaña que construimos
from interfaz.interfaz_app_registrar import InterfazAppRegistrar


class Ventana(Frame):
	# solo hay una ventana en el programa, aqui se añaden las pestañas que se vayan a usar.
	def __init__(self, master=None): #constructor de la ventana
		Frame.__init__(self, master)
		self.master = master
		#declarar todas las pestañas (tabs) que contendrá esta ventana
		self.tab_control = None #controlador que tiene las pestañas
		self.tab_inventario = None #pestaña del inventario
		self.tab_regitrar = None

		self.init_window() #tareas antes de mostrar ventana
		self.tab_control.bind("<<NotebookTabChanged>>", self.configure_tab_control) #cuando cambia la pestaña, ir a esta funcion


	def init_window(self):
		self.master.title("Simulador de puntos de Reorden Inventco.")
		self.crear_tabs()
	
		self.grid(column = 0, row = 0)
		#self.pack(fill=BOTH, expand=1)

	def configure_tab_control(self, event):
		self.rellenar_tabs_de_aplicacion()	


	def rellenar_tabs_de_aplicacion(self):
		#aqui se ponen las funciones que rellenan a todas las tabs a usar
		self.rellenar_tab_inventario()

	def rellenar_tab_inventario(self):
		#antes se usaba porque habia generador, ahora no hace nada
		#self.tab_inventario.set_numeros(self.tab_generador.generador.get_generacion())
		pass
	

	def crear_tabs(self):
		#crea el control de tabs y todas las tabs de la app
		self.tab_control = ttk.Notebook(self) # tab de control, no es visible pero es el padre de las demas
		#se crean los objetos de las pestañas y se añaden a esta ventana
		self.tab_inventario = InterfazAppInventario(self.tab_control) # se crea una nueva tab, en este caso es una interfazappinventario, se envia al padre que es tab_control
		self.tab_control.add(self.tab_inventario, text="Inventarios") # se agrega a tab control la nueva tab creada y se pone su titulo "inventarios"
		
		self.tab_registrar = InterfazAppRegistrar(self.tab_control)
		self.tab_control.add(self.tab_registrar, text="Registrar")

		self.tab_control.grid(column= 1, row = 1) #todas las tabs aparecen empezando en la col 1, fila 1.

