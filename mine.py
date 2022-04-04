import hashlib
import random
import string

# this is a mining Script
# gets a phrase as input
# adds a random string and hashes it at each iteration
# prints all the hashes that starts with five zero's
phrase = input("Enter a phrase please : ")
print("The phrase is :", phrase)
print("The hash of the phrase is :", hashlib.sha256(phrase.encode()).hexdigest())
# zeros = input("Enter the number of zeros : ")

for x in range(0, 10000000):
    random_string = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for y in range(25))
    attempt = phrase + random_string
    solution = hashlib.sha256(attempt.encode()).hexdigest()
    if solution.startswith("00000"):
        print(solution)
