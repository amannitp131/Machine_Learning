import logging

##set basic configuration 
logging.basicConfig(
    level=logging.DEBUG,
    datefmt="%Y-%m-%d-%H-%M-%S",
    handlers=[
        logging.FileHandler("arthimetic.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("arthimetic logger")


def add(a,b):
    logger.debug(f"adding two number {a} and {b} and getting result as {a+b}")
    return a+b


def subtract(a,b):
    logger.debug(f"subtracting two number {a} and {b} and getting result as {a-b}")
    return a-b



res1=add(2,5)


