import hashlib
import random
import string
import sys

from utils import get_payload


def mine(prev_block):
    payload = get_payload(prev_block)
    print("The payload is :", payload)
    print("The hash of the payload is :", hashlib.sha256(payload.encode()).hexdigest())
    Found = False
    while not Found:
        random_string = "".join(
            random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for y in range(25))
        attempt = payload + random_string
        solution = hashlib.sha256(attempt.encode()).hexdigest()
        if solution.startswith("0000"):
            print(solution)
            Found = True

