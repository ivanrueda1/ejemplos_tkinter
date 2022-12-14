from tkinter import Tk, Menu, PhotoImage

def salir():
    root.destroy()
   
root = Tk()
barra_menus = Menu()
root.config(menu=barra_menus)

menu_archivo = Menu(tearoff=0)
menu_archivo.add_command(label="Nuevo")

submenu_abrir = Menu(tearoff=0)
submenu_abrir.add_command(label="Explorar")
submenu_abrir.add_command(label="Recientes")
menu_archivo.add_cascade(label='Abrir', menu=submenu_abrir)

menu_archivo.add_command(label="Guardar")
menu_archivo.add_command(label="Guardar como")
menu_archivo.add_separator()
img = PhotoImagefile="imagennnnn.png"
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)

menu_edicion = Menu(tearoff=0)
menu_edicion.add_command(label="Deshacer")
menu_edicion.add_command(label="Rehacer")
menu_edicion.add_separator()
menu_edicion.add_command(label="Copiar")
menu_edicion.add_command(label="Pegar")
menu_edicion.add_command(label="Borrar")
menu_edicion.add_command(label="Seleccionar todo")
barra_menus.add_cascade(label="Edición", menu=menu_edicion)


menu_ayuda = Menu(tearoff=0)
menu_ayuda.add_command(label="Manual usuario")
menu_ayuda.add_command(label="Acerca de...")
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

root.mainloop()

