#Number checker:
#print(" Welcome to odd/even numbers checker!")
#number=int(input("Which number do you want to check!: "))
#if number % 2 == 0:
#    print(" This is even number.! ")
#else:
#    print("This is odd number.! ")

#Rollercoaster ticket
#print("Wecome to rollercoaster tickets service ")
#hight=int(input("enter your hight: "))
#if hight >= 120:
#      print("you can ride")
#      age=int(input("enter your age: "))
#      if age <= 12:
#          print("please pay 5$")
#      elif age <= 18:
#          print("please pay 7$")
#      else:
#          print("please pay 12$")
#else:
#    print("sorry you have to grwo taller")

# BMI Calculator:
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
#bmi = round(weight / height ** 2)
#if bmi < 18.5:
#  print(f"Your BMI is {bmi}, you are underweight.")
#elif bmi < 25:
#    print(f"Your BMI is {bmi}, you have a normal weight.")
#elif bmi < 30:
#    print(f"Your BMI is {bmi}, you are slightly overweight.")
#elif bmi < 35:
#    print(f"Your BMI is {bmi}, you are obese.")
#else:
#  print(f"Your BMI is {bmi}, you are clinically obese.")


#Leap years calculator:
year=int(input("choose a year: "))
st1= year % 4 ==0
st2= year % 100 ==0
st3= year % 400 ==0
if st1==False:
    print(f" the year {year} is not leap!")
elif st2==False:
    print(f" the year {year} is a leap!")
elif st3==True:
    print(f" the year {year} is a leap!")
else:
    print(f" the year {year} is not leap!")

      


