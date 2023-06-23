#Write a python program to implement Selection sort.
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):#The outer loop for i in range(len(arr)) iterates through each element of the array. It represents the boundary between the sorted and unsorted parts of the array.
        
        # Find the minimum element in the remaining unsorted part
        min_index = i# represents the current minimum element's index.
        for j in range(i+1, len(arr)):# searches for the minimum element in the remaining unsorted part of the array. 
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
print("Unsorted array:", arr)

sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)