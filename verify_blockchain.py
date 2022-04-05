# Verifies integrity of the Blockchain
# Looping from the last block to the first one
# Computing each Hash of a Block and comparing it to the Hash put at the end of the Block
# TODO : verifying signature for each block
from verify_block import verify_block


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


