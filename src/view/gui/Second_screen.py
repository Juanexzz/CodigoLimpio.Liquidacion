from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

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
