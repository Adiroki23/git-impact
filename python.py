from os import system, name
from time import sleep


userbal = 50000
transactions = {}

# def Admin():
#     resof100 = 10000
#     resof500 = 2000
#     resof200 = 5000

def clear():
    # for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')
    

def showbal():
    clear()
    print('User: Someone 01')
    print('\nUser balamce is: ',userbal)
    sleep(1.9)
    clear()
    
def deposit(d):
    global userbal
    clear()
    userbal += d
    print()
    print(d, 'deposited successfully')
    transactions[i] = d
    sleep(0.8)
    
def withdraw(w):
    global userbal
    userbal -= w
    print(w, '\nprocessing...')
    sleep(0.6)
    clear()
    print()
    print()
    countn(w)
    transactions[i] = -w
    sleep(1.9)
    
def countn(w):
    if w>10000:
        n5 = w//500 
        n2 = (w-n5*500)//200
        n1 = (w-n5*500-n2*200)//100
        print('amount withdrawn:',w,'\n')
        sleep(0.4)
        print(n5,'500s,')
        if n2!=0:
            sleep(0.2)
            print(n2,'200s,')
        if n1!=0:
            sleep(0.2)
            print(n1,'100s,')
            
    if w<10000 and w>5000:
        n5 = (w-w/5)//500
        n2 = (w/10)//200
        n1 = (w/10)//100
        rem = w-(500*n5)-(200*n2)-(100*n1)
        remn2 = rem//200
        remn1 = (rem-remn2*200)//100
        
        print('amount withdrawn:',w,'\n')
        sleep(0.4)
        print(n5,'500s,')
        if n2!=0:
            sleep(0.2)
            print(n2+remn2,'200s,')
        if n1!=0:
            sleep(0.2)
            print(n1+remn1,'100s,')
            
    if w<5000:
        n5 = (w/2)//500
        n2 = (w/4)//200
        n1 = (w/4)//100
        rem = w-(500*n5)-(200*n2)-(100*n1)
        remn2 = rem//200
        remn1 = (rem-remn2*200)//100
        
        print('amount withdrawn:',w,'\n')
        sleep(0.4)
        print(n5,'500s,')
        if n2!=0:
            sleep(0.2)
            print(n2+remn2,'200s,')
        if n1!=0:
            sleep(0.2)
            print(n1+remn1,'100s,')
            
            
def stmt():
    clear()
    sleep(0.2)
    print('\nStatement\n')
    # print(transactions)
    for i in transactions:
        print(transactions[i])
        sleep(0.2)
    sleep(2)
    clear()
           
i=0
t= True

while True:
    
    i+=1  
    clear()
    print('User: Someone 01 ')
    sleep(0.2)
    print('\nCheck Balance (1)')
    sleep(0.1)
    print('Deposit       (2)')
    sleep(0.1)
    print('Withdraw      (3)')
    sleep(0.1)
    print('Statement     (4)')
    sleep(0.2)
    opt = int(input('\nOption: '))    
    clear()
    
    if opt==1:
        showbal()

    if opt==2:
        sleep(0.2)
        print('DEPOSIT FUNDS')
        while True:
            sleep(0.2)
            if t:
                d = int(input('\nEnter amount: '))
            else:
                print('\nuse amount in 100s')
                sleep(0.2)
                d = int(input('Enter amount again: '))
            
            if d%100==0:
                deposit(d)
                t=True
                break
            else:
                print('!! Invalid input')
                t=False
                continue
        
    if opt==3:
        sleep(0.2)
        print('WITHDRAW FUNDS')
        while True:
            sleep(0.2)
            if t:
                w = int(input('\nEnter amount: '))
            elif w>userbal:
                
                w = int(input('\nEnter sufficient amount: '))
            else:
                print('\nuse amount in 100s')
                sleep(0.2)
                w = int(input('Enter amount again: '))
            
            if w%100==0 and w<=userbal:
                withdraw(w)
                t=True
                break
            
            else:
                print('!! amount invalid')
                t=False
                continue
    
    if opt==4:
        stmt()
    
    #written by Shivam