class Pos:
    def __init__(self, line, col):
        self.__line = line
        self.__col = col
    
    def advince(self):
        self.col = self.col + 1
    
    @property
    def line(self):
        return self.__line
    
    @line.setter
    def line(self, value):
        if value < 0:
            raise ValueError("line must be positive")
        self.__line = value
    
    @property
    def col(self):
        return self.__col
    
    @col.setter
    def col(self, value):
        if value < 0:
            raise ValueError("col must be positive")
        self.__col = value
    
    def __str__(self):
        return f"({self.line}, {self.col})"