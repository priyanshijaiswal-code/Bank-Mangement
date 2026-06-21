import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")

    except Exception as err:
        print(f"An exception error occured as {err}")  

    @classmethod
    def __update(cls):
            with open(cls.database,'w') as fs:
                fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
            alpha =random.choices(string.ascii_letters,k=3)
            num = random.choices(string.digits,k=3)
            spchar =random.choices("@#$^*&*&",k=1)
            id = alpha + num + spchar
            random.shuffle(id)
            return "".join(id)        

    def createaccount(self):
        info =  {
            "name" : input("Tell your name :-"),
            "age" : int(input("Tell your age:-")),
            "email" : input("Tell your email:-"),
            "pin" : int(input("Tell your 4 digit pin  :-")),
            "AccountNo." : Bank.__accountgenerate(),
            "balance" : 0 
        }
        if info['age']  < 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("Your Account has been created")
            for i in info:
                print(f"{i} :{info[i]}")
            print("please note down your account number ")    

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin as well "))
            
        userdata = [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("how much you want to deposit "))
            if amount > 100000 or amount < 0:
                print("Sorry!! The amount is to much you can deposit below 100000 and above 0")

            else:
                userdata[0]['balance'] += amount      
                Bank.__update()
                print("Amount deposited successfully ")    


    def withdrawmoney(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("soory no data found")
        
        else:
            amount = int(input("how much you want to withdraw "))
            if userdata[0]['balance']  < amount:
                print("soory you dont have that much money")
              
            else:
                
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully ")            
    def showdetails(self):

        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]
        print("your information are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}") 

    def updatedetails(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No such user found")
        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")
        
            newdata = {
                    "name": input("please tell new name or press enter : "),
                    "email":input("please tell your new Email or press enter to skip :"),
                    "pin": input("enter new Pin or press enter to skip: ")
                }
        
            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']   

            newdata['AccountNo.'] = userdata[0]['AccountNo.']
            newdata['balance'] = userdata[0]['balance']
            

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                     continue
                else:
                   userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")


    def  Delete(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry!! no such data exist")
        else:
            check = input("Press y if you want to actually delete your data or press n ")
            if check == 'n' or check == "N":
                print("bypassed") 
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted succesfully")
                Bank.__update()
        

          
                

user = Bank()
print("Press 1 for creating an Account")
print("Press 2 for deposting the money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting your Account")

check = int(input("Tell your response:-"))

if check == 1:
    user.createaccount()
if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetails()    
if check == 5:
    user.updatedetails()    
if check == 6:
    user.Delete()    