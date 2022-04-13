import uuid


def generate_random_string() -> str:
    return f'whitebox_{uuid.uuid4().hex}'
