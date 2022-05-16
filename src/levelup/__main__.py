import sys
from levelup.game import GameUI

try:
    ui = GameUI()
    ui.start()
except KeyboardInterrupt:
    sys.exit()
