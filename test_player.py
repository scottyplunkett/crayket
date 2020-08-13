import unittest
from player import Player
from test_helpers import stub_finished_targets

class TestPlayer(unittest.TestCase):
    def test_player_completed_all_targets_true_when_all_targets_closed(self):
        player = Player('1', 0, stub_finished_targets())
        self.assertTrue(player.completed_all_targets)

    def test_player_has_winning_score_true_when_greater_than_or_equal_to_best_in_all_scores(self):
        player = Player('1', 100, stub_finished_targets())
        self.assertTrue(player.has_winning_score([99, 1, 23, 100]))

if __name__ == '__main__':
    unittest.main()