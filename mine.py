import hashlib
import random
import string

from utils import get_payload


def mine(prev_block):
    # difficulty_input = int(input("Enter number of zeros for pow : "))
    difficulty = "00000"
    # for x in range(difficulty_input):
    #     difficulty += "0"

    payload = get_payload(prev_block)
    print("The payload is :", payload)
    print("The hash of the payload is :", hashlib.sha256(payload.encode()).hexdigest())
    Found = False
    while not Found:
        random_string = "".join(
            random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for y in range(25))
        attempt = payload + random_string
        solution = hashlib.sha256(attempt.encode()).hexdigest()
        if solution.startswith(difficulty):
            print("proof of work with " + "5" + " zeros sucessfully found : " + solution)
            Found = True
