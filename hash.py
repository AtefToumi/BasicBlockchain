import hashlib


# Hashes a file and writes the hashed string in the same file


# Computes hash of a string
def compute_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


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
        print("the hash of the block is : " + hashed_data)
        # f.write(hashed_data)
