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


def hash_file_v2(filename):
    with open(filename, "r") as f:
        data = f.read()
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
    with open(filename, "a") as file:
        file.write(hashed_data)
        # f.write(hashed_data)


# Looking up the index where the payload stops in the file and reading from line 1 to the index to get the payload back
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


def sign_file(filename, transaction, prev_block):
    with open(prev_block) as f:  # Reads the last line from the prev_block which is the prev_hash
        prev_hash = f.readlines()[-1]
        f.close()
    with open(prev_block) as file:  # Get the Payload from the prev_block and append to it the new transactions
        payload = get_payload(prev_block)
        payload.append(transaction)
        print(payload)

    with open(filename, "w+") as file:  # Write the new Payload to the new Block/File
        file.write(prev_hash + "\n")
        for i in payload:
            file.write(i)
        # file.write(prev_hash + "\n" + transaction)
        signed_data = gpg.sign_file(file, passphrase="thisisformybachelorarbeit")  # Signing prev_hash + new Payload
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


# Computes hash of a string
def compute_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


# Verify the hash of a given Block/File
def verify_block(filename):
    with open(filename) as f:  # Reading all the block except the last line;which contains the hash of the block
        data = f.readlines()[0:-1]
        to_hash = ""
        to_hash = to_hash.join(
            data)  # Readlines returns an array of strings, join them to get the whole string back

    with open(filename) as file:
        prev_hash = file.readlines()[-1]  # Reads the Hash put in the Block
        computed_hash = compute_hash(to_hash)  # Compute the Hash of the Block
        if prev_hash == computed_hash:  # Check if computed hash corresponds to the hash put in the Block
            # return True
            print("hash is valid")
        else:
            # return False
            print("hash is invalid")

# Verifies integrity of the Blockchain
# Looping from the last block to the first one
# Computing each Hash of a Block and comparing it to the Hash put at the end of the Block
# TODO : verifying signature for each block
def verify_blockchain(fileslist):
    index = len(fileslist) - 1
    print(index)
    while verify_block(fileslist[index]) and index >= 0:
        print("Block number " + str(index) + " is valid")
        index -= 1
        print(verify_block(fileslist[index]))
    if verify_block(fileslist[index]):
        print("The Blockchain is valid")
    else:
        print("Block number " + str(index) + " is invalid")

verify_block("T2")
# verify_blockchain(["T0", "T1", "T2"])
# verify_previous_block("T2")

# sign_file("T1")
# verify_signature("T1.asc")
# stream = open('T1', 'rb')
# signed_data = gpg.sign_file(stream, passphrase="thisisformybachelorarbeit", output="T1.asc")
# print(str(signed_data))
