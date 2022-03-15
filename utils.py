import gnupg
from fs import open_fs

gpg = gnupg.GPG(gnupghome='/home/atef/.gnupg')
home_fs = open_fs(".")


# if os.path.exists("Signatures/"):
#     print("Signatures directory already created")
# else :
#     home_fs.makedir(u"Signatures")
#     print("Created signatures directory")

#Signs a file using gpg, creates a ".asc" file and prints the status
def sign_file(file):
    stream = open(file, 'rb')
    signed_data = gpg.sign_file(stream, passphrase="thisisformybachelorarbeit", output=file + ".asc")
    print("status : ", signed_data.status)

#Verifies the signature of the file and prints if the signature is valid or invalid
def verify_signature(file):
    stream = open(file, 'rb')
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
