###  Notes ###
### Name: Yonathan toledano ###

def calculate_mathematical_expression(num1,num2,operation):
    if operation == '-':
       num = num1 - num2
       return num
    elif operation == '+':
        num = num1 + num2
        return  num
    elif operation == '*':
        num = num1 * num2
        return num
    elif operation == ':':
        if num2 == 0:
            return None
        num = num1 / num2
        return num
    else: return None

def calculate_from_string(str):
    # if we will use split command, well be able to use to numbers and
    # operation from the string in the previos function
   str1 = str.split(' ')
   num1 = float(str1[0])
   operation = str1[1]
   num2 = float(str1[2])
   return calculate_mathematical_expression(num1,num2,operation)
