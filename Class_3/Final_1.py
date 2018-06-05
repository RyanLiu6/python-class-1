import operator

def main():
    myList = [1, 2, 3, 4, 5]
    # print(hasPairs(myList, 7))
    # arr = [12, 11, 13, 5, 6]
    # insertionSort(arr, True)
    # print ("Sorted array is:")
    # for i in range(len(arr)):
    #     print ("%d" %arr[i])

    values = [2, 4, 5, 7, 6]
    riddle(values, 0, 4)
    print(values)


def hasPairs(inputList, targetVal):
    myMap = {}

    for index in range(len(inputList)):
        myMap[inputList[index]] = index

    for num in inputList:
        value = targetVal - num
        if myMap.get(value, None) != None:
            return True

    return False


# Function to do insertion sort
def insertionSort(arr, reverse=False):
    # Traverse through 1 to len(arr)
    lt = operator.gt if reverse else operator.lt
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and lt(key, arr[j]):
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def riddle(nums, indexA, indexB):
    print("riddle ", indexA, indexB)
    if indexA >= indexB:
        return

    nums[indexA], nums[indexB] = nums[indexB], nums[indexA]
    print(nums)

    if nums[indexA] % 2 == 1:
        riddle(nums, indexA, indexB-2)
        riddle(nums, indexA+2, indexB)
    else:
        riddle(nums, indexA, indexB-3)
        riddle(nums, indexA+1, indexB)


if __name__ == "__main__":
    main()
