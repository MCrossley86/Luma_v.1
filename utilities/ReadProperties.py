# Import the necessary modules
import configparser
import os
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create object to read config file and define a path to the config file
config = configparser.RawConfigParser()
config_read_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"..",'configurations','config.ini')
config.read(config_read_path)
logging.debug(f"Config file read from: {config_read_path}")

class ReadConfig:
    @staticmethod
    def get_application_url():
        # Retrieve and return the base URL from the 'CommonInfo' file
        url = config.get('CommonInfo','baseURL')
        logging.debug(f"Application URL: {url}")
        return url

    @staticmethod
    def get_user_email():
        # Retrieve and return the user email from the 'CommonInfo' file
        user_email = config.get('CommonInfo', 'email')
        logging.debug(f"User Email: {user_email}")
        return user_email

    @staticmethod
    def get_password():
        # Retrieve and return the password from the 'CommonInfo' file
        password = config.get('CommonInfo', 'password')
        logging.debug(f"Password: {password}")
        return password
