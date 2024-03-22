#Name: Najja McGee
#Course: CIS 111
#Section: 02
#Date: June 15th, 2023
#Program Name: Programming Exercise 2.4

#Algorithm
#Step 1: The computer will process the mod of 2 is less than 0
#Step 2: It will then display the word "odd"
#Step 3: Next the computer will process the days of 32
#Step 4: Then since the days are greater than 31 it will display "Not a valid day of the month
#Step 5: The computer will process "c" and will see that the character c is not a constitute like "a" or "i"
 
num = 61
if num % 2 > 0:
   print ("Odd")

days = 32
if days > 31:
  print("Not a valid day of the month.")

character = "c"
if character not in ["a", "i"]:
  print(f"the letter'{character}'does not also constitute a word.")