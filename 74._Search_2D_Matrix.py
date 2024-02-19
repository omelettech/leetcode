def binarySearch(lo, mid, arr, key):
    hi = mid + 1
    while hi >= lo:
        if key == arr[mid]:
            return True
        if key < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
        mid = int((lo + hi) / 2)
    return False

def searchMatrix(matrix, target):
    # Number of rows
    num_rows = len(matrix)
    # Number of columns (assuming all rows have the same length)
    last_columns = len(matrix[0])-1
    high=num_rows-1
    low=0
    while high>=low:
        mid=int((high+low)/2)
        if target <= matrix[mid][last_columns] and (mid==0 or target>matrix[mid-1][last_columns]):
            #success
            return binarySearch(0, last_columns, matrix[mid], target)
        elif target>matrix[mid][last_columns]:
            low=mid+1
        else:
            high=mid-1

    return False


matrix1 = [
    [1, 2, 3]
]
print(searchMatrix(matrix1,2))
