#  Copyright Siemens AG, 2019 - 2021
#  Licensed under the Siemens Inner Source License, see LICENSE

__author__ = 'Daniel Panizza'
__version__ = '21.005'
__maintainer__ = 'Daniel Panizza'
__status__ = 'Development'  # Development | Production


def custom_filters():
    """ Custom filter                                                                                           v 21.005
    :return dict: filters
    """
    cf = {'jf_len': jf_len, 'jf_none': jf_none}
    return cf


def jf_len(txt: str, size: int = 30) -> str:
    """ Jinja2 filter, set max text length                                                                      v 20.366
    :param txt: default input
    :param size: max length
    :return str: text
    """
    if txt:
        if len(txt) > size:
            return txt[:size]
        return txt
    return ''


def jf_none(s) -> str:
    """ Jinja2 filter, do not show None                                                                         v 20.366
    :param s: object or None
    """
    if s:
        return str(s)
    return ''
