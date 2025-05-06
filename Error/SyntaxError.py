from .error import Error
class SxError(Error):
    def __init__(self, code, context, msg, pos_s, pos_e):
        super().__init__(
            code, 
            context, 
            "SyntaxError", 
            msg, 
            pos_s, 
            pos_e
        )