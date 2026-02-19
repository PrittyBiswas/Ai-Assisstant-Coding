#The user is asking for help with prompt engineering for loop generation. They want to:

#Create a Python code that takes a list of rainfall values
#Prints only values above 50mm
#Labels them as "heavy rainfall"
#Provide a suitable prompt, code, explanation, and output

#Prompt:
#Write a Python code that takes a list of rainfall values and prints only those values that are above 50mm, labeling them as "heavy rainfall".      
#Code:
rainfall_values = [10, 25, 55, 70, 30, 80, 45]      

for value in rainfall_values:
    if value > 50:
        print(f"{value}mm - heavy rainfall")    
#Explanation:
#The code initializes a list of rainfall values. It then iterates through each value in the list using a for loop. Inside the loop, it checks if the current value is greater than 50mm. If the condition is true, it prints the value along with the label "heavy rainfall". This way, only the values that exceed 50mm are displayed with the appropriate label.

#Output:
# 55mm - heavy rainfall
# 70mm - heavy rainfall   
# 80mm - heavy rainfall

