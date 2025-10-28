import random
import string

def generate_random_string(length=8, chars=None):
    """
    if chars is None:
        # 默认使用：大小写字母 + 数字
        chars = string.ascii_letters + string.digits
    
    return ''.join(random.choice(chars) for _ in range(length))