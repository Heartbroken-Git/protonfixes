""" Game fix for 911 First Responders, should work as well for Emergency 4 Deluxe (untested)
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Uses a x32 prefix, winetricks to install the directX 9 and ensures us of native quartz lib
    """

    log('Applying fixes for 911 First Responders')

    log('Using a win32 prefix')
    util.use_win32_prefix()

    log('Installing DirectX 9')
    util.protontricks('d3dx9_43')

    log('Overriding quartz lib to native')
    util.winedll_override('quartz', 'n')

