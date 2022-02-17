import os
import sys

#List files and sizes
file_names = (os.listdir())
file_sizes = []
for i in file_names:
    file_sizes.append(os.stat(i).st_size)
listgeneral = list()
value = 0
while value < len(file_names) :
    listgeneral.append(file_names[value])
    listgeneral.append(file_sizes[value])
    value += 1

# add for delete
all_cluster = set()
value2 = 0
while value2 < len(file_names)-1 :
    for i in file_sizes:
        if file_sizes.count(i) > 1:
            all_cluster.add(i)
    value2 += 1
all_cluster2 = list(all_cluster)

#Duplicate
value3 = 0
value4 = 0
delete_place = []
while value3 < len(all_cluster2):
    while value4 < (listgeneral.count(all_cluster2[value3])-1):
        value4 += 1
        delete_place.append((all_cluster2[value3]))
    if value4 == (listgeneral.count(all_cluster2[value3])-1):
        value4 = 0
    value3 += 1

#ASK
if len(delete_place) < 1:
    print ("There is no duplicate.")
    sys.exit()
else:
    print (len(delete_place) , "files will be delete. Are you sure ?      Y|N")
    eminmisin = input ("")
    if eminmisin == "n" or eminmisin == "N":
        print ("Exit")
        sys.exit()
    else:
        #delete
        for i in delete_place:
            if i in listgeneral:
                os.remove(listgeneral[listgeneral.index(i)-1])
                listgeneral.pop(listgeneral.index(i)-1)
                listgeneral.pop(listgeneral.index(i))
