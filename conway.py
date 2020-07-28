import os
from time import sleep
from colorama import Back, Style
import random
os.system('mode 1000,1000')
os.system('cls')
i = int(input("Enter The Number Of Columns: "))
j = int(input("Enter The Number Of Rows: "))
c = int(input('Choose Display:\n1) Continuos\n2) Non-Continuos\n\n'))
d = False
if c == 1:
    d = True
if i > 35:
    i = 35
if j > 100:
    j = 100    
main_array = [[0 for temp_j in range(j)] for temp_i in range(i)]
# Rule 1: any live cell with two or three n's survive
# Rule 2: any dead cell with three live n's becomes a live cell


def n(x, y):
    global main_array

    n_counter = 0
    try:
        if main_array[x-1][y-1] == 1 or main_array[x-1][y-1] == 2:
            n_counter += 1
    except:
        pass
    try:
        if main_array[x-1][y] == 1 or main_array[x-1][y] == 2:
            n_counter += 1
    except:
        pass
    try:
        if main_array[x-1][y+1] == 1 or main_array[x-1][y+1] == 2:
            n_counter += 1
    except:
        pass
    try:
        if main_array[x][y-1] == 1 or main_array[x][y-1] == 2:
            n_counter += 1
    except:
        pass
    try:
        if main_array[x][y+1] == 1 or main_array[x][y+1] == 2:
            n_counter += 1
    except:
        pass
    try:
        if main_array[x+1][y-1] == 1 or main_array[x+1][y-1] == 2:
            n_counter += 1
    except:
        pass
    try:
        if main_array[x+1][y] == 1 or main_array[x+1][y] == 2:
            n_counter += 1
    except:
        pass
    try:
        if main_array[x+1][y+1] == 1 or main_array[x+1][y+1] == 2:
            n_counter += 1
    except:
        pass
    return n_counter

def create():
    global main_array
    for x in range(i):
        for y in range(j):
            if main_array[x][y] == 3:
                main_array[x][y] = 1


def destroy():
    global main_array
    for x in range(i):
        for y in range(j):
            if main_array[x][y] == 2:
                main_array[x][y] = 0


def reset():
    for x in range(i):
        for y in range(j):
            main_array[x][y] = 0


def check():
    global main_array
    for x in range(i):
        for y in range(j):
            if main_array[x][y] == 0:
                continue
            v = n(x, y)
            if not(v == 2 or v == 3):
                main_array[x][y] = 2
    for x in range(i):
        for y in range(j):
            if main_array[x][y] == 1:
                continue
            elif n(x, y) == 3:
                main_array[x][y] = 3
    create()
    destroy()


f = True


def p_array():
    print('* '*int((j/2)-1)+'*'+'SOF'+'* '*int((j/2)-1))
    global f
    print(Back.RED)
    for x in range(i):
        for y in range(j):
            if main_array[x][y] == 0:
                print(' ', end=' ')
            else:
                print(Back.GREEN + ' ', end=' ')
                print(Back.RED, end='')
        print()
    print(Style.RESET_ALL)
    print('* '*int((j/2)-1)+'*'+'EOF'+'* '*int((j/2)-1))

    if f:
        print('\n+\n')
    else:
        print('\n-\n')
    f = not(f)


# Initialize


def setup():
    global s
    global main_array
    
    
    while True:
        os.system('cls')
        p_array()
    #For random initialization
    # for temp_v in range(20):
    #     main_array[random.randint(0, i-1)][random.randint(0, j-1)] = 1
        print('Enter Starting Alive Cell Position: (Max: {},{}), (Enter "+" To Insert Random Live Cells), (Leave Blank When Done) '.format(i-1,j-1))
        try:
            x = input('Position X-Axis: ')
            

            if x == '':
                break
            if x == '+':
                tmp = int(input('Enter Number Of Cells: '))
                if tmp > ((i-1)*(j-1)):
                    temp = (i-1) * (j-1)
                print("Insertion Started")
                for temp_v in range(tmp):
                    main_array[random.randint(0, i-1) ][random.randint(0, j-1) ] = 1
                os.system('cls')
                p_array()
                input('Insertion Done')
                break
            x = int(x)
            if x >= i:
                input('Enter A Value Less Than {}\n'.format(i))
                continue
            y = int(input('Position Y-Axis: '))
            if y >= j:
                input('Enter A Value Less Than {}\n'.format(j))
                continue
            
            main_array[x][y] = 1
            
        except:
            pass


def home():
    while True:
        os.system('cls')
        p_array()
####Change the speed below
        if d:
            sleep(0.05)
        else:
            
            x = input("Press Enter To Continue: (Enter '+' To Reset Board)")
            if x == '+':
                reset()
                start()
                return

        check()

def start():
    setup()
    home()
start()
