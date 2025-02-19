# FILE NAME - triangle_area.py
# DRG - Rerun for points 2025-02-18-2343
# NAME: Michael Orcutt
# DATE: 2/14/2025
# BRIEF DESCRIPTION: A program to calculate the area of a triangle. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





########## ENTER YER CODE BELOW THIS LINE ##########
    
def find_area():   
    y_val = input("\nEnter the height: ")
    x_val = input( "Enter the base: ")
    area = (float(y_val) * float(x_val)) / 2    
    print(f'\nThe area of the triangle is {area}\n')
    
    
find_area()
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the height: 1
Enter the base: 1

The area of the triangle is 0.5

'''



'''

Enter the height: 8
Enter the base: 4

The area of the triangle is 16.0

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the flow of the program? Which line of code kicks off the process?

It goes from getting values through input() and then calculates the area on line 24.



2. What was the hardest part of this lab?

The hardest part of this lab was deciding when to convert to float to have the decimal place.



'''
