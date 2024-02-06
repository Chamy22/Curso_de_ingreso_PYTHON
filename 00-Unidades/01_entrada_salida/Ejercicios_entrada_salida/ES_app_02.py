import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Yamil 
apellido:Ibrahim
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #descripcion_producto = "Coca-cola" #snake case siempre tiene que ser en minuscula y unidos con un guion bajo (se usa en python)
        # asignacion de una variable, es lo que hicimos en la linea de arriba
        descripcion_producto = prompt ("Datos", "ingrese descripcion del producto")
        
        
        alert ("Descripcion", descripcion_producto)
        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()