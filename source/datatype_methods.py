
"""To Practise data types methods"""
# dir help

import logging
import comments

# create logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler("python_training.log")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)

# logger.debug(dir("python"))
# logger.debug(dir(str))
logger.info(dir(comments))
logger.info(help(comments))

# logger.debug(help(str.join))


logger.debug("welcome to python".capitalize())
logger.debug("python".istitle())
logger.debug("python".islower())
logger.debug("The converted message %s","welcome to python".title())

logger.debug("python".isalpha())

user_input = "123s"
logger.debug(user_input.isdecimal())

logger.debug("123".isdecimal())

logger.debug(user_input.isalnum())

logger.debug("python".isspace())
logger.debug("\n".isspace())
logger.debug("\t".isspace())
logger.debug(" ".isspace())

up_var = "python".upper()
low_var = up_var.lower()
logger.debug(up_var.isupper())
logger.debug(low_var.islower())


logger.debug("python".swapcase())
logger.debug("Python".swapcase())

logger.debug("python".endswith("hon"))
logger.debug("python".startswith("pyt"))

logger.debug(help(dir("python")))








"""To Practise data types methods"""
# dir help

import logging
import comments
import subprocess

# create logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler("python_training.log")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)

# logger.debug(dir("python"))
# logger.debug(dir(str))

# logger.debug(help(str.join))


logger.debug("welcome to python".capitalize())
logger.debug("python".istitle())
logger.debug("python".islower())
logger.debug("The converted message %s","welcome to python".title())

logger.debug("python".isalpha())

user_input = "123s"
logger.debug(user_input.isdecimal())

logger.debug("123".isdecimal())

logger.debug(user_input.isalnum())

logger.debug("python".isspace())
logger.debug("\n".isspace())
logger.debug("\t".isspace())
logger.debug(" ".isspace())

up_var = "python".upper()
low_var = up_var.lower()
logger.debug(up_var.isupper())
logger.debug(low_var.islower())


logger.debug("python".swapcase())
logger.debug("Python".swapcase())

logger.debug("python".endswith("hon"))
logger.debug("python".startswith("pyt"))


## split, splitlines, rsplit, strip, lstrip, rstrip, join, find,rfind, index,rindex, replace
logger.info(dir(str))
# logger.info(dir(comments))
# # logger.info(help(comments))
# logger.info(help(comments.get_db_conn))
#logger.info(help(str.split))

message = "welcome to python"
logger.info(message.split())
logger.info(message.split(maxsplit=1))
ip_address = "127.0.0.1"
list_of_octal = ip_address.split(".")
logger.info(list_of_octal)
file_name = "test.py"
logger.info(file_name.split("."))
logger.info(file_name.split(".")[0])

logger.info(message.rsplit(maxsplit=1))






# output = subprocess.getoutput("dir")
#
# for line in output.splitlines():
#     # print(line)
#     if line.find(".py")!=-1:
#         print(line)