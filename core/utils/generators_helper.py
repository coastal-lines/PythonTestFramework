import random
import uuid


def generate_uid() -> str:
    uid = uuid.uuid4()
    return str(uid)

def generate_int(start_number=0, end_number=12) -> int:
    temp_generated_int = []
    while start_number <= end_number:
        temp_generated_int.append(random.randint(0, 9))
        start_number += 1

    return int("".join(map(str, temp_generated_int)))