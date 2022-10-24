#Rollercoaster ticket
print("Wecome to rollercoaster tickets service ")
hight=int(input("enter your hight: "))
if hight >= 120:
      print("you can ride")
      age=int(input("enter your age: "))
      if age <= 12:
          print("please pay 5$")
      elif age <= 18:
          print("please pay 7$")
      else:
          print("please pay 12$")
else:
    print("sorry you have to grwo taller")