import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from model import liquidacion_total


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class liquidadorLaboral(App):

    def build(self):
        self.contenedor = BoxLayout(orientation = "vertical")
        self.contenedor_inputs = GridLayout(cols = 2)

        self.titulo = Label(text = "Liquidador",
                       font_size = 55,
                       height = 150,
                       size_hint = (1, None))
        self.contenedor.add_widget(self.titulo)


        label_fecha_inicio = Label(text = "Ingrese la fecha de inicio:",
                                   size_hint = (1 , None),
                                   height = 100,
                                   font_size = 30)
        self.contenedor_inputs.add_widget(label_fecha_inicio)

        self.fecha_inicio = TextInput(size_hint = (1 , None),
                                 height = 100,
                                 font_size = 25)
        self.contenedor_inputs.add_widget(self.fecha_inicio)


        label_fecha_fin = Label(text = "Ingrese la fecha de fin:",
                                size_hint = (1 , None),
                                height = 100,
                                font_size = 30)
        self.contenedor_inputs.add_widget(label_fecha_fin)

        self.fecha_fin = TextInput(size_hint = (1 , None),
                              height = 100,
                              font_size = 25)
        self.contenedor_inputs.add_widget(self.fecha_fin)


        label_salario_auxilio = Label(text = "Por favor ingrese su salario con auxilio:",
                                      size_hint = (1 , None),
                                      height = 100,
                                      font_size = 30)
        self.contenedor_inputs.add_widget(label_salario_auxilio)

        self.salario_auxilio = TextInput(size_hint = (1 , None),
                                    height = 100,
                                    font_size = 25)
        self.contenedor_inputs.add_widget(self.salario_auxilio)


        lable_salario_sin_auxilio = Label(text = "Ingrese su salario sin auxilio:",
                                          size_hint = (1 , None),
                                          height = 100,
                                          font_size = 30)
        self.contenedor_inputs.add_widget(lable_salario_sin_auxilio)

        self.salario_sin_auxilio = TextInput(size_hint = (1 , None),
                                        height = 100,
                                        font_size = 25)
        self.contenedor_inputs.add_widget(self.salario_sin_auxilio)


        label_dias_suspension = Label(text = "Ingrese sus dias de suspension:", 
                                      size_hint = (1 , None),
                                      height = 100,
                                      font_size = 30)
        self.contenedor_inputs.add_widget(label_dias_suspension)

        self.dias_suspension = TextInput(size_hint = (1 , None),
                                    height = 100,
                                    font_size = 25)
        self.contenedor_inputs.add_widget(self.dias_suspension)


        label_dias_indemnizacion = Label(text = "Ingrese sus dias de indemnizacion:",
                                         size_hint = (1 , None),
                                         height = 100,
                                         font_size = 30)
        self.contenedor_inputs.add_widget(label_dias_indemnizacion)

        self.dias_indemnizacion = TextInput(size_hint = (1 , None),
                                       height = 100,
                                       font_size = 25)
        self.contenedor_inputs.add_widget(self.dias_indemnizacion)


        label_salario_variable = Label(text = "Ingrese su salario:",
                                       size_hint = (1 , None),
                                       height = 100,
                                       font_size = 30)
        self.contenedor_inputs.add_widget(label_salario_variable)

        self.salario_variable = TextInput(size_hint = (1 , None),
                                     height = 100,
                                     font_size = 25)
        self.contenedor_inputs.add_widget(self.salario_variable)

        self.contenedor.add_widget(self.contenedor_inputs)

        boton_guardar_datos = Button(text = "Calcular", 
                                     font_size = 30,
                                     size_hint = (1, 0.15))
        boton_guardar_datos.bind(on_press = self.calcular())
        self.contenedor.add_widget(boton_guardar_datos)

        return self.contenedor

    def calcular(self, sender):
        fecha_inicio = self.fecha_inicio
        fecha_fin = self.fecha_fin
        salario_auxilio = self.salario_auxilio
        salario_sin_auxilio = self.salario_sin_auxilio
        dias_suspension = self.dias_suspension
        dias_indemnizacion = self.dias_indemnizacion
        salario_variable = self.salario_variable

        liquidacion = liquidacion_total.LiquidacionEmpleado(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)
        



if __name__ == "__main__":
    liquidadorLaboral().run()