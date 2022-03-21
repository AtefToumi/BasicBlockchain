from utils import hash_file,sign_file,verify_signature


class DreamCoinsBlock:

    def __init__(self, last_filename, new_filename, transaction):
        self.last_filename = last_filename
        self.new_filename = new_filename
        self.transaction = transaction

    def add_block(self):
        with open(self.last_filename, "r") as file:
            lines = file.readlines()
            last_hash = lines[2]

        # f = open(self.filename, "w")
        # f.write(self.transaction)
        hash_file(self.new_filename, self.transaction, last_hash)
        # sign_file(self.new_filename)
        # sign_file(self.filename)


t1 = "Anna sends 2 DC to Mike"
t2 = "Bob sends 4.1 DC to Mike"
t3 = "Mike sends 3.2 DC to Bob"
t4 = "Daniel sends 0.3 DC to Anna"
t5 = "Mike sends 1 DC to Charlie"
t6 = "Mike sends 5.4 DC to Daniel"
#
initial_block = DreamCoinsBlock("T2", "T3", t3)
initial_block.add_block()
# sign_file("T2")
# verify_signature("T1")


