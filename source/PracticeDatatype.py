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
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)


# F1list = [12]
# print(F1list [0])
# print(type(F1list[0]))
# a=(120)
# print(type(a))
# name=("xyz",)
# print(type(name))
#
# a = {1, 2, 2, 3, 5, 6}
# print(type(a))
# print(a)
#
# b= [1, 2 ,2, 3, 3, 6]
# print(type(b))
# print(b)
#
# c= ["xyz", "abc", "a", "d"]
# print(type(c))

# message = "welcome to python"
# logger.info(message.split())
# logger.info(message.split(maxsplit=1))
# ip_address = "127.0.0.1"
# list_of_octal = ip_address.split(".")
# logger.info(list_of_octal)
# logger.info(ip_address.split(maxsplit=1))
# logger.info(ip_address.rsplit(maxsplit=1))
#
# logger.info(ip_address.split(sep='.',maxsplit=1))
# logger.info(ip_address.rsplit(sep='.',maxsplit=1))


file_name = "test.py"
logger.info(file_name.split("."))
logger.info(file_name.split(".")[0])



# logger.info(file_name.strip(".py"))
# logger.info(dir(str))  \
logger.info(help(str.find))
# logger.info(dir(list))
message1 = "000hello world 0000"
logger.info(message1.strip('0'))
logger.info(message1.lstrip('0'))
logger.info(message1.rstrip('0'))

logger.info(file_name.find(".py"))
logger.info(file_name.find(".txt"))
logger.info(file_name.index(".py"))
# logger.info(file_name.index(".txt"))

#output = IPv4 Address. .  192.168.0.2


