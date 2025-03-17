# Import the necessary modules
import logging
import os

class LogGenerator:
    @staticmethod
    def get_logger():
        # Log the action and create a path to the "logs" directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        log_path = os.path.join(project_root, 'logs')
        logging.debug(f"Project root: {project_root}")
        logging.debug(f"Log path: {log_path}")

        # If the logs directory doesn't exist, create one and log it
        logging.info(f"Creating logs directory at {log_path}")
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        # Log the action and set the file path
        log_file = os.path.join(log_path, "automation.log")
        logging.debug(f"Log file path: {log_file}")

        # Log the action and set up the root logger
        logging.debug("Setting root logger to DEBUG level")
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # If previous handlers exist, clear them and log it
        logging.info("Clearing previous handlers from the logger")
        if logger.hasHandlers():
            logger.handlers.clear()

        # Log the action and create a new file handler with the desired format
        logging.debug("Adding new file handler to the logger")
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
                '%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p',
            )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Log the action and ensure logger propagates to the root logger
        logging.debug("Setting logger propagation to True")
        logger.propagate = True
        return logger