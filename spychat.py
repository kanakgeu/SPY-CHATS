spy_list={'kanak':{'rating':4.0,'age':21,'status':'','friends':[''],'salutation':'Mr.' }}
status_history={}
status=['available','busy','online']


def spy_status(name):
    print spy_list[name]['status']
    status_option=int(raw_input("1.update old status \n2.Add new status\n3.Choose from pre-defined status"))
    if status_option==1:
        print "your current status is: "+spy_list[name]['status']
        for i in range(len(status_history[name])):
            print str(i+1)+". "+str(status_history[name][i])
        status1=int(raw_input("choose from above options: "))
        status1=status1-1
        spy_list[name]['status']=spy_list[name]['status'][status1]
        print "Your status updated successfully!"
    elif  status_option==2:
        status2=raw_input("Enter your new status:")
        spy_list[name].update({'status':status2})
        print "Your new status added successfully!"
    else:
        print "Invalid option!"
    print spy_list[name]['status']


def spy_friend(name):
    f_name = raw_input("Enter your friend name:")
    if len(f_name)!=0:
        f_age = int(raw_input("Enter your friend age:"))
        if f_age > 12 and f_age < 50:
            f_rating = float(raw_input("Give the rating to spy:"))
            if f_rating < spy_list[name]['rating']:
                print "This can not added in your friendlist. "
            else:
                spy_list[name]['friends'].append(f_name)
                print "your friend added successfully in your list!"
        else:
            print "You cannot be added.\n"
    else:
        print "Invalid name!"
    print len(spy_list[name]['friends'])


def select_a_friend(name):
    friend_list = len(spy_list[name]['friends'])
    if friend_list == 0:
        print "You have no friends added. \n"
        return ("null")
    else:
        print "In your friend list,You have various people .\n"
        for i in range(0, friend_list):
            print str(i + 1) + ". " + str((spy_list[name]["friends"].keys())[i])
        position = int(
            raw_input("Enter the number friends with whom you want to chat: "))
        position = position - 1
        if (position < 0 or position >= friend_list):
            print "You have entered a wrong input\nTry again.\n"
            return ("null")
        else:
            return (position)


def chat_read(name):
    position = select_a_friend(name)
    if position == "null":
        return ()
    f_name = spy_list[name]["friends"].keys()[position]
    print "Chat history:\n"
    print spy_list[name]["friends"][f_name]["chat"]

while True:
    user_choice=int(raw_input("Do you want to continue as:\n1. Default user.\n2. New user."))
    if user_choice==1:
        import spy_details
        spy_list.update(spy_details.spy_list)
        name = spy_details.spy_list.keys()[0]
        status_history.update(spy_details.status_history)
        status_history[name].append(spy_list[name]["status"])

    elif user_choice==2:
        name=raw_input("Enter your name: ")
        if len(name) ==0:
            print "Invalid name. "
            continue
        else:
            sal=int(raw_input("Enter your salutation:\n1.Mr. \n2.Ms."))
            if sal==1:
                salutation="Mr"
            elif sal==2:
                salutation="Ms"
            else:
                print "Wrong salutation entered\n"
                continue
            age=int(raw_input("Enter your age"))
            if age>12 and age<50:
                rating=float(raw_input("Give the rating to spy:"))
                online_status = raw_input("Enter your status:")
                spy_list.update({name: dict(salutation=salutation, age=age, rating=rating ,status=online_status)})
                print "you added to spychat successfully!"
                status_history.update({name:[online_status]})
            else:
                print "Your age cannot be authenticated.\n"
    else:
        print "Wrong input"
        continue
    if name in spy_list:
        print "Welcome %s %s \nage= %i and rating= %i status=%s" %(spy_list[name]['salutation'],name,spy_list[name]['age'],spy_list[name]['rating'],spy_list[name]['status'])
        spy_menu=int(raw_input("Enter the choice:\n1.Add status update \n2.Add a friend \n3.Send an secret message \n4.Read a secret message \n5.Read chats from a user \n6.Close application"))
        if spy_menu==1:
            spy_status(name)
        elif spy_menu==2:
            spy_friend(name)
      
        else:
            print "Invalid Input!"
            continue
    else:
        if len(name) ==0:
            print "Invalid name. "
            continue
        else:
            sal=int(raw_input("Enter your salutation:\n1.Mr. \n2.Ms."))
            if sal==1:
                salutation="Mr"
            elif sal==2:
                salutation="Ms"
            else:
                print "Wrong salutation entered\n"
                continue
            age=int(raw_input("Enter your age"))
            if age>=12 and age<50:
                rating=float(raw_input("Give the rating to spy:"))
                online_status = raw_input("Enter your status:")
                spy_list.update({name: dict(salutation=salutation, age=age, rating=rating ,status=online_status)})
                print "you added to spychat successfully!"
                status_history.update({name:[online_status]})
            else:
                print "Your age cannot be authenticated.\n"
                continue
        opt=raw_input("Run again? press \"y\" else any other key: ")
        if opt=="y":
            continue
        else:
            break