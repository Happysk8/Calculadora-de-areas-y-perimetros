import os
import tkinter as tk
from PIL import Image, ImageTk
from calculator import areas_calculator, perimeters_calculator

#Cambiar la siguiente ruta de acuerdo a la máquina en la que se esté corriendo la app
os.chdir("C:/Users/LENOVO/.vscode/apps/Calculadoradeareasyperimetros/Calculadora-de-areas-y-perimetros")

class app:

    def __init__(self):
        self.a = 2
        self.areas = areas_calculator()
        self.perimeters = perimeters_calculator()
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=300)
        self.canvas.grid(columnspan=3, rowspan=3)

        #logo
        self.logo = Image.open('images/logo.png')
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.grid(column=1, row=0)

        #browse button
        self.browse_text = tk.StringVar()
        self.browse_btn = tk.Button(self.root, textvariable=self.browse_text, command=lambda:self.areas.circle_area(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
        self.browse_text.set("Calcular")
        self.browse_btn.grid(column=1, row=2)


    def run(self):

        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print('interrupted!')


if __name__ == "__main__":

    calculator = app()
    calculator.run()

    