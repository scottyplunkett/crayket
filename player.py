class Player():
    def __init__(self, name, score, targets):
        self.name = name
        self.score = score
        self.targets = targets

    def add_shots_to_target(self, value, amount):
        for target in self.targets:
          if target['value'] == value:
            target['shots'] = target['shots'] + amount

    def completed_all_targets(self):
        return all(target['status'] == 'closed' for target in self.targets)

    def has_winning_score(self, scores):
        return all(self.score >= score for score in scores)
