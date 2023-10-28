import time
import pickle
import os

class Hospital:
    def __init__(self):
        self.sno=0
        self.name=''
        self.age=0
        self.sex=''
        self.email=''
        self.fname=''
        self.address=''
        self.city=''
        self.state=''
        self.height=0
        self.weight=0
        self.doctor=''
        self.med=''
        self.bill=0
        self.paymethod=''
        self.pno=0
        self.bgroup=''
        self.dname=''
        
        
    def Input(self):
        self.sno=input('enter serial number :')
        self.name=input('enter patinet\'s name :')
        self.age=input('enter patinet\'s age :')
        self.sex=input('enter patinet\'s sex (male/female) :')
        self.height=input('enter patinet\'s height :')
        self.weight=input('enter patinet\'s weight(in Kg)')
        self.bgroup=input('enter patinet\'s blood group :')
        self.fname=input('enter patinet father\'s name :')
        self.address=input('enter address :')
        self.city=input('enter city :')
        self.state=input('enter state :')
        self.pno=input('enter phone number :')
        self.email=input('enter E-mail :')
        self.doctor=input('enter doctor\'s name :')
        self.dname=input('enter disease name :')
        self.med=input('enter prescribed medicine :')
        self.bill=input('enter bill amount:Rs.')
        self.paymethod=input('enter payment method(cash/cheque/card) :')
        
    
    def output(self):
        print('SERIAL NUMBER :_',self.sno)
        print('PATIENT\'S NAME :_',self.name)
        print('PATIENT\'S AGE :_',self.age)
        print('PATIENT\'S SEX :_',self.sex)
        print('PATIENT\'S HEIGHT :_',self.height)
        print('PATIENT\'S WEIGHT :_',self.weight)
        print('PATIENT\'S BLOOD GROUP :_',self.bgroup)
        print('PATIENT FATHER\'S NAME :_',self.fname)
        print('ADDRESS :_',self.address)
        print('CITY :_',self.city)
        print('STATE :_',self.state)
        print('CONTACT NUMBER :_',self.pno)
        print('E-MAIL ADDRESS :_',self.email)
        print('DISEASE NAME :_',self.dname)
        print('DOCTOR\'S NAME :_',self.doctor)
        print('PRESCRIBED MEDICINES :_',self.med)
        print('BILL AMOUNT :_',self.bill)
        print('PAYMENT METHOD :_',self.paymethod)
        
        
import time
import pickle
import os
    
    
def writeHospital():
    fout = open('Hospital5.DAT','wb')
    ob = Hospital()
    print('Enter Details:')
    ob.Input()
    pickle.dump(ob,fout)
    print('Record Saved')
    fout.close()
    
    
def readHospital():
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    
    try:
        print('Hospital Detail are:')
        while True:
            ob = pickle.load(fin)
            ob.output()
            print()
    
    except EOFError:
        fin.close()     
        
def searchHospitalsno(n):
    
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    flag = False
    
    try:
        print('\nHospital Detail are:')
        while True:
            ob = pickle.load(fin)
            if ob.sno == n:
                ob.output()
                flag = True
                
    except EOFError:
        if not flag:
            print('\n')
            print('\n')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
            print('\n.....RECORD...DOES...NOT...EXIST.....')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close()
        
    
def searchHospitalemail(n):
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    flag = False
    
    try:
        print('\nHospital Detail are:')
        while True:
            ob = pickle.load(fin)
            if ob.email ==n:
                ob.output()
                flag = True
                
    except EOFError:
        if not flag:
            print('\n')
            print('\n')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
            print('\n.....RECORD...DOES...NOT...EXIST.....')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close()
        
        
def searchHospitalcontact(n):
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    flag = False
    
    try:
        print('\nHospital Detail are:')
        while True:
            ob = pickle.load(fin)
            if ob.pno == n:
                ob.output()
                flag = True
                
                
    except EOFError:
        if not flag:
            print('\n')
            print('\n')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
            print('\n.....RECORD...DOES...NOT...EXIST.....')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close()
        
        
def searchbloodgroup(n):
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    flag = False
    
    try:
        print('\nHospital Detail are:')
        while True:
            ob = pickle.load(fin)
            if ob.bgroup == n:
                ob.output()
                flag = True
                
                
    except EOFError:
        if not flag:
            print('\n')
            print('\n')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
            print('\n.....RECORD...DOES...NOT...EXIST.....')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close()
        
    
def searchage(n):
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    flag = False
    
    try:
        print('\nHospital Detail are:')
        while True:
            ob = pickle.load(fin)
            if ob.age == n:
                ob.output()
                flag = True
                
    except EOFError:
        if not flag:
            print('\n')
            print('\n')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
            print('\n.....RECORD...DOES...NOT...EXIST.....')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close()
        
        
def searchsex(n):
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    flag = False
    
    try:
        print('\nHospital Detail are:')
        while True:
            ob = pickle.load(fin)
            if ob.sex == n:
                ob.output()
                flag = True
                
    except EOFError:
        if not flag:
            print('\n')
            print('\n')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
            print('\n.....RECORD...DOES...NOT...EXIST.....')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close()
        
        
