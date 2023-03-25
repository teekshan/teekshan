import mysql.connector as sql

class DBhelper():
    def __init__(self):
        self.con = sql.connect(host="localhost", port=3306 ,user="root", password= "root",database='new1')
        
        query = 'create table if not exists test_table(userid int primary key, name varchar(20), roll_no int(20))' #command
        
        #making cursor
        
        cur = self.con.cursor()
        cur.execute(query)
        print("created")
        
    #insert 
    def insert_user(self,Name,userId,Roll_no):
        query = "insert into test_table(userid,name,roll_no) values({}, '{}', {})".format(userId,Name,Roll_no)
        print(query)
        
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        
        print("user saved to db")
        
     
        
#main code
# helper = DBhelper()
# helper.insert_user("manan",2,200)
# helper.insert_user("truce",4,199)
# helper.insert_user("trip",5,199)
# helper.insert_user("deepak",6,199)
# helper.insert_user("ousama",14,199)
# helper.insert_user("mannat",13,199)
# helper.insert_user("harsh",12,199)
# helper.insert_user("navdeep",11,199)
# helper.insert_user("arvind",10,19)

    def fetch_all(self,userId):
        query = f"select * from test_table" #to print all
        # f"select * from test_table where userid={userId}" to print the only selected row 
        cur = self.con.cursor(buffered=True)
        cur.execute(query)
        self.con.commit()
        #traversing using row
        for row in cur:
            print("User Id: ", row[0])
            print("Name of student : ", row[1])
            print("Roll Number: ", row[2])
            print()
            print()
            
            
        
#deleting the user
    def delete_user(self,userId):
        query = f"delete from test_table where userid={userId}"
        #to check query
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        
        #updating the user
    def update_user(self,userId,new_user_id,new_name,new_roll_no):
        query = f"update test_table set userid={new_user_id}, name = '{new_name}', roll_no ={new_roll_no} where userid={userId}"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        #assignment 
        #add code to show what val you updated
        #any one of the val if possible all of them