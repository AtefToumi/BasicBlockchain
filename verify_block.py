import gnupg
from fs import open_fs

from hash import compute_hash

gpg = gnupg.GPG(gnupghome='/home/atef/.gnupg')
home_fs = open_fs(".")


# Verify the hash of a given Block/File


def verify_block(filename):
    results =""
    with open(filename) as f:  # Reading all the block except the last line;which contains the hash of the block
        data = f.readlines()[0:-1]
        to_hash = ""
        to_hash = to_hash.join(
            data)  # Readlines returns an array of strings, join them to get the whole string back


    with open(filename) as file:
        prev_hash = file.readlines()[-1]  # Reads the Hash put in the Block
        results += "The Hash saved in the file is : " + prev_hash + " >>>>>> "
        computed_hash = compute_hash(to_hash)  # Compute the Hash of the Block
        results += "Hashing the DATA to compare it to the hash saved in the file :  " + computed_hash
        if prev_hash == computed_hash:  # Check if computed hash corresponds to the hash put in the Block
            print("HASH IS VALID")
            results += " =====> HASH IS VALID"
            return results
        else:
            print("HASH IS INVALID")
            results+=" =====> HASH IS INVALID"
            return results


# verify_block(str(sys.argv[1]))


# Verifies the signature of the file and prints if the signature is valid or invalid
def verify_signature(filename):
    stream = open(filename, 'rb')
    verified = gpg.verify_file(stream)
    print(verified.status)
    if verified.status == "signature valid":
        print("Signature is valid")
        return True
    else:
        print("Signature is invalid")
        return False
