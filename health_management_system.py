def getdate():
    import datetime
    return datetime.datetime.now()

def lock_harry():
    while (True):
        user21 = input('Harry! What do you want to Lock? \n Press C for Exercise \n Press D for Diet \n')
        if (user21 == 'C'):
            str1 = input('Enter your Exercise Plans : ')
            a = open('harry_exercise.txt','w')
            a.write(str(getdate()) + " " + str1)
            a.close()
            break
        elif (user21 == 'D'): 
            str2 = input('Enter your Diet Plans : ')
            b = open('harry_diet.txt','w')
            b.write(str(getdate()) + " " + str2)
            b.close()
            break
        else:
            print('Enter a Proper Value!')

def lock_rohan():
    while (True):
        user22 = input('Rohan! What do you want to Lock? Exercise or Diet? \n Press E for Exercise \n Press F for Diet \n')
        if (user22 == 'E'):
            str3 = input('Enter your Exercise Plans : ')
            c = open('rohan_exercise.txt','w')
            c.write(str(getdate()) + " " + str3)
            c.close()
            break
        elif (user22 == 'F'):
            str4 = input('Enter your Diet Plans : ')
            d = open('rohan_diet.txt','w')
            d.write(str(getdate()) + " " + str4)
            d.close()
            break
        else:
            print('Enter a Proper Value!')

def lock_hammad():
    while (True):
        user23 = input('Hammad! What do you want to Lock? Exercise or Diet? \n Press G for Exercise \n Press H for Diet \n')
        if (user23 == 'G'):
            str5 = input('Enter your Exercise Plans : ')
            e = open('hammad_exercise.txt','w')
            e.write(str(getdate()) + " " + str5)
            e.close()
            break
        elif (user23 == 'H'):
            str6 = input('Enter your Diet Plans : ')
            f = open('hammad_diet.txt','w')
            f.write(str(getdate()) + " " + str6)
            f.close()
            break
        else:
            print('Enter a Proper Value!')

def retrieve_harry():
    while (True):
        user31 = input('What do you want to Retrieve? Exercise or Diet? \n Press I for Exercise \n Press J for Diet \n')
        if (user31 == 'I'):
            with open('harry_exercise.txt') as harry1:
                for a in harry1:
                    print(a)
                    break
            break
        elif (user31 == 'J'):
            with open('harry_diet.txt') as harry2:
                for b in harry2:
                    print(b)
                    break
            break
        else:
            print('Enter a Proper Value!')

def retrieve_rohan():
    while (True):
        user32 = input('What do you want to Retrieve? Exercise or Diet? \n Press K for Exercise \n Press L for Diet \n')
        if (user32 == 'K'):
            with open('rohan_exercise.txt') as rohan1:
                for c in rohan1:
                    print(c)
                    break
            break
        elif (user32 == 'L'):
            with open('rohan_diet.txt') as rohan2:
                for d in rohan2:
                    print(d)
                    break
            break
        else:
            print('Enter a Proper Value!')

def retrieve_hammad():
    while (True):
        user33 = input('What do you want to Retrieve? Exercise or Diet? \n Press O for Exercise \n Press P for Diet \n')
        if (user33 == 'O'):
            with open('hammad_exercise.txt') as hammad1:
                for e in hammad1:
                    print(e)
                    break
            break
        elif (user33 == 'P'): 
            with open('hammad_diet.txt') as hammad2:
                for f in hammad2:
                    print(f)
                    break
            break
        else:
            print('Enter a Proper Value!')

def user():
    user1 = input('Select your Client :\n Press 1 for Harry \n Press 2 for Rohan \n Press 3 for Hammad \n ')
    if (user1 == '1'):
        while (True):
            user2 = input('Do you want to Lock Or Retrieve the data? \n Press A for Lock \n Press B for Retrieve \n')
            if (user2 == 'A'):
                lock_harry()
                break
            elif (user2 == 'B'):
                retrieve_harry()
                break
            else:
                print('Enter a Proper Value!')
            
    elif (user1 == '2'):
        while (True):
            user3 = input('Do you want to Lock Or Retrieve the data? \n Press X for Lock \n Press Y for Retrieve \n')
            if (user3 == 'X'):
                lock_rohan()
                break
            elif (user3 == 'Y'):
                retrieve_rohan()
                break
            else:
                print('Enter a Proper Value!')
            
    elif (user1 == '3'):
        while (True):
            user4 = input('Do you want to Lock Or Retrieve the data? \n Press M for Lock \n Press N for Retrieve \n')
            if (user4 == 'M'):
                lock_hammad()
                break
            elif (user4 == 'N'):
                retrieve_hammad()
                break
            else:
                print('Enter a Proper Value!')
            
    else:
        print('Enter a Proper Value!')
        user()
user()
while (True):
    again = input('Do you want to select your Client again? \n Press Y for YES \n Press N for NO \n')
    if (again == 'Y'):
        user()
    elif (again == 'N'):
        print('GoodBye! Have a Nice Day.')
        break
