import configparser
import os

config = configparser.RawConfigParser()
config_read_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"..",'configurations','config.ini')
config.read(config_read_path)

class ReadConfig():
    @staticmethod
    def getapplicationurl():
        url = config.get('CommonInfo','baseURL')
        return url