def searchdname(n):
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    flag = False
    
    try:
        print('\nHospital Detail are:')
        while True:
            ob = pickle.load(fin)
            if ob.dname == n:
                ob.output()
                flag = True
                
    except EOFError:
        if not flag:
            print('\n')
            print('\n')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
            print('\n.....RECORD...DOES...NOT...EXIST.....')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close()
        
    
def searchdoctor(n):
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    flag = False
    
    try:
        print('\nHospital Detail are:')
        while True:
            ob = pickle.load(fin)
            if ob.doctor == n:
                ob.output()
                flag = True
                
    except EOFError:
        if not flag:
            print('\n')
            print('\n')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
            print('\n.....RECORD...DOES...NOT...EXIST.....')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close()
        

def searchpayment(n):
    fin = open('Hospital5.DAT','rb')
    ob = Hospital()
    flag = False
    
    try:
        print('\nHospital Detail are:')
        while True:
            ob = pickle.load(fin)
            if ob.paymethod == n:
                ob.output()
                flag = True
                
    except EOFError:
        if not flag:
            print('\n')
            print('\n')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
            print('\n.....RECORD...DOES...NOT...EXIST.....')
            print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close() 
        
        
        
def modiHospital(b,n):
    fin = open('Hospital5.DAT','rb')
    fout = open('temp5.DAT','ab')
    ob = Hospital()
    flag = False
    
    try:
        while True:
            ob = pickle.load(fin)
            if ob.sno == b:
                flag = True
                
                if n == 1:
                    a = input('ENTER NEW PATIENT\'S NAME:-->')
                    ob.name = a 
                    pickle.dump(ob,fout)
                    
                elif n == 2:
                    a = input('ENTER NEW PATIENT\'S AGE:--> ')
                    ob.age = a
                    pickle.dump(ob,fout)
                    
                elif n == 3:
                    a = input('ENTER NEW PATIENT\'S SEX(MALE/FEMALE):--> ')
                    ob.sex = a
                    pickle.dump(ob,fout)
                    
                elif n == 4:
                    a = input('ENTER NEW PATIENT\'S HEIGHT:--> ')
                    ob.height = a
                    pickle.dump(ob,fout)
                    
                elif n == 5:
                    a = input('ENTER NEW PATIENT\'S WIGHT(In Kgs):--> ')
                    ob.weight = a
                    pickle.dump(ob,fout)
                    
                elif n == 6:
                    a = input('ENTER NEW PATIENT\'S BLOOD GROUP:--> ')
                    ob.bgroup = a
                    pickle.dump(ob,fout)
                    
                elif n == 7:
                    a = input('ENTER NEW PATIENT\'S FATHER NAME:--> ')
                    ob.fname = a
                    pickle.dump(ob,fout)
                    
                elif n == 8:
                    a = input('ENTER NEW PATIENT\'S ADDRESSS:--> ')
                    ob.address = a
                    pickle.dump(ob,fout)
                    
                elif n == 9:
                    a = input('ENTER NEW PATIENT\'S CITY:--> ')
                    ob.city = a
                    pickle.dump(ob,fout)
                    
                elif n == 10:
                    a = input('ENTER NEW PATIENT\'S STATE:--> ')
                    ob.state = a
                    pickle.dump(ob,fout)
                    
                elif n == 11:
                    a = input('ENTER NEW PATIENT\'S CONTACT NUMBER:--> ')
                    ob.pno = a
                    pickle.dump(ob,fout)
                    
                elif n == 12:
                    a = input('ENTER NEW PATIENT\'S E-MAIL ADDRESS:--> ')
                    ob.email = a
                    pickle.dump(ob,fout)
                    
                elif n == 13:
                    a = input('ENTER NEW PATIENT\'S DISEASE NAME:--> ')
                    ob.dname = a
                    pickle.dump(ob,fout)
                    
                elif n == 14:
                    a = input('ENTER NEW DOCTOR\'S NAME:--> ')
                    ob.doctor = a
                    pickle.dump(ob,fout)
                    
                elif n == 15:
                    a = input('ENTER NEW PRESCRIBED MEDICINE:--> ')
                    ob.med = a
                    pickle.dump(ob,fout)
                    
                elif n == 16:
                    a = input('ENTER NEW BILL AMOUNT:-->Rs. ')
                    ob.paymethod = a
                    pickle.dump(ob,fout)
                    
                elif n == 17:
                    a = input('ENTER NEW PEYMENT METHOD(Cash/Cheque/card):--> ')
                    ob.bill = a
                    pickle.dump(ob,fout)
                    
                elif n == 18:
                    print('–––––––––––––––––ENTER THE NEW DETAILS–––––––––––––––––')
                    ob.Input()
                    pickle.dump(ob,fout)
                    
                else:
                    print('ENTER VALID CHOICE!!!!!!')
                    
            else:
                pickle.dump(ob,fout)
                
    except EOFError:
        if not flag:
            if not flag:
                print('\n')
                print('\n')
                print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
                print('\n.....RECORD...DOES...NOT...EXIST.....')
                print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        fin.close()
    fout.close()
    os.remove('Hospital5.DAT')
    os.rename('temp5.DAT','Hospital5.DAT')
    

