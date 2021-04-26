#Jackson E. Rollins
#4/11/2021

#Program that asks for a year from the user and then determines if it is a leap year or not

n = input("Please enter a year. Positive integer values only: ")

year = int(n)

if (year%400 == 0):
    print("% s is a Leap Year." % year)
elif (year%100 == 0):
    print("% s is not a Leap Year." % year)
elif (year%4 == 0):
    print("% s is a Leap Year." % year)
else:
    print("% s is not a Leap Year." % year)