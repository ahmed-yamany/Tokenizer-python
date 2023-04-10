SINGLE_CHARACTER_TOKENS = {
    "+": "PLUS",
    "-": "MINUS",
    '*': 'MULT',
    "/": 'DEVIATION',
    '(': 'RIGHTPAREN',
    ')': 'LEFTPAREN',
    '.': 'DOT',
    ',': 'COMA',
    ' ': "SPACE",
    '=': "EQUAL",
    '\n': "NEWLINE"
}

class SingleCharacter:
    @staticmethod
    def is_single_char_token(char):
        return char in SINGLE_CHARACTER_TOKENS.keys()

    @staticmethod
    def get_single_char_token(char):
        return SINGLE_CHARACTER_TOKENS[char]
