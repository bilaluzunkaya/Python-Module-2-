""""
#Module-2 Assignment
#A1:
name = input("Give name: ")
greeting = f"Hello, {name}!"
print(greeting)
""""
""""
#A2:
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is", area)
"""
"""""
#A3
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print("The perimeter of the rectangle is", perimeter)
print("The area of the rectangle is", area)

"""

"""""

#A4

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))


sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average_of_numbers = sum_of_numbers / 3

#
print(f"The sum of the numbers: {sum_of_numbers}")
print(f"The product of the numbers: {product_of_numbers}")
print(f"The average of the numbers: {average_of_numbers}")
"""
"""
#A5 
talents = float(input("Enter Leiviskät: "))
pounds = float(input("Enter Naulat: "))
lots = float(input("Enter Luodit: "))


# 1 luoti = 13.3 g
# 1 naula = 32 luotia
# 1 leiviskä = 20 naulaa
total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)


kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000


print("Nykyaikainen massa:")
print(f"{kilograms} kilogrammaa ja {remaining_grams:.2f} grammaa.")
"""
""""
#A6
code3_1 = random.randint(1, 6)
code3_2 = random.randint(1, 6)
import random


code3_1 = random.randint(0, 9)
code3_2 = random.randint(0, 9)
code3_3 = random.randint(0, 9)


code4_1 = random.randint(1, 6)
code4_2 = random.randint(1, 6)
code4_3 = random.randint(1, 6)
code4_4 = random.randint(1, 6)


print(f"3-digit code: {code3_1}{code3_2}{code3_3}")
print(f"4-digit code: {code4_1}{code4_2}{code4_3}{code4_4}")
"""
