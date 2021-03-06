# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        cur_index = i
        curr_numb = arr[i]

        while cur_index > 0 and curr_numb < arr[cur_index - 1]:
            # swap them 
            arr[cur_index], arr[cur_index - 1] = arr[cur_index - 1], arr[cur_index]
            # we need to keep track of our current books changing index
            cur_index -= 1

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    length = len(arr)
    
    for i in range(length - 1):
        for j in range(0, length-i-1):
                
                
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    


    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
