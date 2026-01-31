def Quick_Sort(arr):
    if len(arr)<=1:
        return arr
    mid=arr[len(arr)//2]
    Left=[x for x in arr if x<mid]
    MidVal=[x for x in arr if x==mid]
    Right=[x for x in arr if x>mid]
    print(Left,MidVal,Right)
    print(Quick_Sort(Left),MidVal,Quick_Sort(Right))

    return Quick_Sort(Left)+MidVal+Quick_Sort(Right)



