# Ask For Age
# age = input("How old are you: ")
# if age:
#   age = int(age)
#   if age >= 18 and age < 21:
#     print("You can enter, but need a wristband!")
#   elif age >= 21:
#     print("You are good to enter and can drink")
#   else:
#     print("You can't come in")
# else:
#   print("Please enter a age!")

# Ask For Age
age = input("How old are you: ")
if age:
  age = int(age)
  if age >= 21:
    print("You are good to enter and can drink")
  elif age >= 18:
    print("You can enter, but need a wristband!")
  else:
    print("You can't come in")
else:
  print("Please enter a age!")