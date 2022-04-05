import gnupg
from fs import open_fs
import sys

from utils import get_payload_list

gpg = gnupg.GPG(gnupghome='/home/atef/.gnupg')
home_fs = open_fs(".")


def sign_file(filename, transaction, prev_block):
    with open(prev_block) as f:  # Reads the last line from the prev_block which is the prev_hash
        prev_hash = f.readlines()[-1]
        f.close()
    with open(prev_block) as file:  # Get the Payload from the prev_block and append to it the new transactions
        payload = get_payload_list(prev_block)
        payload.append(transaction)
        print(payload)

    with open(filename, "w+") as file:  # Write the new Payload to the new Block/File
        file.write(prev_hash + "\n")
        for i in payload:
            file.write(i)
        # file.write(prev_hash + "\n" + transaction)
        signed_data = gpg.sign_file(file, passphrase="thisisformybachelorarbeit")  # Signing prev_hash + new Payload
        file.write("\n" + str(signed_data))

# sign_file(str(sys.argv[1]), str(sys.argv[2]), sys.argv[3])