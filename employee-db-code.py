                                                #FUNCTIONS OF THE APPLICATION:


def input_records(listOfRecords):
    '''This function helps you to input the record of an employee'''
    
    while True:
        name=input('Enter Employee\'s name: ')
        desig=input('Enter designation: ')
        bsal=int(input('Enter the gross salary: '))
        tax=int(input('Enter Tax deduction: '))
        bonus=int(input('Enter the bonus rewarded: '))
        listOfRecords.append([name,desig,bsal,tax,bonus])
        choice=input('Enter "y" or "Y" to continue or any other key to exit: ')
        print()
        if choice!='y' and choice!='Y':
            break

def display_records(listRecords):
    '''This function helps display the records that is maintained by the current list'''
    
    serial=1
    print(listRecords)
    global listOfRecords
    for subRecord in listOfRecords:
        print('Serial number:',serial)
        print('Name:',subRecord[0])
        print('Designation:',subRecord[1])
        print('Basic Salary:',subRecord[2])
        print('Tax applied:',subRecord[3])
        print('Bonus awarded:',subRecord[4])
        print('Net salary:',int(subRecord[2])-int(subRecord[3])+int(subRecord[4]))
        print()
        serial+=1

def save_records(listOfRecords):
    '''This function helps you to save a record in a new file (or by overwriting in a currently existing '.txt' file)'''
    
    f=open('employee.txt','w')
    for subRecord in listOfRecords:
        f.write(subRecord[0]+',')
        f.write(subRecord[1]+',')
        f.write(str(subRecord[2])+',')
        f.write(str(subRecord[3])+',')
        f.write(str(subRecord[4])+'\n')
    print('DATA SAVED IN A NEW FILE')
    print()
    f.close

def resave_records(listOfRecords):
    '''This function helps you to append a new record in a currently existing file'''
    
    f=open('employee.txt','a')
    for subRecord in listOfRecords:
        f.write(subRecord[0]+',')
        f.write(subRecord[1]+',')
        f.write(str(subRecord[2])+',')
        f.write(str(subRecord[3])+',')
        f.write(str(subRecord[4])+'\n')
    print('NEW DATA SAVED')
    print()
    f.close()

def load_records(listOfRecords):
    '''This function helps you to extract all the records saved in the file in your currently working list'''
    
    f=open('employee.txt')
    for line in f:
        line=line.split(',')
        name=line[0]
        desig=line[1]
        bsal=int(line[2])
        tax=int(line[3])
        bonus=int(line[4])
        listOfRecords.append([name,desig,bsal,tax,bonus])
    f.close()
        
    serial=1
    for subRecord in listOfRecords:
        print('Serial number:',serial)
        print('Name:',subRecord[0])
        print('Designation:',subRecord[1])
        print('Basic Salary:',subRecord[2])
        print('Tax applied:',subRecord[3])
        print('Bonus awarded:',subRecord[4])
        print('Net salary:',int(subRecord[2])-int(subRecord[3])+int(subRecord[4]))
        print()
        serial+=1

def search_record(listOfRecords):
    '''This function allows you to search an employee's record by inputting his/her name'''
    
    count=0
    emp_name=input('Enter the name of employee you want to search about: ')
    print()
    f=open('employee.txt','r')
    records=f.readlines()
    for i in records:
        record=i.split(',')
        if record[0]==emp_name:
            print('Name:',record[0])
            print('Designation:',record[1])
            print('Basic Salary:',record[2])
            print('Tax applied:',record[3])
            print('Bonus awarded:',record[4])
            print()
            count+=1
    if count==0:
        print('*DATA OF THIS EMPLOYEE NOT FOUND*')
        print()


def delete_record(listOfRecords):
    '''This function allows you to delete a record by looking at the given currently working list and
       deleting it from the list (note that it won't delete it from the file until you save it by overwriting it,
       to be specific, using the 'save_record()' function or the option 1)'''
    
    serial=1
    for subRecord in listOfRecords:
        print('Serial number:',serial)
        print('Name:',subRecord[0])
        print('Designation:',subRecord[1])
        print('Basic Salary:',subRecord[2])
        print('Tax applied:',subRecord[3])
        print('Bonus awarded:',subRecord[4])
        print('Net salary:',int(subRecord[2])-int(subRecord[3])+int(subRecord[4]))
        print()
        serial+=1
    delt=int(input("Enter the serial number you want to delete: "))
    print()
    listOfRecords.pop(delt-1)

                                      #THE MENU AND THE CALLING OF THE FUNCTIONS
    
while True:                             
    
    print('''       EMPLOYEES' DATABASE:

           1. Input Record(s)
           2. Display Records
           3. Save Records 
           4. Load Records
           5. Search from Record
           6. Delete an Entry from the Record
           7. Exit
           ''')
    n=int(input('Enter option number: '))
    print()
    if n==7:
        print('Thankyou for using this application.')
        print('x'*100)
        break
        
    if n==1:
        listOfRecords=[]
        input_records(listOfRecords)
                   
    if n==2:
        display_records(listOfRecords)

    if n==3:
        print('''Do you want to save data in a new file OR append the new data in an older file?
              1. Start Fresh
              2. Append
              ''')
        n1=int(input('Enter option number: '))
        print()
        if n1==1:
            save_records(listOfRecords)
        if n1==2:
            resave_records(listOfRecords)
        
    if n==4:
        listOfRecords=[]
        load_records(listOfRecords)

    if n==5:
        search_record(listOfRecords)

    if n==6:
        delete_record(listOfRecords)