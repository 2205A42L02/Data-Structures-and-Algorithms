def merge_sort(arr):
    if len(arr)>1:
        #Divide the array into two halfes
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        #recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)
        
        #merge the sorted halfes
        merge(arr,left_half,right_half)
        
def merge(arr,left,right):
    i=j=k=0
    #compare and merge the elements from left and right halfes
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
#if there are any remaining elements in left or right halfes,add them to the merged array
while i<len(left):
    arr[k]=left[i]
    i+=1
    k+=1
    
while j<len(right):
    arr[k]=right[j]
    j+=1
    k+=1
   
#Example usage:
my_list=[64,34,25,12,22,11,90]

print("original list:",my_list)
merge_sort(my_list)
print("sorted list:",my_list)