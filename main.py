from kivy.app import App
from kivy.config import Config
from kivy.uix import boxlayout, gridlayout, button, label


class Calculatrice(boxlayout.BoxLayout):
    def calculer(self, expression):
        if expression:
            try:
                self.display.text = str(eval(expression))
            except Exception:
                self.display.text = "Erreur"

    def initialiser(self, expression):
        if expression:
            self.display.text = ""



class MainApp(App):
    def build(self):
        self.title = "Calculatrice" # titre


Config.set("graphics", "width", "250")
Config.set("graphics", "height", "415")
Config.set("graphics", "resizable", "0")

MainApp().run()
