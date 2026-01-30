arr=[1,9,2,8,3,7,4,6,5,10,0]

def Divide_Arr(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=Divide_Arr(arr[:mid])
    right_half=Divide_Arr(arr[mid:])

    return Merge(left_half,right_half)

def Merge(left_half,right_half):
    i=0
    j=0
    sortedArr=[]
    while i<len(left_half) and j<len(right_half):
        if left_half[i]<right_half[j]:
            sortedArr.append(left_half[i])
            i=i+1
        else:
            sortedArr.append(right_half[j])
            j=j+1

    print(sortedArr)
    sortedArr.extend(left_half[i:])
    sortedArr.extend(right_half[j:])        
        
    return sortedArr
