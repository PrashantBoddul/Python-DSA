UsortedArray=[1,9,2,8,3,7,4,6,5,10,0]
print('Original Array :-',UsortedArray)

NoOfElementsInArr=len(UsortedArray)

for i in range(NoOfElementsInArr):
    k=i
    for j in range(i+1,NoOfElementsInArr):
        if UsortedArray[j]<UsortedArray[k]:
            k=j
            
    UsortedArray[i],UsortedArray[k]=UsortedArray[k],UsortedArray[i]

print('Original Array After Sorting:-',UsortedArray)


