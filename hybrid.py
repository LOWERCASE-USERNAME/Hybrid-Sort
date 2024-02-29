def hybrid_sort(arr, k):
    if(len(arr) <= k): return insertion_sort(arr)
    else: return merge(hybrid_sort(arr[0 : len(arr)//2], k), hybrid_sort(arr[len(arr)//2 : len(arr)], k))

def insertion_sort(arr):
    for i in range(len(arr)):
        value = arr[i]
        j = i - 1
        #traverse the sub-array which is to the left of the current value and sort it
        while j >= 0 and value < arr[j]:
            #if the previous element is smaller than the current value
            #push that element forward 1 step.
            arr[j + 1] = arr[j]
            #move down 1
            j -= 1
        #end the while loop, find the appropriate index for the value
        #move up 1 to restore the position after the last loop
        j += 1
        arr[j] = value
    return arr
        
def merge(arrLeft, arrRight):
    arr = [None] * (len(arrLeft) + len(arrRight))
    leftIdx = rightIdx = currentIdx = 0

    #Iteratively compare the first element of the two array, and take the smaller one to put it into the new array. This works
    #because if the two arrays are presumably already sorted in the previous recursion
    #This will be done only when the cursor in one of the array or both, has no more left element to traverse 
    while leftIdx < len(arrLeft) and rightIdx < len(arrRight):
        if(arrLeft[leftIdx] <= arrRight[rightIdx]):
            arr[currentIdx] = arrLeft[leftIdx]
            leftIdx += 1
        else:
            arr[currentIdx] = arrRight[rightIdx]
            rightIdx += 1
        currentIdx += 1

    #Put all of the leftover element into the rightmost of the result array
    while leftIdx < len(arrLeft):
        arr[currentIdx] = arrLeft[leftIdx]
        leftIdx += 1
        currentIdx += 1
    
    while rightIdx < len(arrRight):
        arr[currentIdx] = arrRight[rightIdx]
        rightIdx += 1
        currentIdx +=1

    return arr


# def merge_sort(arr):
#     divide_and_conquer(arr, 0, len(arr) - 1)

# def divide_and_conquer(arr, left, right):
#     if(left < right):
#         middle = (left + right)//2
#         divide_and_conquer(arr, left, middle)
#         divide_and_conquer(arr, middle + 1, right)
#         merge(arr, left, right, middle)

# def merge(arr, left, right, middle):
#     arrLeft = arr[left:middle + 1]
#     arrRight = arr[middle + 1:right + 1]
#     leftIdx = rightIdx = remainIdx = 0
#     for i in range(left, right):
#         if leftIdx < len(arrLeft) and rightIdx < len(arrRight):
#             if(arrLeft[leftIdx] <= arrRight[rightIdx]):
#                 arr[i] = arrLeft[leftIdx]
#                 leftIdx += 1
#             else:
#                 arr[i] = arrRight[rightIdx]
#                 rightIdx += 1
#             remainIdx = i + 1

#     while leftIdx < len(arrLeft):
#         arr[remainIdx] = arrLeft[leftIdx]
#         leftIdx += 1
#         remainIdx += 1
    
#     while rightIdx < len(arrRight):
#         arr[remainIdx] = arrRight[rightIdx]