contacts = {
    "stu1" : {
        "name1" : "samaira",
        "phone1" : 9871171628,
        "email1" : "sam@gmail.com"
        },
    
    "stu2" : {
        "name2" : "aryan",
        "phone2" : 9667797856,
        "email2" : "aryan@gmail.com"
        }
    }

contacts["stu3"] = {
    "name" : "khushi",
    "phone3" : 9872663309,
    "email3": "khushi@gmail.com"
    }


def add():
    print("enter new contact's name:")
    new_name = input()
    print("enter new contact's number:")
    new_phone = int(input())
    print("enter new contact's email:")
    new_email = input()
    return new_name, new_phone, new_email

add()

#def update_contact():

def printContacts():
    print(contacts)
    
printContacts() 

def search():
    print("enter n=1 to search by number and n=0 to search by email \n")
    print("n : ")
    n = int(input())
    if(n==0):
        contacts.find(9871171628)
