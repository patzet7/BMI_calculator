# calculates the following:
# DANGER underweight = less than 18.5
# just normal = more or equal to 18.5 and less than 25
# ALERT overweight = more or equal to 25 and less than 30
# DANGER obesity = 30 or more

weight = int(input())
height = float(input())
x = weight/float(height*height)
if x < 18.5
    print("Underweight")
if x>=18.5 and x<25:
    print("Normal")
if x >= 25 and x < 30:
   print("Overweight")
else x >= 30:
   print('Obesity')
