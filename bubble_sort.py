#Write a python program to implement a Bubble Sort algorithm.
 
def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  # iterates over the list from the first element to the second-to-last element. This is because after each iteration of the inner loop, the largest element "bubbles" to the end of the list, so the last element in the list is already sorted.
        for j in range(len(list1)-1):   #iterates from the first element to the second-to-last element of the list. This loop compares adjacent elements and swaps them if they are in the wrong order.
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
list1 = [81,82,56,57,30,19,84,47,42,25]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))