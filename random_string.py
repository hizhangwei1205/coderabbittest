import random
import string

def generate_random_string(length=8, chars=None):
    """
    Generate a random string of specified length.
    
    Parameters:
        length (int): Length of the random string (default: 8).
        chars (str): Characters to sample from. If None, uses ASCII letters and digits.
    
    Returns:
        str: A randomly generated string.
    """
    if chars is None:
        # 默认使用：大小写字母 + 数字
        chars = string.ascii_letters + string.digits
    
    return ''.join(random.choice(chars) for _ in range(length))