import mysql.connector
from datetime import date
mycon=mysql.connector.connect(host='localhost',user='root',password='dontreadthis1',database='banking')
mycursor=mycon.cursor()

def create():
    name=input('Enter your name: ')
    dob=input('Enter the your date of birth in yyyy-mm-dd format: ')
    while True:
        if int(str(date.today())[0:4])-int(dob[0:4])<18:
            print('Must be above the age of 18')
            break
        else:
            telno=int(input('Enter your telephone number: '))
            if len(str(telno))!=8:
                print('Invalid telephone number')
                print('Please re-enter your telephone number')
                telno=int(input('Enter your telephone number: '))
            else:
                passwd=input('Enter a password for your account: ')
                print('Creating an account with the given details')
                mycursor.execute('select max(accno) from acc')
                mydata=mycursor.fetchall()            
                accno=mydata[0][0]+1
                print('Your Account No is: ',accno)
                cmd="insert into acc(accno,name,dob,telno,passwd) values(%s,'%s','%s',%s,'%s')"%(accno,name,dob,telno,passwd)
                mycursor.execute(cmd)
                mycon.commit()
                dep=int(input('Enter your intial deposit: '))
                if dep<100:
                    print('Minimum deposit amount 100')
                    dep=100
                elif dep>500000:
                    print('Maximum deposit is 500000')
                    dep=500000  
                tt='d'
                cmd="insert into transac(accno,transtype,dot,transamt,balance) values(%s,'%s','%s',%s,%s)"%(accno,tt,date.today(),dep,dep)
                mycursor.execute(cmd)
                mycon.commit()
                print('Thank you for using our service')
                break
def deposit():
    while True:
        accno=int(input('Enter your account number: '))
        mycursor.execute('select * from acc where accno={}'.format(accno))
        mydata=mycursor.fetchall()
        if mycursor.rowcount!=0:
            passwd=input('Enter your password: ')
            if mydata[0][-1]==passwd:
                dep=int(input('Enter the amount you would like to deposit: '))
                tt='d'
                if dep>500000:
                    print('Maximum deposit exceeded')
                    dep=500000
                mycursor.execute('select * from transac where accno={}'.format(accno))
                mydata=mycursor.fetchall()
                balance=mydata[-1][-1]
                cmd="insert into transac(accno,transtype,dot,transamt,balance) values(%s,'%s','%s',%s,%s)"%(accno,tt,date.today(),dep,balance+dep)
                mycursor.execute(cmd)
                mycon.commit()
                print('Transaction complete')
                break
            else:
                print('Incorrect Password')
                break
        else:
            print('Invalid account no')
            break
def withdraw():
    while True:
        accno=int(input('Enter your account number: '))
        mycursor.execute('select * from acc where accno={}'.format(accno))
        mydata=mycursor.fetchall()
        if mycursor.rowcount!=0:
            passwd=input('Enter your password: ')
            if mydata[0][-1]==passwd:
                wit=int(input('Enter the amount you would like to withdraw (not more than 500000): '))
                tt='w'
                if wit>500000:
                    print('Max withdraw is 500000')
                    wit=500000
                mycursor.execute('select * from transac where accno={}'.format(accno))
                mydata=mycursor.fetchall()
                balance=mydata[-1][-1]
                if wit>balance:
                    print('Withdrawal amount is higher than balance')
                    break
                else:
                    cmd="insert into transac(accno,transtype,dot,transamt,balance) values(%s,'%s','%s',%s,%s)"%(accno,tt,date.today(),wit,balance-wit)
                    mycursor.execute(cmd)
                    mycon.commit()
                print('Transaction complete')
                break
            else:
                print('Incorrect Password')
                break
        else:
            print('Invalid account no')
            break
def display():
    accno=int(input('Enter your account number: '))
    mycursor.execute('select * from acc where accno={}'.format(accno))
    mydata=mycursor.fetchall()
    if mycursor.rowcount!=0:
        passwd=input('Enter your password: ')
        if mydata[0][-1]==passwd:
            print()
            print('Name: ', mydata[0][1])
            print('Date of Birth: ',mydata[0][2])
            print('Telephone No: ',mydata[0][3])
            mycursor.execute('select * from transac where accno={}'.format(accno))
            mydata=mycursor.fetchall()
            print('Balance: ',mydata[-1][-1])
        else:
            print('Incorrect Password')
    else:
        print('Invalid account no')
