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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle

class MainScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.contenedor = BoxLayout(orientation = "vertical")
        self.contenedor_inputs = GridLayout(cols = 2)

        with self.contenedor_inputs.canvas.before:
            Color(0.4, 0.9, 0.4, 1)  
            self.bg_rect = Rectangle(pos=self.contenedor_inputs.pos, size=self.contenedor_inputs.size)
        
        self.contenedor_inputs.bind(size=self._update_bg_rect, pos=self._update_bg_rect)


        self.titulo = Label(text = "Liquidador",
                       font_size = 55,
                       height = 150,
                       size_hint = (1, None))
        self.contenedor.add_widget(self.titulo)


        label_fecha_inicio = Label(text = "Ingrese la fecha de inicio:",
                                   size_hint = (1 , None),
                                   height = 100,
                                   font_size = 30,
                                   color = "black")
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
        boton_guardar_datos.bind(on_press = self.calcular)
        self.contenedor.add_widget(boton_guardar_datos)

        self.add_widget(self.contenedor)
    
    def _update_bg_rect(self, *args):
        self.bg_rect.pos = self.contenedor_inputs.pos
        self.bg_rect.size = self.contenedor_inputs.size
        
    def calcular(self, sender):
        fecha_inicio = self.fecha_inicio.text
        fecha_fin = self.fecha_fin.text
        salario_auxilio = self.salario_auxilio.text
        salario_sin_auxilio = self.salario_sin_auxilio.text
        dias_suspension = self.dias_suspension.text
        dias_indemnizacion = self.dias_indemnizacion.text
        salario_variable = self.salario_variable.text

        liquidacion = liquidacion_total.LiquidacionEmpleado(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)

        resultados = {"prima": str(round(liquidacion.calcular_prima(), 2)),
                      "cesantias": str(round(liquidacion.calcular_cesantias(), 2)),
                      "intereses_cesantias": str(round(liquidacion.calcular_intereses_cesantias(), 2)),
                      "vacaciones": str(round(liquidacion.calcular_vacaciones(), 2)),
                      "indemnizacion": str(round(liquidacion.calcular_indemnizacion(), 2)),
                      "total_liquidacion": str(round(liquidacion.calcular_liquidacion_total(), 2))}
        
        self.manager.get_screen("second").actualizar_resultados(resultados)
        self.cambiar_ventana()

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

class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.contenedor = BoxLayout(orientation = "vertical")
        self.contenedor_labels = GridLayout(cols = 2)

        self.titulo = Label(text = "Resultados",
                            font_size = 55,
                            height = 150,
                            size_hint = (1, None))
        self.contenedor.add_widget(self.titulo)


        self.label_prima = Label(text = "Tu prima es:",
                                 size_hint = (1 , None),
                                 height = 100,
                                 font_size = 30)
        self.contenedor_labels.add_widget(self.label_prima)

        self.prima = TextInput(size_hint = (1 , None),
                               height = 100,
                               font_size = 25)
        self.contenedor_labels.add_widget(self.prima)


        self.label_cesantias = Label(text = "Tus cesantias son:",
                                     size_hint = (1 , None),
                                     height = 100,
                                     font_size = 30)
        self.contenedor_labels.add_widget(self.label_cesantias)

        self.cesantias = TextInput(size_hint = (1 , None),
                                   height = 100,
                                   font_size = 25)
        self.contenedor_labels.add_widget(self.cesantias)


        self.label_intereses_cesantias = Label(text = "Tus intereses sobre las cesantias son:",
                                               size_hint = (1 , None),
                                               height = 100,
                                               font_size = 30)
        self.contenedor_labels.add_widget(self.label_intereses_cesantias)

        self.intereses_cesantias = TextInput(size_hint = (1 , None),
                                             height = 100,
                                             font_size = 25)
        self.contenedor_labels.add_widget(self.intereses_cesantias)


        self.label_vacaciones = Label(text = "tus vacaciones son:",
                                      size_hint = (1 , None),
                                      height = 100,
                                      font_size = 30)
        self.contenedor_labels.add_widget(self.label_vacaciones)

        self.vacaciones = TextInput(size_hint = (1 , None),
                                    height = 100,
                                    font_size = 25)
        self.contenedor_labels.add_widget(self.vacaciones)


        self.label_indemnizacion = Label(text = "tu indemnizacion es:",
                                         size_hint = (1 , None),
                                         height = 100,
                                         font_size = 30)
        self.contenedor_labels.add_widget(self.label_indemnizacion)

        self.indemnizacion = TextInput(size_hint = (1 , None),
                                       height = 100,
                                       font_size = 25)
        self.contenedor_labels.add_widget(self.indemnizacion)


        self.label_total_liquidacion = Label(text = "tu liquidacion es:",
                                             size_hint = (1 , None),
                                             height = 100,
                                             font_size = 30)
        self.contenedor_labels.add_widget(self.label_total_liquidacion)

        self.total_liquidacion = TextInput(size_hint = (1 , None),
                                           height = 100,
                                           font_size = 25)
        self.contenedor_labels.add_widget(self.total_liquidacion)

        self.contenedor.add_widget(self.contenedor_labels)

        self.regresar_inicio = Button(text = "Volver",
                             font_size = 30,
                             size_hint = (1, 0.15))
        self.regresar_inicio.bind(on_press = self.volver_inicio)
        self.contenedor.add_widget(self.regresar_inicio)

        self.add_widget(self.contenedor)
    
    def actualizar_resultados(self, resultados):
        self.prima.text = resultados.get("prima", "0")
        self.cesantias.text = resultados.get("cesantias", "0")
        self.intereses_cesantias.text = resultados.get("intereses_cesantias", "0")
        self.vacaciones.text = resultados.get("vacaciones", "0")
        self.indemnizacion.text = resultados.get("indemnizacion", "0")
        self.total_liquidacion.text = resultados.get("total_liquidacion", "0")

    def volver_inicio(self, sender):
        self.manager.get_screen("main").reiniciar_calculadora()
        self.manager.current = "main"
        

class liquidadorLaboral(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(SecondScreen(name = "second"))
        return sm

if __name__ == "__main__":
    liquidadorLaboral().run()


#Ver porque no me esta borrando los datos con el boton volver