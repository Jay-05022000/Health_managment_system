'''Health managment system.you have 3 clients and you have to store their diet plan and exercise they do.
user can log data into system and also can retrieve data from the system.'''


# Global variables

jay_diet=[]
nidhi_diet=[]
kirtan_diet=[]
jay_exercise=[]
nidhi_exercise=[]
kirtan_exercise=[]


def a(n):
    print("Hey ",n)
    type=input("what kind of data you want to log?: ")
    if (type=='diet'):
        jay_diet.append(input("enter your data: "))
        print("Thanks for your response")
    elif (type=='exercise'):
        jay_exercise.append(input("enter your data: "))
        print("Thanks for your response")

    else:
        print("sorry we are not providing this service at this moment\nThank you!!")

def b(n):
    print("Hey ", n)
    type = input("what kind of data you want to log?: ")
    if (type=='diet'):
        nidhi_diet.append(input("enter your data: "))
        print("Thanks for your response")

    elif (type=='exercise'):
        nidhi_exercise.append(input("enter your data: "))
        print("Thanks for your response")

    else:
        print("sorry we are not providing this service at this moment\nThank you!!")

def c(n):
    print("Hey ", n)
    type=input("what kind of data you want to log?: ")
    if (type=='diet'):
        kirtan_diet.append(input("enter your data: "))
        print("Thanks for your response")

    elif (type=='exercise'):
        kirtan_exercise.append(input("enter your data: "))
        print("Thanks for your response")

    else:
        print("sorry we are not providing this service at this moment\nThank you!!")
while(True):
    i=int(input("Hey customer,what action you would like to perform\nenter 0 for log or 1 for retrieve: "))
    if (i==0):
        print("you have choosed to log data")
        user=input("enter your name: ")

        if(user=='jay'):
            a(user)
        elif(user=='nidhi'):
            b(user)
        elif (user=="kirtan"):
            c(user)
        else:
            print('you are not our customer.so you cant use this application')
    elif(i==1):
        print("you have choosed to retrieve data")
        user = input("enter your name: ")
        type = input("what kind of data you want to retrieve?: ")
        if (user=="jay") and (type=='diet'):
            print('here is your data ',jay_diet)
        elif (user=="jay") and (type=='exercise'):
            print('here is your data ',jay_exercise)
        elif (user=="nidhi") and (type=='diet'):
            print('here is your data ',nidhi_diet)
        elif (user=="nidhi") and (type=='exercise'):
            print('here is your data ',nidhi_exercise)
        elif (user=="kirtan") and (type=='diet'):
            print('here is your data ',kirtan_diet)
        elif (user=="kirtan") and (type=='exercise'):
            print('here is your data ',kirtan_exercise)
    else:
        print('wrong input!!choose right one next time')
        break