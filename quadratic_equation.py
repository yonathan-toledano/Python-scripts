###  Notes ###
### Name: Yonathan toledano ###

import math

def quadratic_equation(a,b,c):
    # the number of solutions depends with the outcome of the Discriminant.
    # setting the Discriminant as a variable will make it easier.
    discr = ((b**2) - (4*a*c))
    if discr < 0:
        return None , None
    if discr == 0:
        x1= ((b*-1) / (2*a))
        return x1 , None
    if discr > 0:
        #sol 1 & 2 are the two possible solutions.
        sol1 = ((b*-1) + (math.sqrt(discr)))
        sol2 = ((b*-1) - (math.sqrt(discr)))
        x1 = ((sol1) / (2*a))
        x2 = ((sol2) / (2*a))
        return x1 , x2

def quadratic_equation_user_input():
    # with the split command it will be easy to use to user inputs
    user_choice = (input("Insert coefficients a, b, and c: ") .split(' '))
    a = float(user_choice[0])
    if a == 0:
        # the user cant choose the number 0 as the first coefficient
        print ("The parameter 'a' may not equal 0")
    else:
        b = float(user_choice[1])
        c = float(user_choice[2])
        #once again the number of solutions depends with the outcome of
        # the Discriminant.
        discr = ((b ** 2) - (4 * a * c))
        if discr < 0:
            print ('The equation has no solutions')
        if discr == 0:
            print ('The equation has 1 solution:' ,
                   (quadratic_equation(a,b,c)[0]))
        if discr > 0:
            print ("The equation has 2 solutions:",
                   (quadratic_equation(a,b,c)[0]) , "and" ,
                   (quadratic_equation(a,b,c)[1]))
