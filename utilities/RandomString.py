# Import the necessary modules
import random
import string
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Log the action and generate a random string
def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    logging.debug(f"Generating random string of size {size} using chars: {chars}")
    return ''.join(random.choice(chars) for _ in range(size))