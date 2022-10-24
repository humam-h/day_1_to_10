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

      


