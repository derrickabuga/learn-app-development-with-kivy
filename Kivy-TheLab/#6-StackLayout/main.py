from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

from kivy.uix.button import Button

class StackLayoutExample(StackLayout):
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for x in range(0, 15):
            button = Button(text=str(x + 1), size_hint = (.2, .2))
            self.add_widget(button)
    """
    passd

class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()