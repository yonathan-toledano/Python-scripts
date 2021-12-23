###  Notes ###
### Name: Yonathan toledano ###

import math

def shape_area():
    user_choice = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if user_choice == '1':
        radios = float(input())
        return (math.pi * (radios**2))
    elif user_choice == '2':
        first_side = float(input())
        second_side = float(input())
        return (first_side * second_side)
    elif user_choice == '3':
        triangle_side = float(input())
        return ((triangle_side**2) * ((math.sqrt(3)) / 4 ))
    else:
        return None
