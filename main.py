from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button, Label

class PlayerMenuButtons(GridLayout):
    def __init__(self, **kwargs):
        super(PlayerMenuButtons, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Button(text='1'))
        self.add_widget(Button(text='2'))
        self.add_widget(Button(text='3'))
        self.add_widget(Button(text='4'))


class PlayerMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(PlayerMenu, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Select # of Players:"))
        self.add_widget(PlayerMenuButtons())


class TurnMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(TurnMenu, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Button(text='Undo'))
        self.add_widget(Button(text='Clear'))


class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(PlayerMenu())
        self.add_widget(TurnMenu())


class ScoreColumn(BoxLayout):
    def __init__(self, **kwargs):
        super(ScoreColumn, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="_"))
        self.add_widget(Label(text="_"))
        self.add_widget(Label(text="_"))
        self.add_widget(Label(text="_"))
        self.add_widget(Label(text="_"))
        self.add_widget(Label(text="_"))
        self.add_widget(Label(text="_"))
        self.add_widget(Label(text="_"))
        self.add_widget(Label(text="_"))


class TargetsColumn(BoxLayout):
    def __init__(self, **kwargs):
        super(TargetsColumn, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text=""))
        self.add_widget(Label(text="20"))
        self.add_widget(Label(text="19"))
        self.add_widget(Label(text="18"))
        self.add_widget(Label(text="17"))
        self.add_widget(Label(text="16"))
        self.add_widget(Label(text="15"))
        self.add_widget(Label(text="B"))
        self.add_widget(Label(text=""))


class Sheet(BoxLayout):
    def __init__(self, **kwargs):
        super(Sheet, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(ScoreColumn())
        self.add_widget(ScoreColumn())
        self.add_widget(TargetsColumn())
        self.add_widget(ScoreColumn())
        self.add_widget(ScoreColumn())


class Root(BoxLayout):
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(Sheet())
        self.add_widget(Menu())


class CrayketApp(App):
    def build(self):
        return Root()


if __name__ == "__main__":
    CrayketApp().run()

