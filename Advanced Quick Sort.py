arr=[0,10,1,9,2,8,3,7,4,6,5]
High=len(arr)-1
Low=0

def Partition_Logic(arr,Low,High):
    pivot=arr[High]    
    i=Low-1
    print(f"\n--- New Partition Range: {arr[Low:High+1]} (Pivot: {pivot}) ---")

    for j in range(Low,High):
        if arr[j]<=pivot:
            i+=1
            print(f"Swap: arr[{j}]({arr[j]}) with arr[{i}]({arr[i]})")
            arr[i],arr[j]=arr[j],arr[i]            
            print(f"Current state: {arr}")
        else:
            # Show when the inspector sees a big number and does nothing
            print(f"Skip: {arr[j]} is larger than {pivot}")
            
    print(f"Final Swap: Pivot {pivot} moves to index {i+1}")
    arr[i+1],arr[High]=arr[High],arr[i+1]
    print(f"Partition Result: {arr}")
    return i+1

def Quick_Sort(arr,Low,High):
    if Low<High:
        pi=Partition_Logic(arr,Low,High)

        Quick_Sort(arr,Low,pi-1)
        Quick_Sort(arr,pi+1,High)


Quick_Sort(arr,Low, High)
print("Fully Sorted Shelf:", arr)
            
