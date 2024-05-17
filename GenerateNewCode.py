import random
import string

# Function to generate a random ID
def random_id():
    letters = string.ascii_lowercase  # Get lowercase letters
    return ''.join(random.choice(letters) for i in range(8))  # Join 8 random lowercase letters to form the ID
