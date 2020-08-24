from enum import Enum

class GameState(Enum):
  Configuring = 'Please select the number of players.'
  Ready = 'Please click start to begin.'

class Game():
  def __init__(self, players):
    self.players = players
    self.state = GameState.Configuring

  def set_players(self, players):
    self.players = players
    self.state = GameState.Ready

  def players_scores(self):
    return [*map(lambda player: player.score, self.players)]

  def over(self):
    for player in self.players:
      if player.completed_all_targets() and player.has_winning_score(self.players_scores()):
        return True
