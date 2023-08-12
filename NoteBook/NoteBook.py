import csv
import os,time
from datetime import datetime

#Menu#

menu1 = '************************************\n\tWelcome to NoteBook\n************************************\n1)New Page\n2)Open NoteBook\n0)Exit\n************************************'

#----Operations----#

def memory(path):
    # Program kapaninca kendini sifirliyor
    global memory_dict
    with open(path,'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader :
            row = str(row[0])
            if row[0] == '\t' :
                for k in memory_dict.keys():
                    if k == date_row:
                        memory_dict[k].append(row)
            else:
                date_row = row
                if not date_row in memory_dict.keys():
                    memory_dict.update({date_row:[]})

def memory_write(path):
    with open(path,'w') as file:
        csv_writer = csv.writer(file,delimiter=',')
        for k in memory_dict.keys():
            csv_writer.writerow([k])
            for v in memory_dict[k]:
                csv_writer.writerow([v])

def new_page(path):
    with open(path,'w') as file :
        csv_writer = csv.writer(file,delimiter=',')
        current_time = datetime.now().strftime('%d/%m/%y')
        csv_writer.writerow([current_time])
        user_note = input('Enter your note:')
        csv_writer.writerow([f'\t{user_note}'])
    memory(path)
    memory_write(path)
    print('New page added.')
    print(f'Note: {user_note}')
    wait = input()

def open_page(path):
    with open(path,'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(str(row[0]))
    wait = input()


#Main#
memory_dict = {}
file_path = 'data.csv'
memory(file_path)
runner = True
user_input = None
while runner:
    if user_input == None:
        print(menu1)
        user_input = int(input('Enter your choice:'))
    elif user_input == 0:
        runner = False
    elif user_input == 1:
        new_page(file_path)
        user_input = None
    elif user_input == 2:
        open_page(file_path)
        user_input = None
    else:
        print('Please enter a valid number.')
        user_input = None
        time.sleep(1)
    
    os.system('clear')
    