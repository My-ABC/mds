from Tokens import *
from .node import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_tok = self.tokens[0] if tokens else None

    def advance(self):
        self.pos += 1
        self.current_tok = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        return self.current_tok

    def parse(self):
        return self.expr()
    #######################
    # 优先级处理（从低到高）
    #######################
    def expr(self):
        """加减法（最低优先级）"""
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

    def term(self):
        """乘除法（中等优先级）"""
        return self.bin_op(self.factor, (TT_MUL, TT_DIV))

    def factor(self):
        """乘方（右结合）"""
        return self.bin_op(self.unary_op, (TT_POW,), right_associative=True)

    #######################
    # 一元运算符和原子表达式
    #######################
    def unary_op(self):
        """处理连续一元运算符（如 --+-3）"""
        # 收集所有连续一元运算符
        ops = []
        while self.current_tok and self.current_tok.type in (TT_PLUS, TT_MINUS):
            ops.append(self.current_tok)
            self.advance()
        
        # 获取底层表达式
        node = self.atom()
        
        # 从右向左应用运算符（数学标准：--3 = -(-3)）
        for op in reversed(ops):
            node = UnaryOpNode(op, node)
        
        return node

    def atom(self):
        """处理数字和括号表达式"""
        tok = self.current_tok
        
        # 处理数字
        if tok.type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(tok)
        
        # 处理括号
        elif tok.type == TT_LPAREN:
            self.advance()
            
            # 检查是否为空括号 ()
            if self.current_tok and self.current_tok.type == TT_RPAREN:
                self.advance()
                # 创建值为0的数字节点，位置信息使用原括号位置
                return NumberNode(Token(TT_INT, 0))
            
            # 非空括号的正常处理
            expr_node = self.expr()
            
            self.advance()
            return expr_node

    #######################
    # 通用二元操作处理
    #######################
    def bin_op(self, func, ops, right_associative=False):
        """处理二元运算符的通用逻辑"""
        left = func()
        
        while self.current_tok and self.current_tok.type in ops:
            op_tok = self.current_tok
            self.advance()
            
            # 右结合运算符（如乘方）递归调用自身，左结合调用下一优先级
            right = self.bin_op(func, ops, right_associative) if right_associative else func()
            
            left = BinOpNode(left, op_tok, right)
        
        return left