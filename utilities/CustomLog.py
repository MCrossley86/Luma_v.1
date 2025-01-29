import logging
import os

class LogGenerator():
    @staticmethod
    def get_logger():
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        log_path = os.path.join(project_root, 'logs')
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_file = os.path.join(log_path, "automation.log")
        logger = logging.getLogger('luma_automation')
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                '%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p',
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.propagate = False
        return logger



