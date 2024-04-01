import csv  #for csv file
import stdiomask    #for masking password
import time     #for time pauses
from datetime import datetime   #for datetime
import pyttsx3      #for output voice
import username #for security credential
api=pyttsx3.init('sapi5')    #initialization of voice from api
voices=api.getProperty('voices')     
api.setProperty('voices',voices[0].id)  #taking audio from api

now = datetime.now()    #setting current date time
d2 = now.strftime("%d %b %Y %H:%M:%S")  #formatting datetime


def bol(audio): #function for output voice
    api.say(audio)  
    api.runAndWait()

def Ex_cept(xxx):
    while True:
        try:
            p=int((input(xxx)))
            return p
        except Exception as e:
            print(e)
            print("\n Please Enter Valid Input....!!!🙏")
            #bol("Please Enter Valid Input....!!!")


def y_n(ilu):
    while True:
        #bol("  press 'Y' if yes , 'N', if no ")
        k=input(ilu)
        if k=='y' or k=='Y' or k=='n' or k=='N':
            return k
        else:
            print("\n >>> uh-huh ☹...Please press 'Y' if yes , 'N' if no ")


def empty_space(khali):
    while True:
        
        k=input(khali)
        if k=='':
            print("\n Please Enter Valid Input....!!! 🙏")
            #bol("Please Enter Valid Input....!!!")
        else:
            return k
            




class Patient(): #class patient which we'll be using for data collection
    def __init__(self,date,name,age,cough,fever,tired,breath):  #constructor
        self.date=date
        self.name=name
        self.age=age
        self.cough=cough
        self.fever=fever
        self.tired=tired
        self.breath=breath
    def report(self):   #member function for printing report
        #bol('this is your updated recent report')
        print('\n------Updated Report 📑-------')
        for key,value  in (vars(self).items()):
            print (" {:<10} {:<3} {:<10} ".format(key,':',value))
        print('-----------------------------')
def patient_info(choice,name): #function for taking name and age for new registration
    if choice==2:
        print('\n>>> Tell me your first name please...😁 ')
        #bol(' tell me your first name please : ')
        name=empty_space('<<< ')
        name=name.capitalize()
    else:
        pass
    #time.sleep(0.5)
    print("\n>>> that's a good name ", name,'☺')
    #bol(f'thats a good name {name} ')
    #time.sleep(0.5)
    print('\n>>> How old are you...? 🤔')
    #bol('How old are you ')
    age=Ex_cept("<<< ")
    #time.sleep(0.5)
    #bol('Okay, Now lets examine you for some symptoms....')
    print('\n>>> Okay, Now lets examine you for some symptoms.... ⏳')
    return name,age
