""" To practise netsted data type"""

# I want to collect list of student information in whichever the order they registered , it's not fixed
# list of dict
# Adding marks for math, science, language to each student
# I need to get each subject mark by it's subject name, How you can modify the existing data type?

class_information = [
    {"name":"xyz",
     "dob":"13/07/2017"},
    {"name":"yz",
     "dob":"12/05/2017"}
]

print(type(class_information))
print(class_information[0]["name"])


# print(class_information)
# # for var in iterable_object/Collection:
#
# for student in class_information:
#     print("student:%s"%student)

# count = 0
# for student in class_information:
#     if student["name"] == "yz":
#         class_information[count]["db"] = "13/06/2017"
#
#     count +=1

#print(class_information)
# class_information[1]['dob'] = "13/06/2017"
#
# student2 = class_information[1]
# print(type(student2))
# print(student2['name'],student2['dob'])
# print(class_information)
#

#

#stream_data = ("a", "b", "c, a")
# arr1 = [1,2]
# arr2 = [3,4]
# print(arr1)
# print(arr2)
# arr = arr1 + arr2
# print(arr)
# arr2.extend([1,2])
# arr2.append(arr1)
# print(arr2)

stream_data = ("abcdeaa")
datalist = []
count = 0
for character in stream_data:
    data = character[count]
    print(character[count])
    datalist.append(data)
    print(datalist)

count +=1

aList = [123, 'xyz', 'zara', 'abc', 123]
print("Count for 123 : ", aList.count(123))



x= len(datalist)
print(x)
d = {}
index = 0            # Python's indexing starts at zero
for item in datalist:   # Python's for loops are a "for each" loop
    print(index, item)
    d[index] = {}
    d[index]["key"] = item
    d[index]["value"] = datalist.count(item)


    #d[index]["position"] = datalist.index(item)
    #d["index"] = d
    #print(d[index])
    #d.update(d[index])
    # repeated_item_pos= []
    # repeated_item_pos_index =  datalist.index(item)
    # repeated_item_pos.append(repeated_item_pos_index)
    # print(repeated_item_pos)

    print("d :", d)
    index += 1


m = [d]
print("m :", m)

b = m[0]
print(b)



i = 0
for i in b:
   print(i)
   b[i]['pos'] = i
   print("b :", b)

   i += 1




#d = dict()


#d[index] = {}

##d[1].update(d2)


# d = {{},{}}
#

# #
# d[index]["key"]= item
# d[index]["value"]= datalist.count(item)
# d[index]["position"]= datalist.index(item)
#
# d.update(d)
# print(d)


#
# # d["key"]= datalist[index]
# # d["value"]= datalist.count(datalist[index])
# # d["position"]= datalist.index(datalist[index])
#

# #d.append(d)
#
# #print(d[index])
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [123, 234, 456]
# d = {'a': [], 'b': []}
# d['a'].append(list1)
# d['a'].append(list2)
# print(d['a'])
#
# d1 = {"key" : "a", "value": 3, "pos": 6 }
# d2 = {"key" : "b", "value": 1, "pos": 1 }
# d = {0: {}, 1: {}}
# d[0].update(d1)
# d[1].update(d2)
# print(d)


# #print(datalist[count])
# for data in datalist:
#
#     print(data)
#
#
# d[count]["key"] =  data
# d[count]["value"] = datalist.count(data)
# #datalist[count]["position"] = datalist.index(data)
#
# print(d[count])
# count +=1

# class_information[0]["marks"] = [60, 70, 80]
# class_information[1]["marks"] = [70,80, 100]
#
# print(class_information)
# #
# # class_information[0]["marks"]["math']  #
#
# class_information[0]["marks"] = {
#     "math":60,
#     "science":70,
#     "language":80
# }
#
# class_information[1]["marks"] = {
#     "math":70,
#     "science":80,
#     "language":90
# }
#
# print(class_information)
#
# class_information[0]["marks"]["science"]=80
# print(class_information)



# d1 = dict()
# d1["key"] = 1
#
# d2 = dict()
# d2["key"] = 2
#
# d3 = d1.update(d2)
# print(d1)
# print(d2)
# print(d3)



    # d(m)={d["key"]= datalist[m],
    #  d["value"]= datalist.count(datalist[m]),
    #  d["position"]= datalist.index(datalist[m])}










#print(stream_data)


# stream_data[0]["data"]= {
#                     "value":"a",
#                     "index":0
#                        }
#
# count = 0
# for letter in stream_data:
# stream_data[count]["detail"] = {
#
#                "value":"[letter[count]]",
#                "count":1,
#                 "index":"count"
#
# }
# count +=1
# print(stream_data)

# stream_data[1]["data"] = {
#
#                   "value":"b",
#                   "index":1
# }
# print(type(stream_data))
# print(stream_data)



        #class_information[count]["db"] = "13/06/2017"




