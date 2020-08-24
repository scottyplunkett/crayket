# Crayket
The Darts Game– Cricket... But in A Ray's house.

# Dependencies
- [Python 3](https://www.python.org/downloads/)
- [Kivy](https://kivy.org/#download)

# Setup
In a terminal window–
1. Clone this Repository:
`git clone https://github.com/scottyplunkett/crayket`
2. Change directories into project root:
`cd crayket`

# Test
from the project root:
`python -m unittest discover .`

# Run
from the project root:
`python main.py`

# NOTES
We'll probably want to nuke most of this code and just start over fresh now that I understand how to separate the kivy presentation from the logic a little better. Doing lots of presentation work in the `main.py` file and a lot of this should instead be managed from the `crayket.ky` file. Also using plain python for the logic atm, see the `game.py` and `player.py` files as well as their associated test... This kinda business we should work on inside the kivy python files (`main.py`), to take better advantage of [Kivy Properties](https://kivy.org/doc/stable/gettingstarted/properties.html) and what not.
