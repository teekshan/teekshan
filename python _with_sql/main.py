from dbhelper import DBhelper

def main():
    db = DBhelper()
    while True:
        print("*****************WELCOME*******************")
        print()
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit the program")
        try:
            choice = int(input())
            if (choice==1):
                #insert user
                uid = int(input("enter user id: "))
                user_nm = input("enter user name: ")
                user_no = int(input("enter user number: "))
                db.insert_user(user_nm,uid,user_no)
                
            elif (choice==2):
                db.fetch_all(5) #display all or some
            elif(choice==3):
                userid = int(input("enter carefully the user you want to delete: "))
                
                db.delete_user(userid)#deleting user
            elif(choice==4):
                userid = int(input("enter user id you want to update of : "))
                new_user_id = int(input("new user  id you want to change to : "))
                new_name = input("new name you want to add: ")
                new_roll_no = int(input("new roll number you want to give: "))
                db.update_user(userid,new_user_id,new_name,new_roll_no) #update user
            elif(choice==5):
                break
            else:
                print("invalid input try again")
            
        except Exception as e:
            print(e)
            print("invalid input try again")
            
if __name__=="__main__":
    main()
