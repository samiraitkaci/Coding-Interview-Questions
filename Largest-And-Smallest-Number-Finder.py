def bubble_sort(array): 
    n = len(array) 

    for i in range(n): #

        already_sorted = True #create flag that allows function to terminate early if there is nothing left to sort 

        for j in range(n - i - 1): #length of array minus current index within array minus one
            if array[j] < array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j] #if current value is greater then swap them

                already_sorted = False #as  i had to swap elements set  the already sorted flag to false to not finish the algorithm prematurely
        
        if already_sorted:
            break

    print(array)        
    print('Greatest:', array[0], 'Smallest', array[n-1])



numbers = [344,56,1,23454,5,9,8,0,2]
#for i in range(10):
#    integer = int(input('Input an integer'))
#    numbers.append(integer)

bubble_sort(numbers)
        

        
    


