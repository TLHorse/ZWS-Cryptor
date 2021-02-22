import os, sys
from termcolor import colored
from ZWStringConverter import *

LAST_RESULT = ""
zws_instance = ZWStringConverter("")

def pbanner():
    banner = colored(f"""
      ______
     /___  /\\  Zerowidth String Cryptor | @TLHorse from 52pojie
    //  / / \\\\ Type in then ENTER. The encoded string will be printed.
    \\\\ / /__// Commands | ::openweb:: ::banner:: ::quit:: ::cp::
     \/_____/  
    """, 'yellow')
    print(banner)

def mode_colored(string: str):
    global zws_instance
    return colored(string, 'green' if zws_instance.isZWS() else 'red')

def getinput():
    global LAST_RESULT, zws_instance
    input_str = input("     >>> ")
    
    if   input_str == '::openweb::':    os.system('open https://www.52pojie.cn')
    elif input_str == '::banner::':     pbanner()
    elif input_str == '::quit::':       sys.exit(0)
    elif input_str == '::cp::':         os.system(f'echo "{LAST_RESULT}" | pbcopy')
    if input_str.startswith("::") and input_str.endswith("::"): getinput()

    zws_instance.targetString = input_str
    info = f"[{mode_colored('ENCODE') if not zws_instance.isZWS() else mode_colored('DECODE')}]"

    out = zws_instance.convert()
    quot = mode_colored('"')
    print(f'{info} {quot}{out}{quot}')
    LAST_RESULT = out
    getinput()

pbanner()
getinput()