def patient_R_NR(choice,l): #function to check if patient is registred or not yet
    
    x=[]    
    y=[]
    total_visit=0
    print('\n>>> Tell me your first name please... ')
    #bol(' tell me your first name please : ')
    name=empty_space('<<< ')
    name=name.capitalize()
    csv_file=csv.reader(open('covidata.csv','r'))
    for i in csv_file:
        for j in i:
            if j==name:
                date,name,age,cough,fever,tired,breath=i[0],i[1],i[2],i[3],i[4],i[5],i[6]
                p=Patient(date,name,age,cough,fever,tired,breath)
                x.append(vars(p))
                total_visit=total_visit+1
    if total_visit>0: # if patient is registered 
        if choice==1:   #for follow up
            print("\n>>> Patient is already registered 🙄")
            #bol("Patient is already registered")
            print(">>> We are redirecting you for follow up..... 🔃")
            #bol("We are redirecting you for follow up.....")
        else:
            pass
        #time.sleep(0.5)
        print('\n>>> Welcome back...... 🙏',name,'\n   Hope you are doing great 😉')
        #bol(f'Welcome back......{name} hope you are doing great')
        print('\n>>> Total consultation made',total_visit)
        #bol(f'you have made {total_visit} follow up till now...')
        #time.sleep(0.5)
        print('\n>>> Do you want previous consultation report..? (y/n): ')
        #bol('would you like to glance at your  previous reports?.... ')
        m=y_n("<<<  ")
        if m=='y' or m=="Y":
            for i in x:
                y.append(i['date'])
            print (" {:<3} {:<3} {:<10} ".format('\nSr.',':','Date'))
            for i in range(len(y)):
                print (" {:<3} {:<3} {:<10} ".format(i+1,':',y[i]))
            #bol('this is the list of date on which you had follow up')
            #time.sleep(0.5)
            print('\n>>> Which previous consultation report you wanna see...?')
            #bol('Which previous consultation report you wanna see...?')
            #bol("please enter respect date's serial number...")
            print(('>>> Enter consultation number : '))
            rep=Ex_cept("<<<  ")
            #time.sleep(0.5)
            print('\n-----Previous Report 📑-------')
            for key,value in (x[rep-1].items()):      
                    print (" {:<10} {:3} {:<10} ".format(key,':',value))
            print('----------------------------')
            #bol('this is your previous report of follow up made on...')
            #bol(y[rep-1])
        #time.sleep(0.5)
        print('\n>>> Okay,... lets start with procedure ✌')
        #bol('okay,... lets start with procedure')
        #bol('please answer the following questions,..... so that i can re examine you....')
    else: #if patient is not registered
        if choice==1:
            pass
        else:
            print('\n>>> Ooops Patient not found!!! 😬')
            print('\n>>> Please register 😄')
            #bol('ooops ,... patient Not Found...... please register again')
        name,age=patient_info(choice,name)

    #time.sleep(1)
    print('\n>>> Do you feel dry cough 🤧? (y/n) : ')
    #bol('Do you feel dry cough?')
    cough =y_n("<<<  ")
    print('\n>>> Do you have fever 🤒? (y/n) : ')
    #bol('Do you have fever?')
    fever =y_n("<<<  ")
    print('\n>>> Do you feel tired at all 🥱? (y/n) : ')
    #bol('Do you feel tired at all?')
    tired =y_n("<<<  ")
    print('\n>>> Do you have difficulty in breathing 😷? (y/n) : ')
    #bol('Do you have difficulty in breathing?')
    breath =y_n("<<<  ")
    #time.sleep(0.5)
    #bol('Thank you , for providing relavent information')
    q=Patient(d2,name,age,cough,fever,tired,breath)
    q.report()
    l.append(vars(q))
    for data in l:
        with open('covidata.csv','a') as file:
            writer=csv.writer(file)
            writer.writerow([data['date'],data['name'],data['age'],data['cough'],data['fever'],data['tired'],data['breath']])
    return name,age,cough,fever,tired,breath

def examine(name,age,cough,fever,tired,breath): #function to examine and conclusion
        if cough=='y'and fever=='y' and tired=='y' and breath=='y' or cough=='Y' or fever=='Y' or tired=='Y' or breath=='Y':
            #time.sleep(1)
            print("\n>>> hmmm...🤥\n    Don't engage wit people 🤝.\n    Contact your Doctor 👨‍⚕️.\n    Please call 📱 : 001-23978046 \n    And follow  some steps to avoid spreading it.")
            #bol("hmmm... Don't engage wit people... Contact your Doctor..   please call  001-23978046   And follow  some steps to avoid spreading it.")
        elif cough=='n'and fever=='n' and tired=='n' and breath=='n' or cough=='N'or fever=='N' or tired=='N' or breath=='N':
            #time.sleep(1)
            print('\n>>> Pick up a pillow and jump to bed 🛏💃.\n    No one is gonna harm you 😎💪.\n    Follow some steps to avoid getting it...')
            #bol('Pick up a pillow and jump to bed  No one is gonna harm you   Follow some steps to avoid getting it...')
        else:
            #time.sleep(1)
            print("\n>>> Okay, Don't  worry it's normal",name, '\n    Take care of yourself And follow following steps:')
            #bol("Okay, Don't  worry it's normal ")
            #bol(name)
            #bol('>>> Take care of yourself .... And follow following steps...')
            #time.sleep(0.5)
            print("\n>>> You can protect yourself and help prevent spreading the virus to others if you: ")
            #bol('You can protect yourself  and help prevent spreading the virus to others  if you:')
            #time.sleep(0.5)
            print('\n>>> Do:    \n    Wash your hands regularly for 20 seconds, with soap and water 🧼💦 \n    or alcohol-based hand rub  ')
            #bol("Do:  Wash your hands regularly for 20 seconds, with soap and water alcohol-based hand rub ")
            #time.sleep(0.5)
            print("\n>>> Wear mask when you are outside. 😷")
            #bol("Wear mask when you are outside.")
            #time.sleep(0.5)
            print('\n>>> Cover your nose and mouth with a dispossable tissue of flexxed elbow \n    when you cough or sneeze 🤧')
            #bol("Cover your nose and mouth with a dispossable tissue of flexxed elbow  when you cough or sneeze")
            #time.sleep(0.5)
            print("\n>>> Avoid close contact (1 meter or 3 feets )   with people who are unwell 🤮 ")
            #bol("Avoid close contact 1 meter or 3 feets with people who are unwell ")
            #time.sleep(0.5)
            print("\n>>> Stay home and self-isolate from others in the household if you feel unwell 🏠 ")
            #bol("Stay home and self-isolate from others  in the household if you feel unwell")
            #time.sleep(0.5)
            print("\n>>> Don't \n   Touch your eyes, nose, or mouth if your hands are not clean.")
            #bol("Don't")
            #bol("Touch your eyes, nose, or mouth if your hands are not clean.")
        print('\n>>> Thankyou for choosing me for examining yourself 😊')
        #bol('Thankyou for choosing me for examining yourself')
        print('\n>>> Stay Safe. Stay Healthy, \n    See you soon...😉',name)
        #bol(f' Stay Safe. Stay Healthy, See you soon...{name}')
        
