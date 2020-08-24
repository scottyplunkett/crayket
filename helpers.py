TARGET_VALUES = ["20", "19", "18", "17", "16", "15", "B"]

def new_target(value, shots = 0, status = 'unopened'):
    return { 'value': value, 'shots': shots, 'status': status }

def new_targets():
    return list(map(new_target, TARGET_VALUES))
