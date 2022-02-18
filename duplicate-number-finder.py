myarray = []

for index in range(10):
    numbers = int(input('Input an integer'))
    myarray.append(numbers)

def duplicate(array):
    for i in array:
        numberOfTimes = array.count(i)
        if numberOfTimes > 1:
            print("Duplicate value is:", i)
            break



duplicate(myarray)

#   for i in myarray:
#        numberOfTimes = myarray.count(i)
#        if numberOfTimes > 1:
#            print("Duplicate value is:", [i])

