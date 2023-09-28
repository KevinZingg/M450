#  Copyright Siemens AG, 2022 - 2023
#  Licensed under the Siemens Inner Source License, see LICENSE
__author__ = 'Daniel Panizza'
__version__ = '23.250'
__maintainer__ = 'Daniel Panizza'
__status__ = 'Development'  # Development | Production

import os
from os import listdir
from os.path import isfile, join


def load_sie_env(debug: bool = False) -> None:
    """ Load the Windows environment file .env                                                                  v 23.248
    :param debug: boolean
    """
    print(f'#REQ# Load sie39 environment with debug={debug} on os: {os.name}')
    # mypath = 'C:\\python\\code.webseitesicherheitspruefer'
    mypath = os.path.dirname(os.getcwd())
    if debug:
        only_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        prn(f'DEBUG: files in folder (get cwd): {only_files}', debug)
    if os.name == 'posix':  # posix nt java - running in azure
        os.environ['log_level'] = '10'
        return
    if os.name == 'nt':
        try:
            with open(f'{mypath}//.env', mode='r') as f:
                read_line(f, debug=debug)
        except FileNotFoundError:
            prn(f' dot_env file not found: .env')
        prn(f'  env {os.environ}', False)
        prn(f'  os.getenv app_name: {os.environ["app_name"]}', True)


def prn(msg: str, debug: bool = False) -> None:
    """ Print a message if in DEBUG mode                                                                        v 22.238
    :param debug: boolean
    :param msg: message
    """
    if debug:
        print(msg)


def read_line(f: iter, debug: bool) -> None:
    """ Readline thru a .env file                                                                               v 22.336
    :param f: file
    :param debug: bool
    """
    for line in f:
        prn(f' line in .env: {line.strip()}', debug=False)
        if len(line) < 2:
            continue
        line = line.strip()
        prn(f' line strip(): {line}', False)
        if line.startswith('#'):
            continue
        if line.find('=') > 0:
            prn(f' line: {line}', False)
            e = line.split('=')
            if len(e) > 2:
                print("1 - line with pwd_mail")
                e[1] = e[1] + "=" + e[2]
                e[1] = e[1].strip("'")
                prn(f'   file .env: {e[0]}', debug)
                os.environ[e[0]] = e[1]
                print(f"pwd_mail output {os.environ[e[0]]}")
            if len(e) == 2:
                # print("2 - line with pwd_mail")
                e[1] = e[1].strip("'")
                prn(f'   file .env: {e[0]}', debug)
                # prn(f' valid .env: {e[0]} = |{e[1]}|', False)
                os.environ[e[0]] = e[1]
            else:
                continue
