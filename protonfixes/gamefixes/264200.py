""" Game fix for One Finger Death Punch
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Uses winetricks to install the dotnet40 verb
    """

    log('Applying fixes for One Finger Death Punch')

    log('Installing .NET Framework 4.0')
    util.protontricks('dotnet40')

    log('Disabling ESync prior to launching')
    util.disable_esync()

