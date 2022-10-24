#BMI calculator:
hight = input("enter your hight in m: ")
weight = input("enter your weight in kg: ")
h= float(hight)
w= float(weight)
bmi= w / h**2
print(int(bmi))

#Age calculator:
age=input("what is your current age? ")
a= 90 - int(age)
x= a * 365
y= a *52
z= a *12
print(f"you have {x} days, {y} weeks, and {z} months left.")

#Bell and tip calculator:
print("welcome to bell calculator!")
bell=float(input("what was the total bell? $ "))
tip_per=int(input("what presenatge tip would like to give: 10, 12, or 15? "))
people=int(input("who many people to split the bell? "))
tip= (tip_per / 100) * bell
total_bell= (tip + bell) / people
result=round( total_bell, 2)
result="{:.2f}".format(total_bell)
print(f"each person should pay: {result} $ ")


            


