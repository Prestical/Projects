import csv
import os
from tqdm import tqdm
from time import sleep

# I made this program to imcrease motivation to study.In my opinion that way it becomes fun :D

# ************************ IMPORTANT ************************
# If you want to change PLAYER name you must change it in csv file.
# It may give error because of the file path difference. I recommend to change the file path before running the code.
# If you want to add a new skill in csv file make your changes like that: skill kind,level,exp,level limit,total minutes
# Point calculation : Minutes * 0.1 = Exp

path = "dataBase.csv"

file = open(path)
data = csv.reader(file)
myDict = {}

class menus():
    def main():
        print('''
********** Welcome to Real_Life_RPG **********
1) View Status
2) Go EXP Farming
0) Quit
**********************************************
        ''')
    def write():
        print('''
**********************************************
        ''')
        for x,k in enumerate(myDict.keys()):
            print(f'{x+1}) {k.capitalize()}')
        print('''
**********************************************
        ''')


def write_to_csv():
    if not bool(myDict):
        print('Please view status first !!')
    else:
        menus.write()
        enterW = input('Select an operation (Type name of the option, not number): ')
        minutes = int(input(f'How many minutes did you worked on {enterW.capitalize()} ? Enter: '))
        with open(path, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            checker = 0
            for k,v in myDict.items():
                if checker == 0:
                    writer.writerow((k,v[0]))
                else:
                    v[0] = int(v[0])
                    v[1] = int(v[1])
                    v[2] = int(v[2])
                    v[3] = int(v[3]) 
                    if k == enterW.upper():
                        v[3] += minutes
                        if v[2] == 10:
                            v[1] = (v[3] * .1)
                        else:
                            v[1] = (v[3] * .1) - (v[2]/2)
                        while v[1] >= v[2]:
                            v[1] -= v[2]
                            v[2] *= 2
                            v[0] += 1
                    writer.writerow((k,v[0],int(v[1]),v[2],v[3]))
                checker +=1
        print('Data Changed')

def view():
    with open(path) as file:
        data = csv.reader(file)
        global myDict
        for x,line in enumerate(data):
            myDict.update({line[0]:line[1:]})
            if x == 0 :
                print(f'{line[0]}: {line[1]}')
            else:
                print(line[0],f'/ Total Hours: {round(float(myDict[line[0]][3]) / 60 ,1)}')
                for i in tqdm(range(int(myDict[line[0]][1])),
                              desc=f'Level {myDict[line[0]][0]}',
                              bar_format='{desc}{percentage:3.0f}% {bar}|{n}/{total}',
                              total=int(myDict[line[0]][2]),
                              ncols=80,):
                    sleep(.01)
# Program Loop
while True:
    menus.main()
    enter = int(input('Select an operation: ')) 
    os.system('clear')
    if enter == 0:
        break
    elif enter == 1:
        view()
    elif enter == 2:
        write_to_csv()
    else:
        print('Write a valid number !!')
    fin = input('Press any key to continue')
    os.system('clear')
