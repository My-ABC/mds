class Error:
    def __init__(self, code, context, errn, msg , pos_s, pos_e):
        self.code = code
        self.context = context
        self.errn = errn
        self.msg = msg
        self.pos_s = pos_s
        self.pos_e = pos_e
    
    def to_tryback(self):
        msg = ""
        msg += f"  File \"{self.context.at}\", line {self.pos_s.line}\n"
        msg += f"    {self.code}\n"
        msg += f"    {self.pos_e.col*" "+(self.pos_e.col - self.pos_s.col)*"^"}\n\n"
        msg += f"{self.errn}: {self.msg}"
        return msg