class NumberNode:
    def __init__(self, token):
        self.value = token.value
    
    def __repr__(self):
        return f'NumberNode({self.value})'

class BinOpNode:
    def __init__(self, left, op_token, right):
        self.left = left
        self.op = op_token
        self.right = right
    
    def __repr__(self):
        return f'BinOpNode({self.left}, {self.op}, {self.right})'

class UnaryOpNode:
    def __init__(self, op_token, node):
        self.op = op_token
        self.node = node
    
    def __repr__(self):
        return f'UnaryOpNode({self.op}, {self.node})'