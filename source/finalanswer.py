stream_data = ("abcdeaa")
datalist = []
count = 0
for character in stream_data:
    data = character[count]
    print(character[count])
    datalist.append(data)
    print(datalist)

count +=1

d = {}
index = 0            # Python's indexing starts at zero
for item in datalist:   # Python's for loops are a "for each" loop
    print(index, item)
    d[index] = {}
    d[index]["key"] = item
    d[index]["value"] = datalist.count(item)

    print("d :", d)
    index += 1


# m = [d]
# print("m :", m)

# b = d
# print(b)


print(type(d))
i = 0
for i in d:
   print(i)
   d[i]['pos'] = i
   print("d :", d)

   i += 1