def welcome(l):  #function welcome and menu 
    print('\n >>> Menu:')
    print('1.-> New User.')
    print('2.-> Follow up.')
    print('3.-> Exit')
    #bol('please select one option')
    #bol('press 1 ,to make new consultation')
    #bol('press 2 , to take follow up')
    #bol('press 3 , if you want to exit')
    print('\n>>> Enter choice: ')
    choice=Ex_cept("<<<  ")
    if choice==1:
        #bol('welcome to covi doc, i am  doc assist......')
        #bol('before going further please introduce yourself by giving answer of some questions....')
        name,age,cough,fever,tired,breath=patient_R_NR(choice,l)
    elif choice==2:
        #bol('welcome to covi doc, i am  doc assist......')
        name,age,cough,fever,tired,breath=patient_R_NR(choice,l)
    else:
       return choice
    examine(name,age,cough,fever,tired,breath)

def authentication(): #function for security authentication
    auth_count=3    #no. of login chances
    u_n,pwd=username.user() #security function 
    while auth_count>0: #loop for 3 chances of validation
        #bol('Please enter Username And ,Password')
        credential=input("\nUsername : " ) #input username
        auth=stdiomask.getpass('Password : ') #input password
        if credential==u_n and auth == pwd: #authentication
            print(' >>> Login Successfull... 😃')
            #bol('Login Successfull...')
            #time.sleep(0.5)
            print('\n>>> Note:  The following Program is assistant doctor so dont  worry, the result will be 100% acurate, lets get started .....')
            #bol('Note: The following Program is assistant doctor so dont worry, the result will be 100% acurate, lets get started .....')
            #time.sleep(0.5)
            print('\n*********************************************** Welcome to CoviDOC ********************************************************')
            #bol('Welcome To Covi Doc')
            while True: #loop for carring out multiple operations
                l=[] #list for storing dictionary of patient's details  it is used in entering data in csv file
                choice=welcome(l) #calling welcome function
                if choice==3: #for exiting
                    print('\n>>> Bye Bye 🖐')
                    #bol('Bye Bye')
                    break
                else: #for new consultation or follow up
                    print('\n*********************************************************************************************************************')
                    print('\n>>> Do you want to consult again? (y/n)')
                    #bol('Do you want to consult again?....')
                    con=y_n("<<<  ")
                    if con=='y'or con=='Y':
                        pass
                    else:
                        print('\n>>> Bye Bye 🖐')
                        #bol('Bye Bye')
                        break
            break
        else: #for incorrect username or pswrd 
            print(' >>> Invalid User 🤨')
            #bol('ooops, invalid user....')
            auth_count-=1
            if auth_count>0:
                print("\n>>> Please try again")
                #bol(">>> Please try again")
                if auth_count<2:
                    print(' >>> You have only ',auth_count,' attempt left!!!😣')
                    #bol(f'You have only {auth_count} attempt left!!!')
                else:
                    print(' >>> You have only ',auth_count,' attempts left!!!😣')
                    #bol(f'You have only {auth_count} attempts left!!!')

            else:  #after 3 attempts
                print(' >>> Access denied 😶')
                #bol('Access Denied')

#main function
if __name__ =='__main__': 
    authentication()


