#ASSIGNMENT 2
# Caroline Breen 23364211
# 13/october/2024
import math 
name = input("Please enter your name:")
heightcm = input("Please enter your height in centimeters:")

# need to slice this float to get just numbers after decimal place

heightft = float(heightcm)/30.48
heightft2 = float(math.floor(heightft))

# - math.floor heightcm for the heightft that is printed!!!!

heightinches = float(heightft - heightft2)*12
heightinches2 = float(math.floor(heightinches))

heightqinches = float(heightinches - heightinches2)*4
heightqinches2 = float(math.floor(heightqinches))

# fix mathfloor(qinches) !!!!!!

# divided by 30.48 (cm to ft)
# multiply ft x 12 to convert to inches


print("Dear", name.upper(), "you are", heightft2, "feet,", heightinches2, "inches, and",
      heightqinches2, "quarter inches tall.")


input("\n\nPress the enter key to exit.")


