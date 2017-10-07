


class TextBlock():
    def __init__(self, instr):
        self.block = [list(row) for row in instr.split('\n')]
        # all need to be the length of the longest row
        max_row_size = max([len(row) for row in self.block])
        self.block = map(lambda x: x + [' ']*(max_row_size-len(x)), self.block)

    def get_width(self):
        return len(self.block[0])

    def get_height(self):
        return len(self.block)

    def add_padding(self, rows):
        self.block = ((rows/2)*[([' ']*self.get_width())]) + self.block
        self.block = self.block + ((rows-(rows/2))*[([' ']*self.get_width())])

    def concatinate_block(self, concat_block):
        offset = self.get_height() - concat_block.get_height()
        # if offset is positive, add rows to concat_block
        if offset < 0:
            self.add_padding(abs(offset))
        elif offset > 0:
            concat_block.add_padding(offset)

        new_block = []
        # put current block first
        for i in range(self.get_height()):
            new_block.append(self.block[i] + concat_block.block[i])
        self.block = new_block
        
    def print_block(self):
        for row in self.block:
            print row

    def export(self):
        return '\n'.join([''.join(row) for row in self.block])
