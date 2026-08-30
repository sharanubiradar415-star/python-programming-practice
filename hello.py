arr=[10,20,10,30,40,20,50]

target=20
last_index=-1

for i in range(len(arr)):
    if arr[i]==target:
        last_index=i

print("Last occurence at index",last_index)