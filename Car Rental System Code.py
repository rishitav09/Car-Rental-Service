from feedback import modulefeedback
import csv
import mysql.connector
from tabulate import tabulate
import datetime
h1=["Car Registration No.","Make","Model","Available"]
l1=[["A0002","Honda","F567W2","No"],
    ["A0003","Honda","X2319Y","Yes"],
    ["A0004","Honda","A67512","No"],
    ["A0005","Honda","B67S23","No"],
    ["A0006","Honda","MN67S2","Yes"],]
with open("list1.csv","w",newline="")as c1:
    w=csv.writer(c1)
    w.writerow(h1)
    w.writerows(l1)
    c1.close()

h2=["Customer ID","Customer Name","Address","Mobile No."]   
l2=[["C0001","ABC","Dubai","231342"],
     ["C0002","ABC","Sharjah","893412"],
     ["C0003","PQR","Abu Dhabi","764534"],
     ["C0004","EFG","Ajman","986713"]]
with open("list2.csv","w",newline="")as c2:
    w=csv.writer(c2)
    w.writerow(h2)
    w.writerows(l2)
    c2.close()

    
h4=["Car ID","Customer ID","Return Date","Duration"]
l4=[["A0004","C0004","27-03-2022","12"],
    ["A0002","C0002","30-03-2022","24"]]
with open("list4.csv","w",newline="")as c4:
    w=csv.writer(c4)
    w.writerow(h4)
    w.writerows(l4)
    c4.close()
 
while True:
    print()
    print("1.CAR REGISTRATION-COMPANY LOGS")
    print("2.COSTOMER DETAILS-COMPANY LOGS")
    print("3.FORM FOR RENTING CARS")
    print("4.RENTED CAR RETURNING LOGS")
    print("5.CARS FOR SALE(DATABASE)")
    print("0.EXIT")
    print()
    c=eval(input("ENTER YOUR CHOICE: "))
    print()
    x=0
    f=0
    loc1=0
    loc2=0
    loc3=0
    g=0
    s=0
    no=0
    make=0
    model=0
    available=0
    nno=0
    nmake=0
    nmodel=0
    navailable=0
    y=0
    i=0
    name=0
    address=0
    mobile=0
    carid=0
    customerid=0
    fee=0
    date=0
    duedate=0
    telephone=0
    email=0
    name1=0
    no1=0
    name1=0
    telephone1=0
    telephone2=0
    email1=0
    name2=0
    no2=0
    mobile2=0
    email2=0
    choice1=0
    choice2=0
    message=0
    if c==1:
        print("CAR REGISTRATION-COMPANY LOGS")
        print()

