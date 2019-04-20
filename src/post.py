"""
Post

Represents a post made by a user
"""
import re
import random

class Post():
    def __init__(self, author: str = "No Author", contents: str = "CAW CAW CAW"):
        self.author = author
        self.contents = contents

# TODO write a util for converting human text into "CAW"s

# defines valid regex for a message
# valid_regex = re.compile('((k|c)r?a+w+\s?)+', flags=re.RegexFlag.I)

def translate_message(input: str) -> str:
    """
    Translate a sentence into CRAW speak

    >>> translate_message("Y'all ever just YEET?")
    'CAAWW CAAW CAAW CAAWW'

    """
    # TODO need to handle symbols and stuff
    return ' '.join([translate_word(x) for x in input.split()])

def translate_word(input: str) -> str:
    """
    Translate a word into CAW speak

    >>> translate_word("tests")
    'CAAWW'
    >>> translate_word("test")
    'CAAW'
    >>> translate_word("")
    ''
    >>> translate_word("a")
    'CA'
    >>> translate_word("ab")
    'CAW'
    >>> translate_word("abc")
    'CAW'

    """
    random.seed("CAAAAAWWWWW")
    if len(input) == 0:
        return ''
    if len(input) == 1:
        return 'CA'
    if len(input) == 2 or len(input) == 3:
        return 'CAW'
    # subtract the starting C and the ending W
    x = len(input) - 2
    # must have at least one A
    num_a = random.randint(1, x)
    return 'C' + ('A'*num_a) + ('W'*(x - (num_a - 1)))