def terminate():
    accno=int(input('Enter your account number: '))
    mycursor.execute('select * from acc where accno={}'.format(accno))
    mydata=mycursor.fetchall()
    if mycursor.rowcount!=0:
        passwd=input('Enter your password: ')
        if mydata[0][-1]==passwd:
            mycursor.execute('delete from acc where accno={}'.format(accno))
            mycon.commit()
            mycursor.execute('delete from transac where accno={}'.format(accno))
            mycon.commit()
            print("Account terminated")
        else:
            print('Incorrect Password')
    else:
        print('Invalid account no')
def transfer():
    while True:
        accno1=int(input('Enter your account number: '))
        mycursor.execute('select * from acc where accno={}'.format(accno1))
        mydata1=mycursor.fetchall()
        if mycursor.rowcount!=0:
            passwd=input('Enter your password: ')
            if mydata1[0][-1]==passwd:
                accno2=int(input('Enter the account number to which you want to transfer: '))
                mycursor.execute('select * from acc where accno={}'.format(accno2))
                mydata1=mycursor.fetchall()
                if mycursor.rowcount!=0:
                    tran=int(input('Enter the amount you would like to transfer: '))
                    mycursor.execute('select * from transac where accno={}'.format(accno1))
                    mydata1=mycursor.fetchall()
                    balance1=mydata1[-1][-1]
                    if tran>balance1:
                        print('Transfer amount is higher than balance')
                        break
                    else:
                        tt='w'
                        cmd1="insert into transac(accno,transtype,dot,transamt,balance) values(%s,'%s','%s',%s,%s)"%(accno1,tt,date.today(),tran,balance1-tran)
                        mycursor.execute(cmd1)
                        tt='d'
                        mycursor.execute('select * from transac where accno={}'.format(accno2))
                        mydata2=mycursor.fetchall()
                        balance2=mydata2[-1][-1]
                        cmd2="insert into transac(accno,transtype,dot,transamt,balance) values(%s,'%s','%s',%s,%s)"%(accno2,tt,date.today(),tran,balance2+tran)
                        mycursor.execute(cmd2)
                        mycon.commit()
                    print('Transaction complete')
                    break
                else:
                    print('Invalid account no')
                    break
            else:
                print('Incorrect Password')
                break
        else:
            print('Invalid account no')
            break
def trans_d():
    accno=int(input('Enter your account number: '))
    mycursor.execute('select * from acc where accno={}'.format(accno))
    mydata=mycursor.fetchall()
    if mycursor.rowcount!=0:
        name=mydata[0][1]
        passwd=input('Enter your password: ')
        if mydata[0][-1]== passwd:
            mycursor.execute('select * from transac where accno={}'.format(accno))
            mydata=mycursor.fetchall()
            print()
            print('Name: ',name)
            print()
            print('TransType'+'\t','DateOfTrans'+'\t','TransAmt'+'\t','Balance')
            for x in range(len(mydata)):
                tt=mydata[x][1]
                if tt=='d':
                    tt='Deposit  '
                else:
                    tt='Withdrawal'
                dot=str(mydata[x][2])+'\t'*2
                ta=str(mydata[x][3])
                bal=mydata[x][4]
                ta+=' '*(8-len(ta))+'\t'
                print(tt+'\t',dot,ta,str(bal)+'\t')
                
        else:
            print('Incorrect password')
    else:
        print('Invalid account no')
def ch_pass():
    accno=int(input('Enter your account number: '))
    mycursor.execute('select * from acc where accno={}'.format(accno))
    mydata=mycursor.fetchall()
    x=input('Enter your existing password: ')
    if mydata[0][-1]==x:
        while True:
            z=input('Enter the new password: ')
            y=input('Confirm the new password: ')
            if y!=z:
                print('Try again')
                break
            else:
                mycursor.execute("update acc set passwd='{}' where accno={}".format(y,accno))
                mycon.commit()
                print('Password changed')
            break
    else:
        print ('Incorrect password')

print('Welcome To Axios Holdings')
while True:
    print()
    print('M E N U')
    print('1. Create Account')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Transfer')
    print('5. Display Account Details')
    print('6. Display Transaction Details')
    print('7. Change Password')
    print('8. Terminate')
    print('9. Exit')
    ch=int(input('Enter your choice: '))
    if ch==1:
        create()
    elif ch==2:
        deposit()
    elif ch==3:
        withdraw()
    elif ch==4:
        transfer()
    elif ch==5:
        display()
    elif ch==6:
        trans_d()
    elif ch==7:
        ch_pass()
    elif ch==8:
        terminate()
    elif ch==9:
        print('Thank You For Using Our Service')
        break
    else:
        print('Invalid Choice')
        break
mycon.close()