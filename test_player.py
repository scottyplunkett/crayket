import unittest
from player import Player
from test_helpers import stub_finished_targets, stub_unfinished_targets
from helpers import new_target, TARGET_VALUES

class TestPlayer(unittest.TestCase):
    def test_add_shot_to_target(self):
        player = Player('1', 0, stub_unfinished_targets())
        player.targets[0]['shots'] = 0
        player.targets[0]['value'] = TARGET_VALUES[0]
        player.targets[0]['status'] = 'unopened'
        player.add_shots_to_target(TARGET_VALUES[0], 1)
        self.assertEqual(player.targets[0]['shots'], 1)
        self.assertEqual(player.targets[0]['status'], 'unopened')

    def test_player_completed_all_targets_true_when_all_targets_closed(self):
        player = Player('1', 0, stub_finished_targets())
        self.assertTrue(player.completed_all_targets)

    def test_player_has_winning_score_true_when_greater_than_or_equal_to_best_in_all_scores(self):
        player = Player('1', 100, stub_finished_targets())
        self.assertTrue(player.has_winning_score([99, 1, 23, 100]))

    def test_player_get_name_returns_name(self):
        player = Player('Expected Name', 100, stub_finished_targets())
        self.assertEqual('Expected Name', player.get_name())

    def test_player_representation_returns_a_string_with_name_and_score(self):
        player = Player('Expected Name', 100, stub_finished_targets())
        self.assertEqual('Expected Name 100', player.representation()) 


if __name__ == '__main__':
    unittest.main()