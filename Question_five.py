def binary_search(arr, x):
    length=len(arr)
    if  length== 0: #Base case
        return False
    else:
        mid_element = len(arr)//2 #Divideing array into part to get the middle element
        #If element is in the middle
        if (x == arr[mid_element]):  #checking if the middle element is the x
            return True
        else:

            if x > arr[mid_element]:   # If element is somwhere else not in the middle
                return binary_search(arr[mid_element+1:],x)
            else:                            # If element is not in the array

                return binary_search(arr[:mid_element],x)
print(binary_search([1,2,3,4,5,6,7],8))