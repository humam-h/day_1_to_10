#Write your code below this line ๐
pn_list = [1, 2, 3]
def prime_checker(number):
    if number in pn_list:
        print("It's a prime number")
    elif number % 2 == 0 and number % 3 == 0:
        print("It's not a prime number")
    elif number % 5 == 0:
        print("It's not a prime number")
    elif number % 1 ==0 and number % number == 0:
        print("It's a prime number")




#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)



