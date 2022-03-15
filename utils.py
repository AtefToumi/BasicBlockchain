import hashlib

import gnupg
from fs import open_fs

gpg = gnupg.GPG(gnupghome='/home/atef/.gnupg')
home_fs = open_fs(".")


# Hashes a file and writes the hashed string in the same file
def hash_file(filename, transaction):
    data = open(filename)
    data_transactions = data.read()
    print(data_transactions)
    hashed_transaction = hashlib.sha256(transaction.encode()).hexdigest()
    print(hashed_transaction)
    hashed_data = open(filename, "a")
    hashed_data.write("\n"+"||| Transaction : " + transaction+" ||| Hash : " + hashed_transaction)
    # print(data.read())




# Signs a file using gpg, creates a ".asc" file and prints the status
def sign_file(filename):
    stream = open(filename, 'rb')
    signed_data = gpg.sign_file(stream, passphrase="thisisformybachelorarbeit", output=filename + ".asc")
    print("status : ", signed_data.status)


# Verifies the signature of the file and prints if the signature is valid or invalid
def verify_signature(filename):
    stream = open(filename, 'rb')
    verified = gpg.verify_file(stream)
    if verified.status == "signature valid":
        print("Signature is valid")
    else:
        print("Signature is invalid")

#
# sign_file("T1")
# verify_signature("T1.asc")
# stream = open('T1', 'rb')
# signed_data = gpg.sign_file(stream, passphrase="thisisformybachelorarbeit", output="T1.asc")
# print(str(signed_data))
