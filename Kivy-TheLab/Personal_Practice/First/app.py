import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

"""
class Buttons(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        b1 = Button(text="B1")
        b2 = Button(text="B2")

        self.add_widget(b1)
        self.add_widget(b2)
"""

class BoxLayout(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class PracticeApp(App):
    def build(self):
        return BoxLayout()
    
if __name__ == '__main__':
    PracticeApp().run()