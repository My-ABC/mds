from .token import *
from Pos import Pos
from Error import SxError

class Lexer:
    def __init__(self, context, code):
        self.context = context
        self.code = code
        self.pos = Pos(1, -1)
        self.pos.advince()
    
    def make_tokens(self):
        token = []
        self.lparan = 0
        self.op_v = False
        while self.pos.col < len(self.code):
            self.now_char = self.code[self.pos.col] \
                if self.pos.col < len(self.code) else None
            if self.now_char == ' ' or self.now_char == '\t':
                self.pos.advince()
            elif self.now_char in (list(DIGITS) + ["."]):
                res = self.make_number()
                if isinstance(res, Token):
                    token.append(res)
                else:
                    return [],res
                self.op_v = True
            elif self.now_char == "+":
                token.append(Token(TT_PLUS))
                self.pos.advince()
                self.op_v = False
            elif self.now_char == "-":
                token.append(Token(TT_MINUS))
                self.pos.advince()
                self.op_v = False
            elif self.now_char == "*" and self.op_v:
                token.append(Token(TT_MUL))
                self.pos.advince()
                self.op_v = False
            elif self.now_char == "/" and self.op_v:
                token.append(Token(TT_DIV))
                self.pos.advince()
                self.op_v = False
            elif self.now_char == "^" and self.op_v:
                token.append(Token(TT_POW))
                self.pos.advince()
                self.op_v = False
            elif self.now_char == "(":
                token.append(Token(TT_LPAREN))
                self.lparan += 1
                self.pos.advince()
            elif self.now_char == ")":
                token.append(Token(TT_RPAREN))
                self.lparan -= 1
                if self.lparan < 0:
                    return [], SxError(
                        self.code,
                        self.context,
                        "unmatched \")\"",
                        Pos(1, self.pos.col-1),
                        self.pos
                    )
                self.pos.advince()
            else:
                return [], SxError(
                    self.code,
                    self.context,
                    "invalid syntax",
                    Pos(1, self.pos.col-1),
                    self.pos
                )
        if self.lparan != 0:
            return [], SxError(
                self.code,
                self.context,
                "invalid syntax",
                Pos(1, len(self.code)-1),
                Pos(1, len(self.code))
            )
        if token[-1].type in (
            TT_PLUS, 
            TT_MINUS, 
            TT_MUL, 
            TT_DIV, 
            TT_POW
        ):
            return [], SxError(
                self.code,
                self.context,
                "invalid syntax",
                Pos(1, len(self.code)-1),
                Pos(1, len(self.code))
            )
        return token, None
    
    def make_number(self):
        number = ""
        d = 0
        while self.now_char != None:
            if self.now_char in DIGITS:
                number += self.now_char
                self.pos.advince()
            elif self.now_char == "." and d == 0:
                number += self.now_char
                d += 1
                self.pos.advince()
            elif d == 1 and self.now_char == ".":
                return SxError(
                    self.code,
                    self.context,
                    "invalid syntax",
                    self.pos,
                    Pos(1, len(self.code)-1)
                )
            elif self.now_char in LETTERS:
                return SxError(
                    self.code,
                    self.context,
                    "invalid decimal literal",
                    Pos(1, self.pos.col-2),
                    Pos(1, self.pos.col-1)
                    
                )
            else:
                break
            self.now_char = self.code[self.pos.col] \
            if self.pos.col < len(self.code) else None
        if d == 0:
            return Token(TT_INT, int(number))
        else:
            if number == ".":
                return SxError(
                    self.code,
                    self.context,
                    "invalid decimal literal",
                    Pos(1, len(self.code)-2),
                    Pos(1, len(self.code)-1)
                )
            if number[-1] == ".":
                number = number + "0"
            if number[0] == ".":
                number = "0" + number
            return Token(TT_FLOAT, float(number))