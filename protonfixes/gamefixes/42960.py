""" Game fix for Victoria II
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying fixes for Victoria II')

    # Replace launcher with game exe in proton arguments
    log('Launching game exe instead or launcher')
    util.replace_command('victoria2.exe', 'v2game.exe')
