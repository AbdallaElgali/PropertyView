from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDIconButton
from kivy.resources import resource_add_path
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.factory_registers import Factory
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.label import Label
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivymd.uix.list import OneLineListItem
from kivy.clock import Clock
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.fitimage import FitImage
from kivymd.uix.textfield import MDTextField
from kivy.graphics import Color, Line, Ellipse

# Add image to resource path
resource_add_path(r'C:\Users\scorp\Desktop\Programmin\Map App\imgs')

Window.size = (480, 800)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_nav_drawer(self):
        for id, obj in self.ids:
            if id == 'nav_drawer':
                return id

class FirstScreen(Screen):
    pass

class PropertyDetails(Screen):
    pass
class Manager(ScreenManager):
    pass

class MyScrolLView(ScrollView):
    pass

class Logo(FitImage):
    pass

class ValueLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 12
        self.font_name = r'C:\Users\scorp\Desktop\Programmin\Map App\fonts\RobotoSlab.ttf'
        #self.color = (240/255, 240/255, 240/255, 1)
        #self.color = (1, 165/255, 10/255, .9)
        self.color = (1, 1, 1, 1)
class DropDownButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(44)
        self.background_normal = ''  # Remove default background
        self.background_color = (.119, .136, .153, .8)  # Custom background color
        self.color = (1, 165/255, 10/255, .9)  # Text color
        self.font_size = 16  # Font size

class SearchField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = DropDown()
        self.bind(on_text=self.on_text)
        self.dropped = False  # Track initial state of the dropdown widget

        # Populate dropdown with initial suggestions
        self.update_dropdown()

    def on_text(self, instance, value, *args):
        self.update_dropdown()

    def update_dropdown(self):
        app = MDApp.get_running_app()
        model = app.model_ins
        suggestions = model.find_suggestions(self.text)

        # Clear existing dropdown items
        self.dropdown.clear_widgets()

        # Populate dropdown with suggestions
        if suggestions:
            for suggestion in suggestions:
                btn = DropDownButton(text=suggestion)
                btn.bind(on_release=lambda btn: self.select_suggestion(btn.text))

                self.dropdown.add_widget(btn)

            # Show dropdown below the SearchField
            if self.focus and not self.dropped:
                self.dropdown.open(self)
                self.dropped = True
            else:
                self.dropdown.dismiss()
                self.dropped = False

                if self.focus:  # Second character

                    self.dropdown.dismiss()
                    self.dropdown = DropDown()

                    for suggestion in suggestions:
                        btn = DropDownButton(text=suggestion)
                        btn.bind(on_release=lambda btn: self.select_suggestion(btn.text))
                        self.dropdown.add_widget(btn)

                    self.dropdown.open(self)
                    self.dropped = True


    def select_suggestion(self, suggestion):
        self.text = suggestion
        self.dropdown.dismiss()
        self.dropped = False

    def my_callback(self, dt):
        print(dt)

class GoBackListItem(OneLineListItem):
    def release(self):
        app = MDApp.get_running_app()
        def delayed_action(*args):
            app.root.current = "FirstScreen"

        # Schedule the delayed_action function to run after 0.5 seconds (for example)
        Clock.schedule_once(delayed_action, 0.2)


class MenuButton(MDIconButton):
    pass

class MarkerButton(MDRoundFlatButton):
    pass

class Details_button(MDRoundFlatButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = ' Details '

    def release(self, *args):
        app = MDApp.get_running_app()
        app.screen_manager.current = "PropertyDetails"
        app.screen_manager.transition.direction = 'left'
        self.parent.parent.parent.parent.dismiss()

class MyMapMarker(MapMarkerPopup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.marker_text = StringProperty("")
        self.source = r'C:\Users\scorp\Desktop\Programmin\Map App\imgs\marker.png'
        self.size_hint = (None, None)  # Disable size_hint so that size can be set directly
        self.size = (50, 50)  # Set the size of the marker to (50, 50) or any other desired size


    def on_release(self):
        # Define what happens when the marker is clicked
        content_sheet = Factory.ContentCustomSheet()
        app = MDApp.get_running_app()

        details_btn_ins = Details_button()
        details_btn_ins.pos_hint = {'center_x': .5, 'center_y': .5}
        details_btn_ins.bind(on_release=details_btn_ins.release)

        sheet_label = content_sheet.ids.sheet_label
        address = app.model_ins.find_location(self.lat, self.lon)
        sheet_label.text = f'Address: {address[:20]}'
        content_sheet.add_widget(details_btn_ins)
        sheet = MDCustomBottomSheet(screen=content_sheet)
        sheet.open()

    def set_text(self, text):
        self.marker_text = text

class AbuDhabiMap(MapView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.coordinates = self.get_coordinates()


        for coordinate in self.coordinates:
            text, latitude, longitude = coordinate[0], coordinate[1], coordinate[2]
            marker = self.create_map_marker(latitude, longitude, text)
            marker.set_text(text)
            self.add_marker(marker)

    def create_map_marker(self, lat, lon, popup_text):

        marker = MyMapMarker(lat=lat, lon=lon)

        '''
        bubble = Bubble(size=(300, 150))
        box_layout = MDBoxLayout(orientation='vertical')
        label = MDLabel(text=popup_text)
        box_layout.add_widget(label)
        bubble.add_widget(box_layout)
        marker.add_widget(bubble)
        
        '''

        return marker

    def get_coordinates(self):
        app = MDApp.get_running_app()
        return app.coordinates

class RelativeLayout(MDRelativeLayout):
    def do_layout(self, *args):
        for child in self.children:
            child.size = self.size
            child.pos = self.pos


class NextButton(MDRoundFlatButton):
    pass

class CustomIconButton(MDIconButton):
    pass


class Icon(MDIconButton):
    def on_release(self):
        print('Icon pressed')

class BoxLayout(MDBoxLayout):
    pass

