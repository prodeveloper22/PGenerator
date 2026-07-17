import random

def generate_password(length=16):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))
    
print(generate_password())