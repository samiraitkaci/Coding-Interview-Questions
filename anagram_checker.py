#ANAGRAM CHECKER
word = input("Input a string to be checked")

sorted1 = []
sorted2 = []

#this function starts from the last index value of the argument and returns the list starting from that value
def reverse(data_list):
    return data_list[::-1] #this is called slicing, -1 is the start value for the argument 

#this adds each letter to an array 'sorted1' by iterating by the length of 'word'
for i in word:
    sorted1.append(i)

#uses reverse function to reverse sorted1    
sorted2 = reverse(sorted1)

if sorted1 == sorted2:
    print("String is an anagram")
else:
    print("String is not an anagram")










