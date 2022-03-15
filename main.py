from utils import hash_file


class DreamCoinsBlock:

    def __init__(self, filename, transaction):
        self.filename = filename
        self.transaction = transaction

    def add_block(self):
        # f = open(self.filename, "w")
        # f.write(self.transaction)
        hash_file(self.filename, self.transaction)
        # sign_file(self.filename)

    # transaction = "Anna sends 3 DC to Mike"
    # add_block( transaction,"T1",transaction)


t1 = "Anna sends 2 DC to Mike"
t2 = "Bob sends 4.1 DC to Mike"
t3 = "Mike sends 3.2 DC to Bob"
t4 = "Daniel sends 0.3 DC to Anna"
t5 = "Mike sends 1 DC to Charlie"
t6 = "Mike sends 5.4 DC to Daniel"

initial_block = DreamCoinsBlock("T1", t2)
initial_block.add_block()

# second_block = DreamCoinsBlock("T1",t2)
#
# initial_block = DreamCoinsBlock("Initial String", [t1, t2])
#
# print(initial_block.block_data)
# print(initial_block.block_hash)
#
# second_block = DreamCoinsBlock(initial_block.block_hash, [t3, t4])
#
# print(second_block.block_data)
# print(second_block.block_hash)
#
# third_block = DreamCoinsBlock(second_block.block_hash, [t5, t6])
#
# print(third_block.block_data)
# print(third_block.block_hash)
