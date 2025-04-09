import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from model import liquidacion_total
from view.gui.own_classes import BackgroundLabel

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup

class MainScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.contenedor = BoxLayout(orientation = "vertical")
        self.contenedor_inputs = GridLayout(cols = 2)

        with self.contenedor_inputs.canvas.before:
            Color(0.98, 0.98, 0.98, 1)  
            self.bg_rect = Rectangle(pos=self.contenedor_inputs.pos, size=self.contenedor_inputs.size)
        
        self.contenedor_inputs.bind(size = self._actualizar_background, pos = self._actualizar_background)


        self.titulo = BackgroundLabel(text = "Liquidador",
                                      font_size = 55,
                                      height = 150,
                                      size_hint = (1, None),
                                      background_color = (0.25, 0.25, 0.3, 1))
        self.contenedor.add_widget(self.titulo)


        label_fecha_inicio = BackgroundLabel(text = "Ingrese la fecha de inicio:",
                                   size_hint = (1 , None),
                                   height = 100,
                                   font_size = 30,
                                   color = "white",
                                   background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_inputs.add_widget(label_fecha_inicio)

        self.fecha_inicio = TextInput(size_hint = (1 , None),
                                 height = 100,
                                 font_size = 25,
                                 foreground_color = (0.15, 0.15, 0.15, 1))
        self.contenedor_inputs.add_widget(self.fecha_inicio)


        label_fecha_fin = BackgroundLabel(text = "Ingrese la fecha de fin:",
                                size_hint = (1 , None),
                                height = 100,
                                font_size = 30,
                                color = "white",
                                background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_inputs.add_widget(label_fecha_fin)

        self.fecha_fin = TextInput(size_hint = (1 , None),
                              height = 100,
                              font_size = 25,
                              foreground_color = (0.15, 0.15, 0.15, 1))
        self.contenedor_inputs.add_widget(self.fecha_fin)


        label_salario_auxilio = BackgroundLabel(text = "Por favor ingrese su salario con auxilio:",
                                      size_hint = (1 , None),
                                      height = 100,
                                      font_size = 30,
                                      color = "white",
                                      background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_inputs.add_widget(label_salario_auxilio)

        self.salario_auxilio = TextInput(size_hint = (1 , None),
                                    height = 100,
                                    font_size = 25,
                                    foreground_color = (0.15, 0.15, 0.15, 1))
        self.contenedor_inputs.add_widget(self.salario_auxilio)


        lable_salario_sin_auxilio = BackgroundLabel(text = "Ingrese su salario sin auxilio:",
                                          size_hint = (1 , None),
                                          height = 100,
                                          font_size = 30,
                                          color = "white",
                                          background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_inputs.add_widget(lable_salario_sin_auxilio)

        self.salario_sin_auxilio = TextInput(size_hint = (1 , None),
                                        height = 100,
                                        font_size = 25,
                                        foreground_color = (0.15, 0.15, 0.15, 1))
        self.contenedor_inputs.add_widget(self.salario_sin_auxilio)


        label_dias_suspension = BackgroundLabel(text = "Ingrese sus dias de suspension:", 
                                      size_hint = (1 , None),
                                      height = 100,
                                      font_size = 30,
                                      color = "white",
                                      background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_inputs.add_widget(label_dias_suspension)

        self.dias_suspension = TextInput(size_hint = (1 , None),
                                    height = 100,
                                    font_size = 25,
                                    foreground_color = (0.15, 0.15, 0.15, 1))
        self.contenedor_inputs.add_widget(self.dias_suspension)


        label_dias_indemnizacion = BackgroundLabel(text = "Ingrese sus dias de indemnizacion:",
                                         size_hint = (1 , None),
                                         height = 100,
                                         font_size = 30,
                                         color = "white",
                                         background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_inputs.add_widget(label_dias_indemnizacion)

        self.dias_indemnizacion = TextInput(size_hint = (1 , None),
                                       height = 100,
                                       font_size = 25,
                                       foreground_color = (0.15, 0.15, 0.15, 1))
        self.contenedor_inputs.add_widget(self.dias_indemnizacion)


        label_salario_variable = BackgroundLabel(text = "Ingrese su salario:",
                                       size_hint = (1 , None),
                                       height = 100,
                                       font_size = 30,
                                       color = "white",
                                       background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_inputs.add_widget(label_salario_variable)

        self.salario_variable = TextInput(size_hint = (1 , None),
                                     height = 100,
                                     font_size = 25,
                                     foreground_color = (0.15, 0.15, 0.15, 1))
        self.contenedor_inputs.add_widget(self.salario_variable)

        self.contenedor.add_widget(self.contenedor_inputs)

        self.boton_guardar_datos = Button(text = "Calcular", 
                                     font_size = 30,
                                     size_hint = (1, 0.15),
                                     background_color = (0.18, 0.44, 0.75, 1))
        self.boton_guardar_datos.bind(on_press = self.calcular)
        self.contenedor.add_widget(self.boton_guardar_datos)

        self.add_widget(self.contenedor)
    
    def _actualizar_background(self, *args):
        self.bg_rect.pos = self.contenedor_inputs.pos
        self.bg_rect.size = self.contenedor_inputs.size
        
    def calcular(self, sender):
        try:
            fecha_inicio = self.fecha_inicio.text
            fecha_fin = self.fecha_fin.text
            salario_auxilio = float(self.salario_auxilio.text)
            salario_sin_auxilio = float(self.salario_sin_auxilio.text)
            dias_suspension = float(self.dias_suspension.text)
            dias_indemnizacion = float(self.dias_indemnizacion.text)
            salario_variable = float(self.salario_variable.text)

            liquidacion = liquidacion_total.LiquidacionEmpleado(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)

            resultados = {"prima": str(round(liquidacion.calcular_prima(), 2)),
                        "cesantias": str(round(liquidacion.calcular_cesantias(), 2)),
                        "intereses_cesantias": str(round(liquidacion.calcular_intereses_cesantias(), 2)),
                        "vacaciones": str(round(liquidacion.calcular_vacaciones(), 2)),
                        "indemnizacion": str(round(liquidacion.calcular_indemnizacion(), 2)),
                        "total_liquidacion": str(round(liquidacion.calcular_liquidacion_total(), 2))}
            
            self.manager.get_screen("second").actualizar_resultados(resultados)
            self.cambiar_ventana()
        except Exception as ex:
            self.boton_guardar_datos.text = "Esta fallando"


    def cambiar_ventana(self):
        self.manager.current = "second"

    def reiniciar_calculadora(self):
        self.fecha_inicio.text = ""
        self.fecha_fin.text = ""
        self.salario_auxilio.text = ""
        self.salario_sin_auxilio.text = ""
        self.dias_suspension.text = ""
        self.dias_indemnizacion.text = ""
        self.salario_variable.text = ""
