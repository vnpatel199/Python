import sys
from IPython.display import clear_output

ds=[]
turns=[]

def start_game():
    ds.clear()
    ds.append([])
    ds.append([])
    ds.append([])
    turns.clear()

    for i in range(3):
        for j in range(3):
            ds[i].append(' ')
        
def display():
    clear_output()
    for i in range(3):
        for j in range(3):
            if j<2:
                print(ds[i][j],end='|')
            else:
                print(ds[i][j])

def turn(p):
    err=0

    while err==0:
        try:
            inp=int(input(r'Enter your choice(1-9): '))-1
            if inp not in range(9):
                raise Exception

            if inp in turns:
                raise Exception
            turns.append(inp)
            i=2-(inp//3)
            j=inp%3
            ds[i][j]=p
            err=1

        except Exception:
            print("Invalid choice!!!!")
            
def play():

    print("Welcome to Tic-Tac-Toe!!!")

    try:
        p1=(input("Player 1: do you want to be X or O ?: ")).upper()
        if p1=='X':
            p2='O'
        elif p1=='O':
            p2='X'
        else:
            raise Exception

    except Exception:
        print("Enter only X or O.")
        sys.exit(1)
        
    start_game()
    display()   
    turn(p1)
    display()

    for i in range(2):
            turn(p2)
            display()
            turn(p1)
            display()

    for k in range(2):
            if check()==True:
                print("Congratulations Player 1 !!! You won")
                break
                    
            turn(p2)
            display()
                
            if check()==True:
                print("Congratulations Player 2 !!! You won")
                break

            turn(p1)
            display()
        
            if check()==True:
                print("Congratulations Player 1 !!! You won")
                break

def check():
    
    for i in range(3):
        result=""
        for j in range(3):
            result+=ds[i][j]
        if result=="XXX" or result=="OOO":
            return True

    for x in range(3):
        result=""
        for y in range(3):
            result+=ds[y][x]
        if result=="XXX" or result=="OOO":
            return True

    result=""
    for z in range(3):
        result+=ds[z][z]
        if result=="XXX" or result=="OOO":
            return True

    result=""
    result=ds[0][2]+ds[1][1]+ds[2][0]
    if result=="XXX" or result=="OOO":
        return True
    
if __name__=='__main__':

        replay= 'yes'
        while replay=='yes':
            play()
            replay=input("Type yes to replay: ")