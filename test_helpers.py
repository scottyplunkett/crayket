import random

values = ["20", "19", "18", "17", "16", "15", "B"]

def stub_target(value, shots = 3, status = 'closed'):
    return { 'value': value, 'shots': shots, 'status': status }

def stub_finished_targets():
    return map(stub_target, values)

def stub_unfinished_targets():
    return map(lambda v: stub_target(v, random.choice([0, 1, 2]), 'open'), values)