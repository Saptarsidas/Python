arr= [10,5,2,4,7,9,55,4,66,]
n=len(arr)
for i in range (n-1):
        for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                        temp=arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
print("sorted list",arr)