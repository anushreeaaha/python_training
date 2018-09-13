""" To Practise Type casting operation"""
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
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# create formatter
formatter = logging.Formatter("%(asctime)s- %(levelname)s - %(filename)s-%(lineno)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)


logger.info(dir(str))
#logger.info(dir(comments))

# output = subprocess.getoutput("dir")
# logger.info(output)

#output = subprocess.getoutput("ipconfig")
#logger.info(output)

# for line in output.split("\n"):
#      #logger.info(line)
#      if line.find("IPv4 Address")!= -1:
#           logger.info(line)
#           logger.info(type(line))
#           logger.info(line.split(":")[1])
#           logger.info(line.strip(". "))






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

# class_information = [
#     {"name":"xyz",
#      "dob":"13/07/2017"},
#     {"name":"yz",
#      "dob":"12/05/2017"}
# ]
#
# new_tuple = tuple(class_information)
# logger.debug(type(new_tuple))
# logger.debug(new_tuple)

# list(1)


# logger.debug("2nd Class information :"+ str(class_information))
# debug_message= "2nd class information:%s"%(class_information)
# debug_message2 = "2nd class information:a {b}".format(a=10, b=20)
# debug_message3 = "{cls}nd class information".format(cls=2)
# debug_message4 = "{class_id} information".format(class_id="2nd")
# debug_message5 = "{} information {}".format("2nd",class_information)
# logger.debug(debug_message)
# logger.debug(debug_message2)
# logger.debug(debug_message3)
# logger.debug(debug_message4)
# logger.debug(debug_message5)
# logger.debug(debug_message2)
#
#
# message = "python"
# logger.info(message)
# logger.info(list(message))  # list(iterable) tuple(iterable) set(iterable) frozenset(iterable)

# {1:"xx", 2:"yy"}

# logger.info(list(class_information[0]))
#
# d = dict(name="xyz",dob="13/07/2017")
# logger.info(d)
#
# d1 = dict(zip(("name","dob"),("xyz","13/07/2017")))
# logger.info(d1)
#
#
# logger.info(dir(str))
# #logger.info(dir(comments))

# message = "welcome to python"
# logger.info(message.split())
# logger.info(message.split(maxsplit=1))
# ip_address = "127.0.0.1"
# list_of_octal = ip_address.split(".")
# logger.info(list_of_octal)
# file_name = "test.py"
# logger.info(file_name.split("."))
# logger.info(file_name.split(".")[0])
#
# logger.info(ip_address.split(maxsplit=1))
# logger.info(ip_address.rsplit(maxsplit=1))
#
# logger.info(ip_address.split(sep='.',maxsplit=1))
# logger.info(ip_address.rsplit(sep='.',maxsplit=1))
#
# logger.info(file_name.strip("py."))
# message1 = "000hello world 0000"
# logger.info(message1.strip('0'))
# logger.info(message1.lstrip('0'))
# logger.info(message1.rstrip('0'))
#
#
# logger.info(file_name.find(".py"))
# logger.info(file_name.find(".txt"))
# logger.info(file_name.index(".py"))
#logger.info(file_name.index(".txt"))

# logger.info(ip_address.find("."))
# logger.info(ip_address.rfind("."))
# logger.info(ip_address.index("."))
# logger.info(ip_address.rindex("."))
#
#
# different_message = ["Welcome to python", "Welcome to Java","Welcome to scala"]
# # slicing with rfind
# for message in different_message:
#    logger.info(message)
# #logger.info(message[message.rfind(" "):])
#
# #logger.info(different_message[0].rfind(" "))
#
# message5 = "Hello this is Network message \n from Ip address 127.0.0.1"
# logger.info(message5.splitlines())
# logger.info(message5.splitlines())
# logger.info(message5)
#
# output = subprocess.getoutput("dir")
# logger.info(output)
# logger.info(output.splitlines())
#
# logger.info("{form} Finding python files {form}".format(form="="*12))
# for line in output.splitlines():
#     # print(line)
#    if line.find(".py")!=-1:
#     logger.info(line)
#
# help(str.join)
#
# ip_addr = "127.0.0.1"
# list_of_octal = ip_addr.split(".")
# logger.info(list_of_octal)
# list_of_octal[0] = "10"
# logger.info(list_of_octal)
# logger.info(".".join(list_of_octal))
#
# # Find your machine ip address using subprocess module. ipconfig .. ifconfig
# # subprocess
#
# output1 = subprocess.getoutput("ipconfig")
# logger.info(output1)
#
# ip_addr = "127.0.0.1"
# # list_of_octal = ip_addr.split(".")
# # logger.info(list_of_octal)
# new_ip_addr =ip_addr.replace("127","10")
# # logger.info(list_of_octal)
# # logger.info(".".join(list_of_octal))
# #logger.info(new_ip_addr, ip_addr)
#
#
# logger.info(new_ip_addr)
# logger.info("NewIP address: {new_ip} OldIp address:{old_ip}".format(new_ip=new_ip_addr,old_ip=ip_addr))
#
# logger.info(ip_addr.replace(".",":", 3))
# logger.info(ip_addr.replace(".",":", 1))
#
# #logger.info(dir(str))
#
# logger.info(ip_addr.replace(".",":",ip_addr.count(".")))
# logger.info(ip_addr.ljust(20,"x"))
# logger.info(ip_addr.rjust(20,'x'))
# logger.info(ip_addr.center(20,'x'))
# logger.info(ip_addr.zfill(20))
#
# logger.info(ip_addr.center(20))
#
#
# ##############################tuple####################
# #logger.info(dir(tuple))
# logger.info(help(tuple.count))
#
#list_of_names = ("xyz", "yz", "zz","xyz", "mm", 12, 234)
# logger.info(list_of_names.count("xyz"))
# logger.info(list_of_names.count("xz"))
#
# #logger.info(help(tuple.index))
# logger.info(list_of_names.index("mm"))
# #logger.info(list_of_names.index("mm",0,2))
#
# # logger.info(list_of_names.index('2345'))
# logger.info(list_of_names.index("mm",0,5))
#
# #############################list#####################################
# #logger.info(dir(list))
#
list_of_names = ("xyz", "yz", "zz","xyz", "mm", 12, 234)
list_of_data = []
logger.info((list_of_data))
list_of_data.append(12)
logger.info((list_of_data))

list_of_data.append(list_of_names)
logger.info(list_of_data)
logger.info(list_of_data[1])

list_of_data.append("Hello world")
logger.info((list_of_data))
logger.info(list_of_data[-1].split())
logger.info(list_of_data[-1].split()[1])

logger.info(list_of_data[-1]) # "Hello world"[list_of_data[-1].rfind(" "):]
# logger.info(list_of_data[-1].split())
# logger.info(list_of_data[-1].split()[1])
#
dict1 = {"lang1":"python",
         "lang2":"java"}


list_of_data.append(dict1)
logger.info(list_of_data)
logger.info(list_of_data[3]["lang1"])
# #pprint.pprint(list_of_data)
logger.info(list_of_data[3]["lang1"][-1])

list_of_data.insert(0, 2000)  #for insert you have to mention the index no where to add the data
logger.info(list_of_data)
# pprint.pprint(list_of_data)
# pprint.pprint(list_of_data[2])

list_of_data.insert(2, "New Data")
# pprint.pprint(list_of_data)
logger.info(list_of_data)


new_list_data = ["network1","network2","network3"]
list_of_data.append(new_list_data)
logger.info(list_of_data)

list_of_data.pop(-1)
logger.info(list_of_data)
# new_modify = list_of_data + new_list_data
# logger.info(new_modify)
# logger.info(list_of_data)

new_modify = list_of_data + new_list_data # O(n) + O(k)  # O(K)
logger.info(new_modify)
logger.info(list_of_data)

list_of_data.extend(new_list_data) # O(K), here each obhect in list is added as individual object, not as a nested list
logger.info(list_of_data)


list_of_data.clear()
logger.info(list_of_data)

list_of_data.extend(dict1)
logger.info(list_of_data)

list_of_data.remove('lang1')
list_of_data.remove('lang2')
logger.info(list_of_data)

list_of_data.append(dict1)
logger.info(list_of_data)

list_of_data.pop()
logger.info(list_of_data)
list_of_data.extend(dict1)
logger.info(list_of_data)
list_of_data.pop(0) # pop() or pop(-1 or len(list)-1) pop will remove last index if parenthysis does mot mwntion the index no to remove
logger.info(list_of_data)

list_of_data.clear()
logger.info(list_of_data)

list_of_data.extend(dict1)
logger.info(list_of_data)
logger.info(list_of_data.index("lang1"))
logger.info(list_of_data.index("lang2"))
list_of_data.remove("lang1") #remove needs the item to remove ,
logger.info(list_of_data)
list_of_data.remove("lang2") #remove needs the item to remove ,
logger.info(list_of_data)

list_of_data.append(dict1)
logger.info(list_of_data)
list_of_data.remove(dict1)
logger.info(list_of_data)

#
logger.info(list_of_data.count('lang1'))
logger.info(list_of_data.count(2000))

# new_list = [20,2,4, 70,9, 12,5]
# new_list.sort() # without reverse , sorted in ascending order else decending order
# logger.info(new_list)
#
# new_data = ["xx", "yy", "ab", "dn"] # x y a d  # a d x y # y x d a # yy xx dn ab
# new_data.sort(reverse=True)
# logger.info(new_data)
#
#
# new_data.sort() # x y a d  # a d x y # ab dn xx yy
# logger.info(new_data)
# new_data.sort(key=lambda item: item[1])  #x y b n #b n x y #ab dn xx yy
# logger.info(new_data)
#
# list_of_emails = ["xa@gmail.com", "ac@yahoo.com","zb@gmail.com"]
# list_of_emails.sort() # ac@yahoo.co, xa@gmail.com zb@gmail.com
# logger.info(list_of_emails)
# list_of_emails.sort(key=lambda item:item[0])
# logger.info(list_of_emails)
#
# list_of_emails.sort(key=lambda item: item[1]) #  [ 'a', 'c', 'b']  #
# logger.info(list_of_emails) # xa@gmail.com zb@gmail.com ac@yahoo.com

# def key_to_compare(item):
#     return item[1]
#
# list_of_emails.sort(key=key_to_compare)
# logger.info(list_of_emails)
#
# list_of_machines = ["10.2.0.5", "10.2.0.3", "10.3.0.1"]
# # sort it with host address . last digit
# list_of_machines.sort(key=lambda item: item[-1])
# logger.info(list_of_machines)
#
# # 24
# list_of_machines = ["10.2.0.5/24", "10.2.0.3/24", "10.3.0.1/24"]
# # sort it with host address . last digit
# list_of_machines.sort(key=lambda item: item.strip("/24")[-1])
# logger.info(list_of_machines)
#
#
# list_of_employees = [
#             {"emp_id":34,
#              "emp_name":"xx ab"},
#            {"emp_id":2,
#             "emp_name":"yy ca"},
#            {"emp_id":1,
#             "emp_name":"zz dc"}
#                   ]
#
# list_of_employees.sort(key=lambda item: item["emp_id"])
# #list_of_employees.sort(key=lambda item: item[emp_id])
# logger.info(list_of_employees)
#
# # for item in list_of_employees:
# #     item_consider = item
# #
# list_of_employees.sort(key=lambda item: item["emp_name"].split())
# logger.info(list_of_employees)
#


# sort:
#     for item in list_of_employees:
#         key_to_compare(item)




# list_of_employees

# list_of_employees.sort(key=lambda emp_data: emp_data['emp_id'])
#
#
#
# def key_to_compare_dict(item):
#     logger.info(item)
#     return item['emp_id']
#     logger.info(item["item_id"])
#
# list_of_employees.sort(key=key_to_compare_dict)
# logger.info(list_of_employees)

######################reverse######################

list_of_numbers = [23, 1, 45, 6, 7]
logger.info(list_of_numbers[::-1]) # [7, 6, 45, 1, 23]
logger.info(list_of_numbers)  # [23, 1, 45, 6, 7]    
list_of_numbers.reverse()     # [7, 6, 45, 1, 23]      
logger.info(list_of_numbers)

######################dict_datatype methods#######################
#logger.info(dir(dict))  #####'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

list_of_keys =["emp_name","emp_id"]
emp_data = dict.fromkeys(list_of_keys, None)
#emp_data = dict.fromkeys(list_of_keys, 2)
logger.info(emp_data)
#help(dict.fromkeys)



logger.info(emp_data["emp_name"]) # value using key
# logger.info(emp_data["emp_address"])
logger.info(emp_data.get("emp_name"))
logger.info(emp_data.get("emp_address", "No Key Found"))
help(emp_data.get)

logger.info(emp_data["emp_name"]) # value using key
# logger.info(emp_data["emp_address"])
logger.info(emp_data.get("emp_name"))
logger.info(emp_data.get("emp_address", "No Key Found"))
#help(emp_data.get)

emp_data["emp_name"] = "xx"
logger.info(emp_data["emp_name"])
logger.info(emp_data.setdefault("emp_name")) # emp_data.get("emp_name")
logger.info(emp_data.setdefault("emp_address","12/A, India"))
logger.info(emp_data.get("emp_address"))

# dict.keys() -> [key1, key2,...]
# dict.values() -> [ value1, value2,... ]
# dict.items() -> [ (key1, value1), (key2, value2) ...]
logger.info(emp_data.keys())
logger.info(emp_data.values())
logger.info(emp_data.items())

logger.info(emp_data.setdefault("emp_id", "12"))   ##set default only applicable for keys do not exist in dict
logger.info(emp_data)

emp_data["emp_id"] = 12341
logger.info(emp_data.items())

new_data = {"emp_name":"new_xx", "emp_id":1234, "emp_dob":"12/05/1990"}
emp_data.update(new_data)
logger.info(emp_data)

logger.info(emp_data.pop("emp_id"))    ####value of removed key
logger.info(emp_data)

logger.info(emp_data)
logger.info(emp_data.popitem()) # (key, value)
# help(emp_data.popitem)
logger.info(emp_data)
emp_data.clear()
logger.info(emp_data)


###########################set###############################

##add', 'clear', 'copy', 'difference', '
# difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset',
# 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

logger.info(dir(set))
data_set = set()
logger.info(data_set)
data_set.add(123)
data_set.add(243)
logger.info(data_set)
new_data_set = {23, 124, 123, 24, 'k'}
data_set.update(new_data_set)
logger.info(data_set)

logger.info(data_set.difference(new_data_set)) # data_set - new_data_set
logger.info(data_set.intersection(new_data_set)) # data_set matches in new_data_set
logger.info(data_set.union(new_data_set))        # data_set + new_data_set
logger.info(data_set.symmetric_difference(new_data_set))
#  data_section (not in intersection) + new_data_set (not in intersection) =


################################################11thSept_data_set############################################################
logger.info(dir(set))
data_set = set()
logger.info(data_set)
data_set.add(123)
data_set.add(243)
logger.info(data_set)
new_data_set = {23, 124, 123, 24}
# data_set.update(new_data_set)     # data_set = data_set + new_data_set
logger.info(data_set)
logger.info(data_set.difference(new_data_set)) # data_set - new_data_set
logger.info(new_data_set.difference(data_set))
logger.info(data_set.intersection(new_data_set)) # data_set matches in new_data_set
logger.info(data_set.union(new_data_set))        # data_set + new_data_set
logger.info(data_set.symmetric_difference(new_data_set))
logger.info(new_data_set.symmetric_difference(data_set))
data_set.intersection_update(new_data_set)
logger.info(data_set)



# data_set- new_data_set + (new_data_set - data-set)
#  data_section (not in intersection) + new_data_set (not in intersection) =
#
# data_set.update(new_data_set)
# logger.info(data_set)
# data_set.difference_update(new_data_set)  # data_set = data_set - new_data_set
# logger.info(data_set)
# data_set.intersection_update(new_data_set)  # data_set = intersection (data_set and new_data_set)
# logger.info(data_set)
# # data_set = Union(dataset and new_data_set) - Intersection(dataset and new_data_set)
# data_set.symmetric_difference_update(new_data_set)
#
# logger.info(data_set)
# #
# logger.info(data_set.issubset(new_data_set))
# logger.info(data_set.issuperset(new_data_set))
# logger.info(data_set.isdisjoint(new_data_set))
# #

logger.info({1,2,3}.issubset({1,2,3,4}))
logger.info({1,2,3,4}.issuperset({1,2,3}))
logger.info({30,40,60}.isdisjoint({1,2,3}))
# #
# set1 = {1, 2,3}
# set2 = {4, 5, 6}
# logger.info(set1.isdisjoint(set2))


logger.info({1,2,3}.issubset({1,2,3,4}))
logger.info({1,2,3,4}.issuperset({1,2,3}))
logger.info({30,40,60}.isdisjoint({1,2,3}))

logger.info({1,2,3}.issubset({1,2,3,4}))
logger.info({1,2,3,4}.issuperset({1,2,3}))
logger.info({30,40,60}.isdisjoint({1,2,3}))
# #
# set1 = {1, 2,3}
# set2 = {4, 5, 6}
# logger.info(set1.isdisjoint(set2))
#
# {123, 243}
logger.info(data_set.pop()) # retuns data
#help(data_set.pop)
# logger.info(data_set.remove(124))
#help(data_set.remove)
logger.info(data_set)
logger.info(data_set.discard(124))



############################frozenset###################################
logger.info(dir(frozenset))
fz = frozenset("python")
logger.info(fz)
fz = frozenset([1,2,3, 4,5,2])
logger.info(fz)


####################################################
list_of_data = [1234,234, 456,43, ["xx", "yy"]]
# new_data = list_of_data
new_data = list_of_data.copy()
new_data.append(100)
logger.info(list_of_data)
logger.info(new_data)
new_data[4].remove("yy")
logger.info(list_of_data)
logger.info(new_data)


# output
# 2018-09-11 08:10:34,337- INFO - datatypemethods_class.py-579 - [1234, 234, 456, 43, ['xx', 'yy']]
# 2018-09-11 08:10:34,338- INFO - datatypemethods_class.py-580 - [1234, 234, 456, 43, ['xx', 'yy'], 100]
# 2018-09-11 08:10:34,338- INFO - datatypemethods_class.py-582 - [1234, 234, 456, 43, ['xx']]
# 2018-09-11 08:10:34,338- INFO - datatypemethods_class.py-583 - [1234, 234, 456, 43, ['xx'], 100]
