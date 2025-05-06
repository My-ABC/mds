from Tokens.make_token import Lexer
from Ast.ast import Parser

if __name__ == '__main__':
    from Context.context import Context
    context = Context("<stdin>")
    while True:
        code = input(">>> ")
        if code.strip() == "":
            continue
        res, err = Lexer(context,code).make_tokens()
        if err is not None:
            print(err.to_tryback())
        else:
            res = Parser(res).parse()
            print(res)
