import random
import time

def execute_action(action):
    print(f"Executing: {action}")
    time.sleep(1)

    success = random.choice([True, False, True])

    if success:
        return "SUCCESS"

    return "FAILED"
