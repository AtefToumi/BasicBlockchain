import sys
import time

from hash import hash_file_v2
from mine import mine
from sign_block import sign_file
from user import User


class Block:

    def __init__(self, last_filename, new_filename, transaction):
        self.last_filename = last_filename
        self.new_filename = new_filename
        self.transaction = transaction

    def add_block(self, user):
        print("signing block ..")
        time.sleep(2)
        sign_file(self.new_filename, self.transaction, self.last_filename, user)
        print("hashing block ..")
        time.sleep(2)
        hash_file_v2(self.new_filename)
        print("mining block ..")
        time.sleep(2)
        mine(self.last_filename)


t1 = "Anna sends 2 DC to Mike"
t2 = "Bob sends 4.1 DC to Mike"
t3 = "Mike sends 3.2 DC to Bob"
t4 = "Daniel sends 0.3 DC to Anna"
t5 = "Mike sends 1 DC to Charlie"
t6 = "Mike sends 5.4 DC to Daniel"
#
# last_block = input("Please enter the last Block in the Blockchain : ")
# new_block = input("Please enter the new Block's name : ")
# transaction = input("Enter the transaction details : ")
# user_id = input("Enter your id : ")
# user_passphrase = input("Enter your passphrase : ")

# block = Block(last_block, new_block, transaction)
# block.add_block(User(user_id, user_passphrase))

