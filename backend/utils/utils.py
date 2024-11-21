import random
import string
from flask import jsonify


def resp(status: bool, **kwargs):
    res = {'status': status}
    res.update(kwargs)
    return jsonify(res)
    

def random_int(low, high):
    """Generate a random integer between low and high (inclusive)."""
    if low > high:
        raise ValueError("Low value must be less than or equal to high value")
    return random.randint(low, high)

def random_string(length):
    """Generate a random string of specified length."""
    if length < 1:
        raise ValueError("Length must be at least 1")
    
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))
