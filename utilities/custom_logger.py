import logging

class LogMaker:
    @staticmethod
    def log_generate():
        logging.basicConfig(filename="C:\\Users\\pksin\\PycharmProjects\\SeleniumPythonProjects\\saucedemo\\logs\\saucedemo.log",
                            format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S",force= True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger