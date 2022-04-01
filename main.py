from utils import hash_file_v2,sign_file,verify_signature
import sys



class Block:

    def __init__(self, last_filename, new_filename, transaction):
        self.last_filename = last_filename
        self.new_filename = new_filename
        self.transaction = transaction

    def add_block(self):

        sign_file(self.new_filename, self.transaction,self.last_filename)
        hash_file_v2(self.new_filename)



t1 = "Anna sends 2 DC to Mike"
t2 = "Bob sends 4.1 DC to Mike"
t3 = "Mike sends 3.2 DC to Bob"
t4 = "Daniel sends 0.3 DC to Anna"
t5 = "Mike sends 1 DC to Charlie"
t6 = "Mike sends 5.4 DC to Daniel"
#

# hash_file("T1")
initial_block = Block(str(sys.argv[1]), str(sys.argv[2]), sys.argv[3])
initial_block.add_block()
# sign_file("T1")
# verify_signature("T1")