def DelHospital(n):
    fin = open('Hospital5.DAT','rd')
    fount = open('temp5.DAT','wb')
    ob = Hospital()
    flag = False
    
    try:
        while True:
            ob = pickle.load(fin)
            if ob.sno == n:
                flag = True
                print('Record Deleted')
                
            else:
                pickle.dump(ob.fout)
                
    except EOFError:
        if not flag:
            print('Record Does Not Exist')
        fin.close()
        fount.close()
        os.remove('Hospital5.DAT')
        os.rename('temp5.DAT','Hospital5.DAT')
        
        
#MAIN PROGRAM
while True:
    print('\n')
    print('simple hospital management system\n ')
    print('1.WRITE RECORD')
    print()
    print('2.SHOW ALL RECORDS')
    print()
    print('3.SEARCH BY SERIAL NUMBER')
    print()
    print('4.SEARCH BY CONTACT NUMBER')
    print()
    print('5.SEARCH BY BLLOD GROUP')
    print()
    print('6.SEACH BY AGE')
    print()
    print('7.SEARCH BY SEX')
    print()
    print('8.SEARCH DISEASE NAMe')
    print()
    print('9.SEARCH BY DOCTOR NAME')
    print()
    print('10.SEARCH BY PAYMENT METHOD')
    print()
    print('11.SEARCH BY E-MAIL')
    print()
    print('12.MODIFY RECORD ')
    print()
    print('13.DELETE RECORD')
    print()
    print('14.EXIT')
    
    ch = eval(input('PLEASE ENTER YOUR CHOICE :'))
    
    if ch == 1:
        writeHospital()
        
    elif ch == 2:
        readHospital()
        
    elif ch == 3:
        n = input('PLEASE ENTER SERIAL NUMBER TO SEARCH:--> ')
        searchHospitalsno(n)
        
    elif ch == 4:
        n =input('PLEASE ENTER CONTACT NUMBER TO SEARCH:--> ')
        searchHospitalcontact()
        
    elif ch == 5:
        n = input('PLEASE ENTER BLOOD GROUP TO SEARCH:--> ')
        searchbloodgroup(n)
        
    elif ch == 6:
        n = input('PLEASE ENTER AGE TO SEARCH:--> ')
        searchage(n)
        
    elif ch == 7:
        n = input('PLEASE ENTER SEX TO SEARCH:-->')
        searchsex(n)
        
    elif ch == 8:
        n = input('PLEASE ENTER DISEASE NAME TO SEARCH:-->')
        searchdname(n)
        
    elif ch == 9:
        n = input('PLEASE ENTER DOCTOR NAME TO SEARCH:-->')
        searchdoctor(n)
        
    elif ch == 10:
        n = input('PLEASE ENTER PAYMENT MEHOD TO SEARCH:-->')
        searchpayment(n)
        
    elif ch == 11:
        n = input('PLEASE ENTER E-MAIL ADDRESS TO SEARCH:-->')
        searchHospitalemail(n)
        
    elif ch == 12:
        m = input('ENTER THE SERIAL NUMBER TO MODIFY:-->')
        print('\n')
        print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        print('................ENTER YOUR CHOICE................')
        print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
        print('\n')
        print('WHAT DO YOU WANT TO MODIFY:')
        print()
        print('1.PATIONT\'S NAME:-->')
        print('2.PATIONT\'S AGE:-->')
        print('3.PATIONT\'S SEX:-->')
        print('4.PATIONT\'S HEIGHT:-->')
        print('5.PATIONT\'S WEIGHT:-->')
        print('6.PATIONT\'S BLOOD GROUP:-->')
        print('7.PATIONT FATHER\'S NAME:-->')
        print('8.ADDRESS:-->')
        print('9.CITY:-->')
        print('10.STATE:-->')
        print('11.CONTACT NUMBER:-->')
        print('12.E-MAIL ADDRESS:-->')
        print('13.DISEASE NAME:-->')
        print('14.DOCTOR\'S NAME:-->')
        print('15.PRESCRIBED MEDICINES:-->')
        print('16.BILL AMOUNT:-->')
        print('17.PAYMENT METHOD:-->')
        print('18.ALL:-->')
        n = eval(input(':-->'))
        modiHospital(m,n)
        
    elif ch == 13:
        n = input('ENTER SERIAL NUMBER TO DELETE :--')
        DelHospital(n)
        
    elif ch == 14:
        print('\n')
        print('EXITING'),
        time.sleep(2)
        print('*'),
        time.sleep(2)
        print('*'),
        time.sleep(2)
        print('*'),
        break
        
    else:
        print('Analysing yor input.'),
        time.sleep(2)
        print('*'),
        time.sleep(2)
        print('*'),
        time.sleep(2)
        print('*')
        print('\n\n\n~~~~~~~~~~~~~~~~~~~WRONG CHOICE!!!~~~~~~~~~~~~~~~~~~~\n\n\n')