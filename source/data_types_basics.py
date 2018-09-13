""" This module is to practise data types"""
# to comment out use ctrl+ /
# name = "python"
# # print(name)
# print(name[0])
# print(name[-1])
#
#
# a = 20
# print(a)
# print(type(a))
# b = a
# print(b)
# print(type(b))
#
# print(id(a), id(b))
# print(a is b)
#
# print("====== Changing the object for b ======")
# b = "python"
# print(a)
# print(b)
# print(type(b))
# print(id(a), id(b))
# print(a is b)

# ================== Sequential data type ==================== #
# name = "python example"
# print(name)      # "python example"
# print(name[1])   # y
# print(name[2])   # t
# print(name[1], name[-5])  # y, a
# print(name[4], name[-2])  # o, l
# print("emptyCharacter:%s")
# print(name[6])
# print(name[7])
#print(name[7])
# ===================Immutable Modification and deletion data not supported ============= #
# name[1] = 'e'
# del name[0]
# del name
# print(name)

#======================= Mutable Modification and deletion data in Object ============ #
# list_of_accounts = [ 12345, 34556, 56789 ]
# print(list_of_accounts)
# print(list_of_accounts[0])
#
# list_of_accounts[0] = 23456
# print(list_of_accounts[0])
# print(list_of_accounts)
# del list_of_accounts[0]
# print(list_of_accounts)
#
# list_of_accounts_tuple = ( 12345, 34556, 56789 )
# print(list_of_accounts_tuple)

# a = 1
# print(type(a))
# a= (1)
# print(type(a))
# a = (1,)  #define tuple 1 value with ,
# print(type(a))

# ==================== Unordered data =============================== #
#dict, set, frozenset

# dict1 = {} #this is dict,keys have some values.empty curly braces
# set1 = {"kohli" , "dhawan" , "kohli"}  #set will hold only keys , not values fr the key
# set1 = {}
# print(type(set1))
# print(set1)
# fz = frozenset ([1, 2, 3, 4, 1, 3, 45, "XX", "XX"])
# print(type(fz))
# print(fz)
# for i in range (len(fz)):
#     print(i)
#
# set1 = {1,2,3,4,5,6,7,7,6}
# #print(set1)
# print(list(set1))


#
# dict1 = {
#     "kholi": 100,
#     "dhwan": 102,
#     "dhoni": 105
# }
#
#
# for keys,value in dict1.items():
#     list = []
#     k=keys
#     v=value
#     list.append(k)
#     list.append(v)
#     print(list[0])
#     print(list[1])
#
# #
# print(list)




# score_data = {"kohli": 199,
#               "dhawan": 99,
#               "dhoni": 49}
# x = [score_data]
# print(x)

# list1 = [ashok, dhruv, anushree]
# value1 = [1, 2, 3]

previous_data={'p1','p2','p3','p4'}
current_data={'p7','p2'}
print(previous_data)
previous_data.difference_update(current_data)
print(current_data)
print(previous_data)



#list_of_account = [(name1= {"sbi_account": 1234,"icic_account":2245}), (name2= {"sbi_account:"5678, "icic_account":7654})]

#list_of_account = [{"sbi_account": 1234,"icic_account":2245},{"sbi_account:"5678, "icic_account":7654}]

# print(score_data)
#print(score_data [0])
# print(score_data["kohli"])
# del score_data["kohli"]
# print(score_data)
