from Model.Token import Token
from ViewModel.SingleCharacter import SingleCharacter
from ViewModel.MultiCharacter import MultiCharacterTokenizer

class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.__current_char_index = 0
        self.__current_lexeme = ""
        self.tokens: [Token] = []

    def tokenize(self):
        while self.__current_char_index <= len(self.text) -1:
            if SingleCharacter.is_single_char_token(self.__current_char()):
                self.__make_single_char_token()
                self.__check_and_make_MultiCharacter_token()
            else:
                self.__current_lexeme += self.__current_char()
            self.__advance_current_char_index()
        self.__check_and_make_MultiCharacter_token()
        self.tokens = sorted(self.tokens, key=lambda x: x.index)

    def __advance_current_char_index(self):
        self.__current_char_index += 1

    def __current_char(self):
        return self.text[self.__current_char_index]

    def __make_single_char_token(self):
        token = Token(index= self.__current_char_index + 1,
                      type=SingleCharacter.get_single_char_token(self.__current_char()),
                      value=self.__current_char())
        self.tokens.append(token)

    def __check_and_make_MultiCharacter_token(self):
        m = MultiCharacterTokenizer(self.__current_lexeme)
        if m.tokens is not None:
            self.tokens.append(Token(self.__current_char_index, type=m.tokens[0], value=m.tokens[1]))
            self.__current_lexeme = ''


t = """ahmed = 55 + 40"""
tokenize = Tokenizer(t)

tokenize.tokenize()

for i in tokenize.tokens:
    print(i.index, i.type, i.value)
