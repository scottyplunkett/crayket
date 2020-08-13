import unittest
from game import Game
from player import Player
from test_helpers import stub_finished_targets, stub_unfinished_targets

class TestGame(unittest.TestCase):
    def test_players_scores_returns_list_of_all_players_scores(self):
        players = [
            Player('1', 50, stub_finished_targets()),
            Player('2', 67, stub_finished_targets()),
            Player('3', 85, stub_finished_targets()),
            Player('4', 15, stub_finished_targets())
        ]
        game = Game(players)
        self.assertEqual(game.players_scores(), [50, 67, 85, 15])

    def test_game_over_true_when_player_closes_all_targets_has_winning_score(self):
        winning_players_score = 100
        other_players_score = 99
        winning_player = Player('SKP', winning_players_score, stub_finished_targets())
        other_player = Player('AJR', other_players_score, stub_finished_targets())
        players = [ winning_player, other_player ]
        game = Game(players)
        self.assertTrue(game.over())

    def test_game_over_false_when_player_closes_all_targets_has_low_score(self):
        players_score = 98
        other_players_score = 99
        player = Player('SKP', players_score, stub_finished_targets())
        other_player = Player('AJR', other_players_score, stub_unfinished_targets())
        players = [ player, other_player ]
        game = Game(players)
        self.assertFalse(game.over())

if __name__ == '__main__':
    unittest.main()