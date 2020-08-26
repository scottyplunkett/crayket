from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button, Label
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, ObjectProperty
from game import Game
from player import Player
from helpers import new_targets

class PlayerMenuButtons(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.btn1 = Button(text='1')
        self.btn1.bind(on_press=self.update)
        self.btn2 = Button(text='2')
        self.btn2.bind(on_press=self.update)
        self.btn3 = Button(text='3')
        self.btn3.bind(on_press=self.update)
        self.btn4 = Button(text='4')
        self.btn4.bind(on_press=self.update)
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.add_widget(self.btn4)

    def update(self, instance):
        print(instance)
        app = App.get_running_app()
        app.root.configure_players(instance)
        instance.parent.parent.show_current_players()


class PlayerMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label = Label(text="Select # of Players:")
        self.add_widget(self.label)
        self.player_menu_buttons = PlayerMenuButtons()
        self.add_widget(self.player_menu_buttons)

    def on_entered_something(self):
        self.label.text = f'User entered {self.input.text}'
        print('User entered', self.input.text)
        

    def get_player_name(self, player_number):
        self.input = TextInput(text=f'Enter player {player_number} name', multiline=False)
        self.add_widget(self.input)
        self.input.on_text_validate=self.on_entered_something


    def show_current_players(self):
        app = App.get_running_app()
        self.label.text = 'Current Players:'
        self.remove_widget(self.player_menu_buttons)
        self.current_players_label = Label(text=str(len(app.root.players)))
        self.add_widget(self.current_players_label)
        self.get_player_name(1)


class TurnMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Button(text='Undo'))
        self.add_widget(Button(text='Clear'))


class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(PlayerMenu())
        self.add_widget(TurnMenu())


class ScoreColumn(BoxLayout):
    def __init__(self, player, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.player = player
        self.add_widget(Label(text=self.player.name))
        for target in self.player.targets:
            self.add_widget(Label(text=str(target['shots'])))
        self.add_widget(Label(text=""))


class TargetsColumn(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="P", underline=True))
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
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.targets = TargetsColumn()
        self.add_widget(self.targets)

    def sync_players_to_sheet(self, players):
        for player in players:
            self.add_widget(ScoreColumn(player))


class Root(BoxLayout):
    players = ListProperty([])
    game = ObjectProperty(Game(players))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.label = Label(id='instruction', text=self.game.state.value)
        self.add_widget(self.label)
        self.sheet = Sheet()
        self.add_widget(self.sheet)
        self.menu = Menu()
        self.add_widget(self.menu)


    def configure_players(self, instance):
        self.players = []
        print("Set number to %s", instance.text)
        number = int(instance.text) - 1
        while (len(self.players) <= number):
            name = str(len(self.players) + 1)
            self.players.append(Player(name, 0, new_targets()))
        print(self.players)
        self.sheet.sync_players_to_sheet(self.players)
        self.set_game_players()

    def set_game_players(self):
        self.game.set_players(self.players)
        print(self.game.state.value)
        self.label.text = self.game.state.value


class CrayketApp(App):
    def build(self):
        return Root()

CrayketApp().run()

