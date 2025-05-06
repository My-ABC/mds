class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value is None:
            return f'{self.type}'
        return f'{self.type}:{self.value}'
        
DIGITS = '0123456789'
import string
LETTERS = string.ascii_letters

TT_INT    = 'INT'
TT_FLOAT  = 'FLOAT'
TT_PLUS   = 'PLUS'
TT_MINUS  = 'MINUS'
TT_MUL    = 'MUL'
TT_DIV    = 'DIV'
TT_POW    = 'POW'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'