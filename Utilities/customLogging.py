import logging

class LogGen:

    @staticmethod
    def basiclogs():
        print("About to setup log file")
        #logging.basicConfig(format='%(ascitime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        #logging.basicConfig(filename=".\\Logs\ automation.log")
        #logger = logging.getLogger()
        handler = logging.FileHandler('.\\Logs\\automation3.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
