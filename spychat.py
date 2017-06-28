from steganography.steganography import Steganography
spy_list={}
status_history={}
status=['available','busy','online']
flag=0
def spy_status(name):
    print spy_list[name]['status']
    status_option=int(raw_input("1.update old status \n2.Add new status\n3.Choose from pre-defined status"))
    if status_option==1:
        print "your current status is: "+spy_list[name]['status']
        for i in range(len(status_history[name])):
             print str(i+1)+". "+str(status_history[name][i])
        select1=int(raw_input("Choose option from above: "))
        select1=select1-1
        if select1+1>len(status_history[name]):
            print "Wrong input! Plz enter right ooption."
            return
        else:
            spy_list[name]['status']=status_history[name][select1]
            print "Your status updated successfully!"
    elif  status_option==2:
        status2=raw_input("Enter your new status:")
        spy_list[name].update({'status':status2})
        print "Your new status added successfully!"
        if status2 not in status_history[name]:
            status_history[name].append(status2)
    elif status_option==3:
        for i in range(len(status)):
            print str(i+1)+". "+str(status[i])
        select1=int(raw_input("Enter the choice: "))
        select1=select1-1
        if select1+1>len(status_history[name]):
            print "Wrong input! Plz enter right option."
            return
        else:
            spy_list[name]['status']=status[select1]
            if status[select1] not in status_history[name]:
                status_history[name].append(status[select1])
            print "Your status updated successfully!"
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
                spy_list[name]['friends'].update({f_name:{'f_age':f_age,'f_rating':f_rating,"chat":{}}})
                print "your friend added successfully in your list!"
        else:
            print "You cannot be added.\n"
            return()
    else:
        print "Invalid name!"
        return()
    print len(spy_list[name]['friends'])
def select_a_friend(name):
    friend_list = len(spy_list[name]['friends'].keys())
    if friend_list == 0:
        print "You have no friends added. \n"
        return ("null")
    else:
        print "You have following people in your friend list: \n"
        for i in range(0, friend_list):
            print str(i + 1) + ". " + str(spy_list[name]["friends"].keys()[i])
        position = int(raw_input("Enter the number friends with whom you want to chat: "))
        position = position - 1
        if (position < 0 or position >= friend_list):
            print "You have entered a wrong input\nTry again.\n"
            return ("null")
        else:
            return (position)
def send_a_message(name):
    global flag
    position = select_a_friend(name)
    if position == 'null':
        return (0)
    else:
        f_name = spy_list[name]['friends'].keys()[position]
        from steganography.steganography import Steganography
        path_name = "C:\Users\Kanak Goel\Desktop"
        img_name = raw_input("What is the image name?: ")
        path = path_name +"\\" + img_name
        print "your path with specified image name is: " + path
        d_img_name = raw_input("What name should be the output file?: ")
        d_path = "C:\Users\Kanak Goel\Desktop"
        overall_path = d_path + "\\" + d_img_name
        print overall_path
        text = raw_input("Enter the TEXT to encode: ")
        from datetime import datetime
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        flag = flag + 1
        spy_list[name]['friends'][f_name]['chat'].update({flag: {"secret_message": text, "time": date,"boolean": True}})
        print "Come down..................................."
        q= text.strip().split(" ")
        Steganography.encode(path, overall_path, text)
        print "\nMessage has been encoded and sent to %s.\n" % (
            str(spy_list[name]['friends'].keys()[position]))
def read_a_message(name):
    global flag
    position = select_a_friend(name)
    if position == "null":
        return ()
    else:
        from steganography.steganography import Steganography
        f_name = spy_list[name]['friends'].keys()[position]
        print "Friend %s selected\n" % (f_name)
        d_img_name = raw_input("What is the name of the output file you want to decode?: ")
        d_path = "C:\Users\Kanak Goel\Desktop"
        overall_path = d_path+"\\"+ d_img_name
        from datetime import datetime
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print "come down...................................."
        secret_text = Steganography.decode(overall_path)
        if len(secret_text) == 0:
            print "Image has no secret message"
        else:
            print "\nYour secret text is: " + secret_text
def chat_read(name):
    position = select_a_friend(name)
    if position == "null":
        return ()
    f_name = spy_list[name]["friends"].keys()[position]
    print "Chat history:\n"
    print spy_list[name]["friends"][f_name]["chat"]
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
    else:
        sal=int(raw_input("Enter your salutation:\n1.Mr. \n2.Ms."))
        if sal==1:
            salutation="Mr"
        elif sal==2:
            salutation="Ms"
        else:
            print "Wrong salutation entered\n"
        age=int(raw_input("Enter your age"))
        if age>12 and age<50:
            rating=float(raw_input("Give the rating to spy:"))
            online_status = raw_input("Enter your status:")
            spy_list.update({name:{"salutation":salutation, "age":age, "rating":rating ,"status":online_status, "friends":{}}})
            print "you added to spychat successfully!"
            status_history.update({name:[online_status]})
        else:
            print "Your age cannot be authenticated.\n"
else:
    print "Wrong input"
print "Welcome %s %s \nage= %i and rating= %i status=%s" %(spy_list[name]['salutation'],name,spy_list[name]['age'],spy_list[name]['rating'],spy_list[name]['status'])
while True:
    if name in spy_list:
        print ""
        spy_menu=int(raw_input("Enter the choice:\n1.Add status update \n2.Add a friend \n3.Send an secret message \n4.Read a secret message \n5.Read chats from a user \n6.Close application"))
        if spy_menu==1:
            spy_status(name)
        elif spy_menu==2:
            spy_friend(name)
        elif spy_menu == 3:
            send_a_message(name)
        elif spy_menu == 4:
            read_a_message(name)
        elif spy_menu == 5:
            chat_read(name)
        elif spy_menu == 6:
            exit()

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