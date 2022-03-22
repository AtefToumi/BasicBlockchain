import hashlib

import gnupg
from fs import open_fs

gpg = gnupg.GPG(gnupghome='/home/atef/.gnupg')
home_fs = open_fs(".")


# Hashes a file and writes the hashed string in the same file

def hash_file(filename):
    BLOCK_SIZE = 65536  # The size of each read from the file

    file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(filename, 'rb') as f:  # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file
    hash = file_hash.hexdigest()
    with open(filename, "a") as file:
        file.write(str(hash))  # Get the hexadecimal digest of the hash


def hash_file_V2(filename):
    with open(filename, "r") as f:
        data = f.read()
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
    with open(filename, "a") as file:
        file.write(hashed_data)
        # f.write(hashed_data)


def get_payload(filename):
    lookup = '-----BEGIN PGP SIGNED MESSAGE-----'
    with open(filename, "r") as file:
        for num, line in enumerate(file, 1):
            if lookup in line:
                last_transaction = num - 1
        file.close()
    with open(filename) as f:
        return f.readlines()[1:last_transaction]
        # payload = file.readlines()[1:last_transaction]
        # print(payload)
        # return payload
        # return transactions


# Signs a file using gpg, creates a ".asc" file and prints the status
def sign_file(filename, transaction, prev_block):
    with open(prev_block) as f:
        prev_hash = f.readlines()[-1]
        f.close()
    with open(prev_block) as file:
        payload = get_payload(prev_block)
        payload.append(transaction)
        print(payload)

    with open(filename, "w+") as file:
        file.write(prev_hash + "\n")
        for i in payload:
            file.write(i)
        # file.write(prev_hash + "\n" + transaction)
        signed_data = gpg.sign_file(file, passphrase="thisisformybachelorarbeit")
        file.write("\n" + str(signed_data))


# Verifies the signature of the file and prints if the signature is valid or invalid
def verify_signature(filename):
    stream = open(filename, 'rb')
    verified = gpg.verify_file(stream)
    print(verified.status)
    if verified.status == "signature valid":
        print("Signature is valid")
    else:
        print("Signature is invalid")


def compute_hash(filename):
    with open(filename, "r") as file:
        to_hash = file.read()
        return hashlib.sha256(to_hash.encode()).hexdigest()


def verify_previous_block(filename):
    with open(filename) as f:
        to_hash = f.read()[0:-1]
        print(to_hash)
verify_previous_block("T1")
# verify_previous_block("T2")

# sign_file("T1")
# verify_signature("T1.asc")
# stream = open('T1', 'rb')
# signed_data = gpg.sign_file(stream, passphrase="thisisformybachelorarbeit", output="T1.asc")
# print(str(signed_data))
