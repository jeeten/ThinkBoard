from common import log
logging = log.logging
def checkKey(dict, key):
    if isinstance(key, str) and key not in dict.keys():
        raise Exception("{} Key is missing!".format(key))
    elif isinstance(key, list) :
        logging.debug("validation: {} is tupple".format(key))
        for k in key:
            logging.debug("validation: {} iterating".format(k))
            if not k in dict.keys():
                logging.debug("validation: {} is not in dict".format(k))
                raise Exception("{} Key is missing!".format(k))
    else:
        pass
