print("Wecome to rollercoaster tickets service ")
hight=int(input("enter your hight: "))
bell = 0
if hight >= 120:
      print("you can ride")
      age=int(input("enter your age: "))
      if age <= 12:
          bell=  5
          print("child tickets are 5$")
      elif age <= 18:
          bell= 7
          print("youth tickets are 7$")
      elif age >= 45 and age <= 55:
          print("have a free ride with us")
      else:
          bell= 12
          print("adults tickets are 12$")
      wants_photo=input("do you want a photo taken? Y or N ")
      if wants_photo== "Y":
          bell += 3
          print(f"your final bell is {bell}")
else:
    print("sorry you have to grwo taller")