
def FrequentNumber(arr, n):
    Hash = dict()
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1
        else:
            Hash[arr[i]] = 1
    max_count = 0
    res = -1

    for i in Hash:
        if (max_count < Hash[i]):
            res = i
            max_count = Hash[i]
         
    return res
 
arr = [ 2,4,4,5,2,3,3,4,5,6,6,6,1]
n = len(arr)
print(FrequentNumber(arr, n))


