import copy
import logging
import comments
import subprocess
import pprint

# create logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler("python_training.log")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s- %(levelname)s - %(filename)s-%(lineno)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)

#list_of_data = [1234, 234, 456, 43]
# new_data = list_of_data
# new_data.append(100)
# logger.info(list_of_data)
# logger.info(new_data)
#
#
# new_data = list_of_data.copy()
# new_data.append(100)
# logger.info(list_of_data)
# logger.info(new_data)


# new_data = list_of_data
# new_data = list_of_data.copy()  #####shallow copy
list_of_data = [1234,234, 456,43, ["xx", "yy"]]
new_data = copy.deepcopy(list_of_data)   ###deep copy
new_data.append(100)
logger.info(list_of_data)
logger.info(new_data)
new_data[4].remove("yy")
logger.info(list_of_data)
logger.info(new_data)
