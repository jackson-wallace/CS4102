def insertionSort(l, start, end):
    # TODO: IMPLEMENT INSERTION SORT

    for j in range(start+1, end+1):

        # j starts at index 1
        key = l[j]

        # i points to the end of the "sorted" subarray
        i = j - 1

        # while i is not less than first index and the value at i
        # is greater than the value at j
        while i >= start and l[i] > key:

            # move the value at i up one index
            l[i + 1] = l[i]

            # decrement i
            i = i - 1

        # swap key (l[j]) into its final position
        l[i+1] = key


def medianOfThree(l, left, mid, right):

    # dictionary containing value : index pairs
    d = {
        l[left]: left,
        l[mid]: mid,
        l[right]: right
    }

    # sort values
    vals = sorted([l[left], l[mid], l[right]])

    # return median value, median value index
    return vals[1], d[vals[1]]


def partition(l, i, j):
    # TODO: NEED PARTITION FOR QUICKSORT
    # print(l)

    # find pivot and its index using median of three
    pivot, pIdx = medianOfThree(l, i, (i+j)//2, j)
    # print("pivot: " + str(pivot))
    # print("PivotIdx: " + str(pIdx))

    # pIdx = j
    # pivot = l[j]

    # swap pivot value with last value in the list
    l[pIdx], l[j] = l[j], l[pIdx]

    # left points to the index to which values less than the pivot will be swapped
    left = i - 1

    # right loops through array
    for right in range(i, j):
        # print("leftPointer: " + str(left), "rightPointer: " + str(right))
        # if right points to a value less than the pivot
        if l[right] < pivot:
            # we increment left to point to the index where the value will go
            left += 1
            # swap the values at left, right
            l[left], l[right] = l[right], l[left]
    # swap the pivot value into its final location
    l[left+1], l[j] = l[j], l[left+1]
    # return the index of the pivot's final location
    return left + 1


def quickSort(l, i, j, minSize):
    # TODO: IMPLEMENT QUICKSORT
    # print(l)
    if i < j and j-i >= minSize:
        q = partition(l, i, j)
        quickSort(l, i, q-1, minSize)
        quickSort(l, q+1, j, minSize)


def quickSortHybrid(l, i, j, minSize):
    # TODO: IMPLEMENT QUICKSORT
    # print(l)
    if i < j and j-i >= minSize:
        q = partition(l, i, j)
        quickSortHybrid(l, i, q-1, minSize)
        quickSortHybrid(l, q+1, j, minSize)
    else:
        insertionSort(l, i, j)
