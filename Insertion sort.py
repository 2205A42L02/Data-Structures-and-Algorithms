def Insertion_sort(arr):
    n=len(arr)
    #Traverse through all elements in the array starting from the second element
    for i in range(1,n):
        key=arr[i]
        
        #move elements of arr[0..i-1] that are greater than key to onw position ahead of their current position
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
#example usage:
my_list=[64,34,25,12,11,90]

print("original list:",my_list)
Insertion_sort(my_list)
print("sorted list:",my_list)