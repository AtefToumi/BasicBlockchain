import gnupg
from fs import open_fs

gpg = gnupg.GPG(gnupghome='/home/atef/.gnupg')
home_fs = open_fs(".")


# Looking up the index where the payload stops in the file and reading from line 1 to the index to get the payload back
def get_payload_list(filename):
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
def get_payload(filename):
    payload_list = get_payload_list(filename)
    payload = ''.join(payload_list)
    return payload

