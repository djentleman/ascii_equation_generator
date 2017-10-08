


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

    def add_padding_horizontal(self, rows):
        self.block = ((rows/2)*[([' ']*self.get_width())]) + self.block
        self.block = self.block + ((rows-(rows/2))*[([' ']*self.get_width())])

    def add_padding_veritcal(self, cols):
        for i in range(self.get_height()):
            self.block[i] = ((cols/2)*[' ']) + self.block[i] + ((cols-(cols/2))*[' '])

    def concatinate_block_horizontal(self, concat_block):
        offset = self.get_height() - concat_block.get_height()
        # if offset is positive, add rows to concat_block
        if offset < 0:
            self.add_padding_horizontal(abs(offset))
        elif offset > 0:
            concat_block.add_padding_horizontal(offset)

        new_block = []
        # put current block first
        for i in range(self.get_height()):
            new_block.append(self.block[i] + concat_block.block[i])
        self.block = new_block

    def concatinate_block_vertical(self, concat_block):
        offset = self.get_width() - concat_block.get_width()
        if offset < 0:
            self.add_padding_veritcal(abs(offset))
        elif offset > 0:
            concat_block.add_padding_vertical(offset)

        self.block = self.block + concat_block.block
    
        
    def print_block(self):
        for row in self.block:
            print row

    def export(self):
        return '\n'.join([''.join(row) for row in self.block])
