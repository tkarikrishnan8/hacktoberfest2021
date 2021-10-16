def findMajority(arr, size): 
    m = {} 
    for i in range(size): 
        if arr[i] in m: 
            m[arr[i]] += 1
        else: 
            m[arr[i]] = 1
    count = 0
    for key in m: 
        if m[key] > size / 10: 
            count = 1
            print("Majority element is ", key) 
            break
    if(count == 0): 
        print("Majority element does not exist") 
  
# Driver code  
arr = [1,3,4,4,1,4,4]  
n = len(arr) 
  
# Function calling  
findMajority(arr, n) 