class Game():
  def __init__(self, players):
    self.players = players

  def players_scores(self):
    return [*map(lambda player: player.score, self.players)]

  def over(self):
    for player in self.players:
      if player.completed_all_targets() and player.has_winning_score(self.players_scores()):
        return True
