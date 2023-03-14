array=[1,31,2,31,2,"dada",34,69,"a",420,55,55,"dsadas",55,"B",0]
asc_array=[]
desc_array=[]
for i in range(0,len(array)):
    if type(array[i])!=str:
            asc_array.append(array[i])
            desc_array.append(array[i])

for i in range(len(asc_array)):
    for j in range(i + 1, len(asc_array)):
        if asc_array[i] > asc_array[j]:
            asc_array[i], asc_array[j] = asc_array[j], asc_array[i]
        if desc_array[i] < desc_array[j]:
            desc_array[i], desc_array[j] = desc_array[j], desc_array[i]

     
print("Asc order : ",asc_array)
print("desc Order: ",desc_array)
