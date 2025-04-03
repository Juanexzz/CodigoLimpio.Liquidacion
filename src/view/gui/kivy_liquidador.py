import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class liquidadorLaboral(App):

    def build(self):
        contenedor = BoxLayout(orientation = "vertical")
        contenedor_inputs = GridLayout(cols = 2)

        titulo = Label(text = "Liquidador",
                       font_size = 55,
                       height = 150,
                       size_hint = (1, None))
        contenedor.add_widget(titulo)


        label_fecha_inicio = Label(text = "Ingrese la fecha de inicio:",
                                   size_hint = (1 , None),
                                   height = 100,
                                   font_size = 30)
        contenedor_inputs.add_widget(label_fecha_inicio)

        fecha_inicio = TextInput(size_hint = (1 , None),
                                 height = 100)
        contenedor_inputs.add_widget(fecha_inicio)


        label_fecha_fin = Label(text = "Ingrese la fecha de fin:",
                                size_hint = (1 , None),
                                height = 100,
                                font_size = 30)
        contenedor_inputs.add_widget(label_fecha_fin)

        fecha_fin = TextInput(size_hint = (1 , None),
                              height = 100)
        contenedor_inputs.add_widget(fecha_fin)


        label_salario_auxilio = Label(text = "Por favor ingrese su salario con auxilio:",
                                      size_hint = (1 , None),
                                      height = 100,
                                      font_size = 30)
        contenedor_inputs.add_widget(label_salario_auxilio)

        salario_auxilio = TextInput(size_hint = (1 , None),
                                    height = 100)
        contenedor_inputs.add_widget(salario_auxilio)


        lable_salario_sin_auxilio = Label(text = "Ingrese su salario sin auxilio:",
                                          size_hint = (1 , None),
                                          height = 100,
                                          font_size = 30)
        contenedor_inputs.add_widget(lable_salario_sin_auxilio)

        salario_sin_auxilio = TextInput(size_hint = (1 , None),
                                        height = 100)
        contenedor_inputs.add_widget(salario_sin_auxilio)


        label_dias_suspension = Label(text = "Ingrese sus dias de suspension:", 
                                      size_hint = (1 , None),
                                      height = 100,
                                      font_size = 30)
        contenedor_inputs.add_widget(label_dias_suspension)

        dias_suspension = TextInput(size_hint = (1 , None),
                                    height = 100)
        contenedor_inputs.add_widget(dias_suspension)


        label_dias_indemnizacion = Label(text = "Ingrese sus dias de indemnizacion:",
                                         size_hint = (1 , None),
                                         height = 100,
                                         font_size = 30)
        contenedor_inputs.add_widget(label_dias_indemnizacion)

        dias_indemnizacion = TextInput(size_hint = (1 , None),
                                       height = 100)
        contenedor_inputs.add_widget(dias_indemnizacion)


        label_salario_variable = Label(text = "Ingrese su salario:",
                                       size_hint = (1 , None),
                                       height = 100,
                                       font_size = 30)
        contenedor_inputs.add_widget(label_salario_variable)

        salario_variable = TextInput(size_hint = (1 , None),
                                     height = 100)
        contenedor_inputs.add_widget(salario_variable)

        contenedor.add_widget(contenedor_inputs)

        boton_guardar_datos = Button(text = "Calcular", 
                                     font_size = 30,
                                     size_hint = (1, 0.15))
        contenedor.add_widget(boton_guardar_datos)

        return contenedor


if __name__ == "__main__":
    liquidadorLaboral().run()