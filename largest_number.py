

def largest_number (list_of_integers):
    

    if len(list_of_integers) == 1:
        return list_of_integers[0]


    largest_num = largest_number(list_of_integers[1:])

    if list_of_integers[0] > largest_num:
        return list_of_integers[0]
    else:
        return largest_num
    

# print (largest_number([2,3,4,10,1,7]))


