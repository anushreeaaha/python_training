# seq= [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
# # result=[idx for idx, item in enumerate(a) if item in a[:idx]]
# # print(result)
#
# def list_duplicates(seq):
#     d = {}
#     for i in seq:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     dups = []
#     for i in d:
#         if d[i] > 1:
#             dups.append(i)
#     lst = []
#     for i in dups:
#         l = []
#         for index in range(len(seq)):
#             if seq[index] == i:
#                 l.append(index)
#         lst.append(l[1:])
#     new = []
#     for i in lst:
#         for index in i:
#             new.append(index)
#     return new

# d = {
#     0: {'key': 'a', 'value': 3},
#     1: {'key': 'b', 'value': 1},
#     2: {'key': 'c', 'value': 1},
#     3: {'key': 'd', 'value': 1},
#     4: {'key': 'e', 'value': 1},
#     5: {'key': 'a', 'value': 3},
#     6: {'key': 'a', 'value': 3}}
# index = 0
# #for key in d:
# d[0]["a"][""]
#
# list = [1, 1, 2]
# i = 0
# b = []
# for item in list:
#     print(item, i)
#     m = item
#
#     if m == 1:
#         a = list.index(m)
#     #b.append(a)
#     print(a)
#     i +=1

m = [
         {'key': 'a', 'value': 3},
         {'key': 'b', 'value': 1},
         {'key': 'c', 'value': 1},
         {'key': 'd', 'value': 1},
         {'key': 'e', 'value': 1},
         {'key': 'a', 'value': 3},
         {'key': 'a', 'value': 3}
     ]


# index = 0
# for index in m:

m = [
      {'name': 'a', 'value': 3},
      {'name': 'b', 'value': 1},
      {'name': 'c', 'value': 1},
      {'name': 'd', 'value': 1},
      {'name': 'e', 'value': 1},
      {'name': 'a', 'value': 3},
      {'name': 'a', 'value': 3}
     ]

print(type(m))
print(m[0]["name"])
# i = 0
# for i in m:
#     print(i)
#     a = m.index(i)
#     print(a)
#     m[a]['pos'] = a
#     print(m)
#
#     a += 1

a = [
     {
    0: {'key': 'a', 'value': 3},
    1: {'key': 'b', 'value': 1},
    2: {'key': 'c', 'value': 1},
    3: {'key': 'd', 'value': 1},
    4: {'key': 'e', 'value': 1},
    5: {'key': 'a', 'value': 3},
    6: {'key': 'a', 'value': 3}
     }
    ]
print(type(a))
print(a[0])
b = a[0]
print(b)



i = 0
for i in b:
   print(i)
   b[i]['pos'] = i
   print(b)

   i += 1




# class_information = [
#     {"name":"xyz",
#      "dob":"13/07/2017"},
#     {"name":"yz",
#      "dob":"12/05/2017"}
# ]
#
# class_information[0]["marks"] = [60, 70, 80]
# class_information[1]["marks"] = [70,80, 100]

#print(class_information)


