from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout

from kivy.properties import StringProperty

from kivy.metrics import dp

from kivy.uix.button import Button

class PageLayoutExample(PageLayout):
    pass

class ScrollViewExample(ScrollView):
    pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for x in range(0, 100):
            button = Button(text=str(x + 1), size_hint = (None, None), size = (dp(100), dp(100)))
            self.add_widget(button)

class WidgetsExample(GridLayout):
    count = 1
    can_count = False
    my_text = StringProperty("1")

    def on_but_click(self):
        print("Button clicked!")
        if self.can_count:
            self.count += 1
            self.my_text = str(self.count)
    
    def on_toggle_but_state(self, toggle_button):
        print("Toggle State:" + toggle_button.state)
        if toggle_button.state == "normal":
            #OFF
            toggle_button.text = "OFF"
            self.can_count = False
        else:
            #ON
            toggle_button.text = "ON"
            self.can_count = True

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