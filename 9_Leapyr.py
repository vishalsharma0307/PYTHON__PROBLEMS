while True :

    x=int(input("Enter the year :"))
    if((x%100==0)and(x%400==0)):
        print(x,"IS a Leap year")
    elif((x%100!=0)and(x%4==0)):
        print(x,"Is a leap yr")
    else:
        print(x,"IS not a leap yr")