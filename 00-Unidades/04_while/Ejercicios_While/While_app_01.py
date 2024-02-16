import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):

    #    """ condicion = True
    #
    #    alert ("utn", "Inicio")

    #    while condicion:
    #        alert ("utn", "hola")
    #        condicion = question ("Pregunta", "Desea continuar")

    #    alert ("utn", "fin") """

    #    alert ("utn", "Inicio")

    #    contador_de_nombre = 0 
    #    while contador_de_nombre < 3 :
    #        nombre = prompt ("Utn", "Ingrese su nombre")
    #        alert ("Saludo", f"Hola {nombre}")
    #        contador_de_nombre += 1
        
    #alert ("utn", "fin")

            contador = 0
    
            while contador < 10 :
                contador += 1
                alert ("utn", contador)
            #respuesta = question ("utn", "desea continuar?")
            #if not respuesta :
            #break

            alert ("utn", "fin")

        

    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()