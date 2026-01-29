UsortedArray=[1,9,2,8,3,7,4,6,5,10,0]
print('Original Array :-',UsortedArray)

NoOfElementsInArr=len(UsortedArray)

for i in range(1,NoOfElementsInArr):
    for j in range(i,0,-1):
        if UsortedArray[j]<UsortedArray[j-1]:
            UsortedArray[j],UsortedArray[j-1]=UsortedArray[j-1],UsortedArray[j]
            #print(str(UsortedArray[j]),str(UsortedArray[j-1])+" - "+str(UsortedArray[j-1]),str(UsortedArray[j]))

print('Original Array After Sorting:-',UsortedArray)

