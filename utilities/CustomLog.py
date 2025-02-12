import logging
import os

class LogGenerator:

    @staticmethod
    def get_logger():
        # create path to "logs" directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        log_path = os.path.join(project_root, 'logs')
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_file = os.path.join(log_path, "automation.log")

        # setup the root logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # clear previous handlers
        if logger.hasHandlers():
            logger.handlers.clear()

        # create a new file handler with the desired format
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
                '%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p',
            )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # add the file handler to the root logger
        logger.propagate = True
        return logger



