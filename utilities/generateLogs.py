import logging

# logging.basicConfig(filename="../logs/logfil1.log", format='%(asctime)s: %(levelname)s: %(message)s',
#                     datefmt='%m/%d/%y %I:%M:%S %p', level=logging.INFO)
#
# log = logging.getLogger()
# log.error("i am in error block")
# log.info("this is surendra jaganadam")

def log():
    logging.basicConfig(filename="../reports/logs/logfil1.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%y %I:%M:%S %p', level=logging.INFO)
    logger = logging.getLogger()
    return logger

# logger = log()
# logger.info("this is from a function or utility")
