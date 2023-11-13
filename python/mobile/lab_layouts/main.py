from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.metrics import dp


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            # b = Button(text=str(i+1), size_hint=(.1, .1)) # buttons have dynamic size
            b = Button(text=str(i + 1), size_hint=(None, None), size=(dp(100), dp(100)))    # fixed size
            self.add_widget(b)


class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):  # the box layout can do the job of organizing the text for you
    pass
    """def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal" # defines how the screen will be divided
        b1 = Button(text="A")   # creates the button and defines the property text
        b2 = Button(text="B")
        self.add_widget(b1) # adds the button to the screen
        self.add_widget(b2)"""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
