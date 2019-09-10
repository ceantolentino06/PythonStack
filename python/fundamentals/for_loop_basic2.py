# 1. BIGGIE SIZE
def biggieSize(arr):
    for i in range(len(arr)):
        if(arr[i]>0):
            arr[i]='big'
    return arr
print(biggieSize([-1,2,5,-4]))

# 2. COUNT POSITIVES
def countPositives(arr):
    count = 0
    for i in arr:
        if i>0:
            count+=1
    arr[len(arr)-1]=count
    return arr
print(countPositives([-1,1,1,1]))

# 3. SUM TOTAL
def sum(arr):
    total = 0
    for i in arr:
        total+=i
    return total
print(sum([1,2,3,4]))

# 4.  AVERAGE
def average(arr):
    total = 0
    for i in arr:
        total+=i
    return total/len(arr)
print(average([1,2,3,4]))

# 5. LENGTH
def length(arr):
    return len(arr)
print(length([1,2,3,4,5]))

# 6. MINIMUM
def minimum(arr):
    if len(arr)==0:
        return false
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min
print(minimum([37,2,1,-9]))

# 7. MAXIMUM 
def maximum(arr):
    if len(arr)==0:
        return false
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max
print(maximum([37,2,1,-9]))

# 8. ULTIMATE ANALYSIS
def analysis(arr):
    dictionary = {'sumtotal': 0, 'average': 0, 'minimum': 0, 'maximum': 0, 'length': len(arr)}
    min = arr[0]
    max = arr[0]
    total = 0
    for i in arr:
        if i > dictionary['maximum']:
            dictionary['maximum'] = i
        if i < dictionary['minimum']:
            dictionary['minimum'] = i
        dictionary['sumtotal']+=i
    dictionary['average']=dictionary['sumtotal']/dictionary['length']
    return dictionary
print(analysis([37,2,1,-9]))

# 9. REVERSE LIST
def reverse(arr):
    for i in range(int(len(arr)/2)):
        temp = arr[i]
        arr[i]=arr[(len(arr)-1)-i]
        arr[(len(arr)-1)-i]=temp
    return arr
print(reverse([1,2,3,4,5,6]))