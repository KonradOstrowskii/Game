import os
import sys

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the system path
parent_dir = os.path.join(current_dir, '..')
sys.path.insert(0, parent_dir)

# Now you can import your modules
from characters.player import Player
from items.equipment import Equipment

# Your game logic goes here
