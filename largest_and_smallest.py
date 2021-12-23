###  Notes ###
### Name: Yonathan toledano ###
#the 4th test will check if the function will work with negetive numbers
# the 5th test will check if mathematical operations inside the aurgements
# wont effect the expected function result.

def largest_and_smallest(num1,num2,num3):
    # I will call the variables 'max_num' and 'min_num', but wont use the max
    # or min functions.
    #MAX#
    if num1 > num2 and num1 > num3:
        max_num = num1
    elif num2 > num3:
        max_num = num2
    else:
        max_num = num3
    #MIN#
    if num1 < num2 and num1 < num3:
        min_num = num1
    elif num2 < num3:
        min_num = num2
    else:
        min_num = num3
    return (max_num , min_num)

def check_largest_and_smallest():
    if (largest_and_smallest(17,1,6)[0] != 17) or\
            (largest_and_smallest(17,1,6)[1] != 1):
        return  False
    if (largest_and_smallest(1,17,6)[0] != 17) or\
            (largest_and_smallest(1,17,6)[1] != 1):
        return  False
    if (largest_and_smallest(1,1,2)[0] != 2) or\
            (largest_and_smallest(1,1,2)[1] != 1):
        return  False
    if (largest_and_smallest(-3,-2,0)[0] != 0) or\
            (largest_and_smallest(-3,-2,0)[1] != -3):
        return  False
    if (largest_and_smallest(20/2,4-5,1.123)[0] != 10) or\
            (largest_and_smallest(20/2,4-5,1.123)[1] != -1):
        return  False
    else:
        return True