#here
        with open ("list1.csv","r") as c5:
            r=csv.reader(c5)
            for item in r:
                print(" ",item[0]," "*(19-len(item[0]))," ",item[1]," "*(3-len(item[1]))," ",item[2]," "*(5-len(item[2]))," ",item[3]," "*(9-len(item[3]))," ")
                

        while True:
            print("a.To add a new car to the list")
            print("b.To update existing details of the selected car in the list")
            print("c.To delete a car from the list")
            print("d.Exit")
            print()
            x=input("Enter your choice:")
            print()
            if x=="a":
                no=input("Enter Car Registration Number:")
                make=input("Enter car company:")
                model=input("Enter car model:")
                available="Yes"
                ll1=[no,make,model,available]

                with open("list1.csv","a") as c6:
                    w=csv.writer(c6)
                    w.writerow(ll1)
                    c6.close()

                with open ("list1.csv","r") as c7:
                    r=csv.reader(c7)
                    for item in r:
                        if item!=[]:
                            print(" ",item[0]," "*(19-len(item[0]))," ",item[1]," "*(3-len(item[1]))," ",item[2]," "*(5-len(item[2]))," ",item[3]," "*(9-len(item[3]))," ")
                        
                    
                print("Successfully saved")
                print()
            elif x=="b":
                import os
                g=input("Enter existing Car ID:")
                with open("list1.csv","r") as c8:
                    r=csv.reader(c8,delimiter=",")
                    l=list(r)
                    print(l)
                    with open("nlist1.csv","w",newline="") as c9:
                        w=csv.writer(c9)
                        line=0
                        for i in range(len(l)-1):
                            if l[i][0]==g and line!=0:
                                nno=input("Enter new Car Registration Number:")
                                nmake=input("Enter new car company:")
                                nmodel=input("Enter new car model:")
                                navailable=input("Enter car availabilty:")
                                l[i][0]=nno
                                l[i][1]=nmake
                                l[i][2]=nmodel
                                l[i][3]=navailable
                            w.writerow(l[i])
                            line+=1
                os.remove("list1.csv")
                os.rename("nlist1.csv","list1.csv")
                with open("list1.csv","r") as c10:
                    r=csv.reader(c10)
                    for item in r:
                        print(" ",item[0]," "*(19-len(item[0]))," ",item[1]," "*(3-len(item[1]))," ",item[2]," "*(5-len(item[2]))," ",item[3]," "*(9-len(item[3]))," ")
                print("Edited Successfully")
                print()



            elif x=="c":
                import os
                f=input("Enter Car ID to be deleted:")
                with open ("list11.csv","w",newline="") as c11:
                    w=csv.writer(c11)
                    with open("list1.csv","r") as c12:
                        r=csv.reader(c12)
                        l=[]
                        for item in r:
                            if item[0]!=f:
                                
                                l.append(item)
                    w.writerows(l)
                os.remove("list1.csv")
                os.rename("list11.csv","list1.csv")
                with open("list1.csv","r") as c21:
                    r=csv.reader(c21)
                    for item in r:
                        print(" ",item[0]," "*(19-len(item[0]))," ",item[1]," "*(3-len(item[1]))," ",item[2]," "*(5-len(item[2]))," ",item[3]," "*(9-len(item[3]))," ")
                print("Deleted successfully")
                print()
            else:
                break




    elif c==2:
        print("CUSTOMER DETAILS-COMPANY LOGS")
        print()
        
        with open ("list2.csv","r") as c13:
            r=csv.reader(c13)
            for item in r:
                print(" ",item[0]," "*(11-len(item[0]))," ",item[1]," "*(13-len(item[1]))," ",item[2]," "*(9-len(item[2]))," ",item[3]," "*(10-len(item[3]))," ")

        print("YOU CAN ADD DETAILS OF NEW CUSTOMER HERE")
        print()
        i=input("Enter Customer ID:")
        name=input("Enter Customer Name:")
        address=input("Enter address:")
        mobile=input("Enter mobile no:")
        ll2=[i,name,address,mobile]

        with open("list2.csv","a") as c14:
            w=csv.writer(c14)
            w.writerow(ll2)
            c14.close()

        with open ("list2.csv","r") as c15:
            r=csv.reader(c15)
            for item in r:
                if item!=[]:
                    print(" ",item[0]," "*(11-len(item[0]))," ",item[1]," "*(13-len(item[1]))," ",item[2]," "*(9-len(item[2]))," ",item[3]," "*(10-len(item[3]))," ")
            
        print("Added Successfully")
        print()

    elif c==3:
        print("""OUR CONDITIONS:-

                       1.You will only pay when you pick up your car.
                       2.Payment can be made by credit card with an authorization to debit future rentals, traffic fines etc.
                       3.Payment can also be made by cheque, bank transfer, corporate credit card,etc.
                       4.All customers are required to maintain a valid credit card on file at all times, failure of which may result in the termination of the contract).
                       5.If the car is not returned on time, then a fine of Dhs.100 will be charged per day.
                       6.Cancellations and modification of your online booking can be made up to 2 day before the pick-up date.
                       7.All drivers must be a minimum of 25 years of age.
                       8.Drivers on a visit visa must have a valid international license issued by the country of origin along with their national license.
                       9.Drivers on a UAE resident visa must have a valid UAE driving license that is a minimum 6 months old.
                       10.In case the specific make or model or color of vehicle you selected is not available on the pickup day, you will be provided an equivalent car.
                       11.Smoking in our vehicles may result in a charge of up to AED 1000.
                       12.Off-roading, rallying, racing or ‘drifting’ in our vehicles is strictly prohibited.
                       13.Driving through and parking the vehicle in standing water should be avoided as this can cause major damage to the engine.
                       14.Damages caused by such activities will not be covered by insurance and will be borne by you in full""")
        print()
        print("DOCUMENTS REQUIRED:-")
        print()
        l3=[["Passport face and visa page","Pssport face and visa page"],
            ["Credit card to be used for payment","Credit card to be used for payment"],
            ["UAE driver’s license of the user in JPEG format","Home-country driver’s license along with an international driver’s permit"],
            ["Emirates ID (front & back)","Photo of the entry stamp in the passport"],
            ["Proof of Residential Address","-"]]
        print(" UAE Residents(resident or student visas                    Tourists(those on a tourist visa)                  ")
        print()
        for item in l3:
            print(" ",item[0]," "*(60-len(item[0]))," ",item[1]," "*(30-len(item[1]))," ")
        print()
        print("You may securely upload the above documents and fill the customer profile form on our website by logging in to www.carrental.ae/profileform")
        print()
        carid=input("Enter Car ID: ")
        customerid=input("Enter customer ID: ")
        with open("list1.csv","r") as c16:
            r=csv.reader(c16,delimiter=",")
            k=list(r)
            ans1="no"
            for i in range(len(k)):
                if k[i][0]==carid and k[i][3]=="Yes":
                    ans1="yes"
                    break
            if ans1=="no":
                print("Car not found")
        with open("list2.csv","r") as c17:
            r=csv.reader(c17,delimiter=",")
            k=list(r)
            ans2="no"
            for i in range(len(k)):
                if k[i][0]==customerid:
                    ans2="yes"
                    break
            if ans2=="no":
                print("Customer not found")
        if ans1=="yes" and ans2=="yes":
            date=input("Enter date of return(dd/mm/yy):")
            day,month,year=date.split("/")
            validity=True
            try:
                datetime.datetime(int(year),int(month),int(day))
            except ValueError:
                validity=False
            if validity==True:
                days=input("Enter Rent duration:")
                with open("list4.csv","a") as c18:
                    w=csv.writer(c18)
                    w.writerow([carid,customerid,date,days])
                    c18.close()
                with open("list4.csv","r") as c19:
                    r=csv.reader(c19,delimiter=",")
                    k=list(r)
                    for i in k:
                        if i!=[]:
                            print(i)
            else:
                print("Input date is not valid....")
        
        print()

        
    elif c==4:

        with open ("list4.csv","r") as c20:
            r=csv.reader(c20)
            for i in r:
                print(i)

        with open ("list4.csv","r") as c21:
            r=csv.reader(c21)
            k=list(r)
            carid=input("Enter Car ID:")
            for item in k:
                if item[0]==carid:
                    date=item[2]
                    duration=item[3]
                    fees=int(duration)*100
                    print("Date:",date)
                    print("Duration:",duration)
                    print("Fees:",fees)
                    print()
                    print()
                    pos=k.index(item)
                    k.pop(pos)
                    for i in k:
                        print(i)
                    break
            else:
                print("Car not found")
    elif c==5:
        database=input("Enter name of your database:")
        obj=mysql.connector.connect(host="localhost",user="root",password="41723")
        c=obj.cursor()
        q="create database if not exists %s"%(database,)
        c.execute(q)
        print("Database created successfully...")
        c=obj.cursor()
        c.execute("USE "+database)
        tablename=input("Enter the name of table to be created:")
        q="CREATE TABLE IF NOT EXISTS "+tablename+"(RegNo int primary key, CarEngine varchar(20), CarName varchar(20), CarModel varchar(20), Price float)"
        print("Table "+tablename+" created successfully...")
        c.execute(q)
        print()
        print()
        while True:
            print("1.Adding vehicle records")
            print("2.View all car records")
            print("3.Modification of a record")
            print("4.For deleting the record of a paticular vehicle")
            print("5.Purchase a car")
            print("6.Exit")
            choice=eval(input("Enter your choice:"))
            print()
            print()
            if choice==1:
                print("Enter the following details...")
                regno=input("Enter Car Registration Number:")
                engine=input("Enter Car Engine No.:")
                name=input("Enter Car Name:")
                model=input("Enter Car Model:")
                price=eval(input("Enter Price:"))
                record=(regno,engine,name,model,price)
                q="INSERT INTO "+tablename+" VALUES(%s,%s,%s,%s,%s)"
                c.execute(q,record)
                obj.commit()
                print("Record added successfully...")
                print("-"*100)
            elif choice==2:
                try:
                    q="SELECT * FROM "+tablename
                    c.execute(q)
                    print(tabulate(c,headers=["Car Registration No.","Car Engine No.","Car Name","Car Model","Price"]))
                    l=c.fetchall()
                    for i in l:
                        print(i)
                except:
                    print("ERROR")
                print("-"*100)
            elif choice==3:
                regno=input("Enter Car registration No.of the record to be modified:")
                q="SELECT * FROM "+tablename+" WHERE REGNO="+regno
                c.execute(q)
                l=c.fetchone()
                count=c.rowcount
                if count==-1:
                    print("Vehicle ",regno," does not exist in record...")
                    print("-"*100)
                else:
                    print("Engine No:",l[1])
                    print("Name:",l[2])
                    print("Model:",l[3])
                    print("Price:",l[4])
                    print()
                    print()
                    print("Enter value to be modified...")
                    ch=input("Do you want to modify Car Engine No.(y/n)?")
                    if ch=="y":
                        x=input("Enter Car Engine No:")
                        engine=x
                    else:
                        engine=l[1]
                    ch=input("Do you want to modify Car Name?(y/n)")
                    if ch=="y":
                        x=input("Enter Car Name:")
                        name=x
                    else:
                        name=l[2]
                    ch=input("Do you want to modify Car Model?(y/n)")
                    if ch=="y":
                        x=input("Enter Car Model:")
                        model=x
                    else:
                        model=l[3]
                    ch=input("Do you want to modify Car Price?(y/n)")
                    if ch=="y":
                        x=eval(input("Enter Car Price:"))
                        price=x
                    else:
                        price=l[4]
                    r=(engine,name,model,price,regno)
                    q="UPDATE "+tablename+" SET CarEngine=%s,CarName=%s,CarModel=%s,Price=%s WHERE RegNo=%s"
                    c.execute(q,r)
                    obj.commit()
                    print("Record updated successfully...")
                    print("-"*100)
            elif choice==4:
                regno=input("Enter Car Registration Number to be deleted:")
                q="DELETE FROM "+tablename+" WHERE RegNo="+regno
                c.execute(q)
                obj.commit()
                count=c.rowcount
                if count>0:
                    print("Record deleted successfully...")
                else:
                    print("Car not found in records...")
            elif choice==5:
                q="SELECT CarName, CarModel FROM "+tablename
                c.execute(q)
                print(tabulate(c,headers=["Car Name","Car Model"]))
                l=c.fetchall()
                for i in l:
                    print(i)
                print()
                print()
                
                name=input("Enter name of car you want to purchase from the above:")
                model=input("Enter car model you want to purchase from the above:")
                r=(name,model)
                q="select * from "+tablename+" where carname=%s and carmodel=%s"
                c.execute(q,r)
                now=datetime.datetime.now()
                print("\n\n\n\t\t\tReceipt ")
                print("Current Date and Time:",end=" ")
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
                print(tabulate(c,headers=["Car Registration No.","Car Engine No.","Car Name","Car Model","Price"]))
                print()
                print("Thank you for purchasing".center(90))
                print()
                q="DELETE FROM "+tablename+" WHERE carname=%s and carmodel=%s"
                c.execute(q,r)
            else:
                break
    else:
        break
print()
print()
print("*******************************************************FEEDBACK******************************************************************")
modulefeedback.feedback()
print("**********************************************THANK YOU FOR YOUR FEEDBACK********************************************************")
 
    
                
            
