#BMI calculator in Python
height = float(input("Please enter your height in m: "))
weight = float(input("Please enter your weight in kg: "))


BMI = round(weight/height**2)
message =print(f"Your bmi is {BMI}")

if BMI < 18.5:
  print(message+"You are underweight")
elif BMI > 18.5 and BMI < 25:
  message
  print("You have normal weight") 
elif BMI >25 and BMI < 30:
  print(message+"You are overweight")
elif BMI >30 and BMI <35:
  message
  print("You are obese")
else:
  message
  print("You are clinically obese")
