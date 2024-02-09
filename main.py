from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.config import Config
from view import Manager, FirstScreen, MainScreen, MyMapMarker, PropertyDetails
from model import MapModel
from kivy.core.text import LabelBase
import csv

Window.size = (480, 800)

"""

To be named: " PropertyView "

lat: 24.4688
lon: 54.3733

"""
class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.coordinates = None
        self.screen_manager = None
        self.latitude = ""
        self.longitude = ""
        self.model_ins = MapModel()

    def build(self):

        data = self.model_ins.get_data(r'C:\Users\scorp\Desktop\Programmin\Map App\Coordinates.csv')
        self.coordinates = data

        Builder.load_file(r'C:\Users\scorp\Desktop\Programmin\Map App\View.kv')

        # set theme
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"

        self.screen_manager = Manager()

        MainView = MainScreen(name='MainScreen')

        self.screen_manager.add_widget(FirstScreen(name='FirstScreen'))
        self.screen_manager.add_widget(MainView)
        self.screen_manager.add_widget(PropertyDetails(name='PropertyDetails'))

        Config.set('graphics', 'resizable', '0')
        Config.write()
        LabelBase.register("Plush_regular", r"C:\Users\scorp\Desktop\Programmin\Map App\fonts\Anonymous.ttf")

        return self.screen_manager

    def on_start(self):
        root = self.root

    def set_text(self, text, id):
        if "latitude" in str(id):
            self.latitude = text
        else:
            self.longitude = text
    def get_manager(self):
        return self.screen_manager




if __name__ != "__main__":
    pass
else:
    print("Running the app")
    app = MyApp()
    app.run()
