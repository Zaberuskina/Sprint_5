import random
import string

def generate_random_email():
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    email = f"{random_part}@yandex.ru"
    return email
def generate_random_password():
    random_password = ''.join(random.choices(string.digits, k=6))
    return random_password

