def duplicate_number_remover(numbers): # defining a new function
    list_numbers = list(set(numbers)) # list is a function
    list_numbers.sort(reverse=True) # sorts list in descending order
    return list_numbers


numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)  # adds the numbers to the end of file
    #for item in num:
        #if item not in num:
            #num.append(item)
            ## I wasn't able to get comprehension + enumerate working in time as this method would allow the
            ## list to be returned in order

result = duplicate_number_remover(numbers)
print("Result:", result)  # shows output of result removing duplicate numbers
