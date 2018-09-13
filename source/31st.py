""" To Practise Type casting operation"""

import logging

logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug

class_information = [
    { "name":"xyz",
    "dob":"13/07/1989" },
    { "name":"mnp",
     "dob":"12/07/1987" }
                  ]

new_tuple = tuple(class_information)
logger.debug(type(new_tuple))
logger.debug(new_tuple)

# list_of_fruits = ["apple","banana", "orange"]
# input_value = input("Enter some number: ")
# logger.debug(type(input_value))
# logger.debug(input_value)
# int_value = int(input_value)
# logger.debug(type(int_value))
# logger.debug(list_of_fruits[int_value])
#
# #int("2.34")
# logger.debug(int("0o1", base=8))
# logger.debug(int(2.34))
# logger.debug(int(0o1))
#
# # log.debug(help(int))
#
#
# print("The given value is :"+ input_value)
# logger.debug("The given value is :"+ str(int_value))

logger.debug(dir("python"))

new_tuple = tuple(class_information)
logger.debug(type(new_tuple))
logger.debug(new_tuple)

# list(1)


logger.debug("2nd Class information :" + str(class_information))
debug_message = "2nd class information:%s" % (class_information)
debug_message2 = "2nd class information:a {b}".format(a=10, b = 20)
debug_message3 = "{cls}nd class information".format(cls=2)
debug_message4 = "{class_id} information".format(class_id="2nd")
debug_message5 = "{} information {}".format("2nd", class_information)
logger.debug(debug_message)
logger.debug(debug_message2)
logger.debug(debug_message3)
logger.debug(debug_message4)
logger.debug(debug_message5)
logger.debug(debug_message2)

message = "python"
logger.info(message)
logger.info(list(message))




d = dict(name="xyz",dob="13/07/2017")
logger.info(d)


logger.debug("python".capitalize())

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
