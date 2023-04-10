import re
class MultiCharacterTokenizer:
    token_specifications = [
        ('INTEGER', r'\d+'),

        ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ]

    def __init__(self, text):
        self.text = text
        self.tokens = self.__tokenize()

    def token_specifications_regex(self):
        return '|'.join('(?P<%s>%s)' % pair for pair in self.token_specifications)



    def __tokenize(self):
        for matched_object in re.finditer(self.token_specifications_regex(), self.text):
            type = matched_object.lastgroup
            value = matched_object.group()

            return (type, value)
