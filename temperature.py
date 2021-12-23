###  Notes ###
### Name: Yonathan toledano ###

def two_lowest_temp(num1,num2,num3):
### this function will tell the 2 lowest numbers out of 3, by using this
# function it will be rather easy to define the second function. ###
    if num1 <= num2 <= num3:
        low1 = num1
        low2 = num2
    elif num1 <= num3 <= num2:
        low1 = num1
        low2 = num3
    elif num2 <= num1 <= num3:
        low1 = num2
        low2 = num1
    elif num2 <= num3 <= num1:
        low1 = num2
        low2 = num3
    elif num3 <= num2 <= num1:
        low1 = num3
        low2 = num2
    else:
        low1 = num3
        low2 = num1
    return low1 , low2

def is_it_summer_yet(min_temp,temp1,temp2,temp3):
    if (min_temp > two_lowest_temp(temp1,temp2,temp3)[0]) and\
            (min_temp > two_lowest_temp(temp1,temp2,temp3)[1]):
        return False
    else:
        return True