import random, string


def generate_name():
    letters = string.ascii_uppercase + string.digits
    name = random.choice(string.ascii_uppercase)
    name += ''.join(random.choice(letters) for i in range(7))
    return name