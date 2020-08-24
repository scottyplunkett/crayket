import random
from helpers import TARGET_VALUES, new_target

def stub_finished_targets():
    return list(map(lambda v: new_target(v, 3, 'closed'), TARGET_VALUES))

def stub_unfinished_targets():
    return list(map(lambda v: new_target(v, random.choice([0, 1, 2]), 'open'), TARGET_VALUES))