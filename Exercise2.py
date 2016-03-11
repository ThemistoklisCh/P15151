import random
import os

def game_on(board):
    s=n[0][0]+n[1][0]
    if (n[0][2]==0 and n[1][2]==0):
        if (n[0][1]==0 and n[1][1]==0):
            if (s<4):
                return 0
            else:
                return 1
        else:
            return 1
    else:
        return 1

def win(turn,board):

    #First, I'll check the lines and the columns.
        for i in xrange (3):
            line=0
            column=0
            for j in xrange (3):
                for z in xrange (3):
                    if (p[turn][z]==board[i][j]):
                        line+=1
                    if (p[turn][z]==board[j][i]):
                        column+=1
            if (line==3 or column==3):
                a=0
                break
            else:
                a=1

    #Finally,I'll check the 2 diagonals.
        diagonal1=0
        diagonal2=0
        for z in xrange (3):
            if (p[turn][z]==board[0][0]):
                diagonal1+=1
            if (p[turn][z]==board[1][1]):
                diagonal1+=1
            if (p[turn][z]==board[2][2]):
                diagonal1+=1
            if (p[turn][z]==board[0][2]):
                diagonal2+=1
            if (p[turn][z]==board[2][0]):
                diagonal2+=1
            if (p[turn][z]==board[1][1]):
                diagonal2+=1

            if (diagonal1==3 or diagonal2==3):
                b=0
                break
            else:
                b=1

        if (a*b==0):
            return 0
        else:
            return 1

print "Hello Ladies and Gentlemen..."
print "Welcome to a Tic-Tac-Toe game a bit diferent than others (some call it 'Gobblet Gobblers')!!!"
print "Let's Rock!!! \m/ \m/ "
print "-------------------------------------------------------------------------------"
print "Oh...where are my manners...my name is P15151...What about you?..."
names=[0,0]
names[0]=raw_input("Player 1...what is your nickname?")
names[1]=raw_input("Player 2...what about your nickname?")
print "-------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------"


c=0
while c==0:
    d=raw_input("Now my friends,press 'P' if you want to play the game,press 'H' if you want to read the instructions or press 'E' if you have other things to do and leave me be...")
    if (d=="p" or d=="P" or d=="h" or d=="H" or d=="e" or d=="E"):
        c=1


while c!=0:
    #Instructions!!!
    if (d=="H" or d=="h"):
            print "-------------------------------------------------------------------------------------------"
            print "1.You don't have to start with your biggest piece."
            print "2.Don't hesitate to gobble up your opponent's pieces."
            print "3.You can gobble up your own pieces."
            print "4.You can gooble up any smaller size Gobbler.It does not have to be the next size down."
            print "5.Before you move a piece try to remember what is under it."
            print "6.Always look at what your opponent is doing.Think ahead and have fun!!!"
            print "-------------------------------------------------------------------------------------------"

            c=0
            while c==0:
                d=raw_input("Now my friends,press 'P' if you want to play the game,press 'H' if you want to read the instructions or press 'E' if you have other things to do and leave me be...")
                if (d=="p" or d=="P" or d=="h" or d=="H" or d=="e" or d=="E"):
                    c=1

    #Game!!!
    if (d=="P" or d=="p"):
            print "Get ready!"

            #Declare arrays...
            p=[["" for y in xrange(3)] for x in xrange(2)]
            board=[["" for y in xrange(3)] for x in xrange(3)]
            v=[[0 for y in xrange(3)] for x in xrange(3)]
            n=[[0 for y in xrange(3)] for x in xrange(2)]
            wins=[0,0]

            p[0][0]="A1"
            p[0][1]="A2"
            p[0][2]="A3"
            p[1][0]="B1"
            p[1][1]="B2"
            p[1][2]="B3"

            c=0
            while c==0:
                print "Press 'A' for %s to play first,'B' for %s or 'R' so I can select who will start" % (names[0], names[1])
                first_player=raw_input("Who would you like to start the game first?")
                if (first_player=="A" or first_player=="a" or first_player=="B" or first_player=="b" or first_player=="R" or first_player=="r"):
                    c=1

            if (first_player=="A" or first_player=="a"):
                nturn=0
            elif (first_player=="B" or first_player=="b"):
                nturn=1
            else:
                nturn=random.choice([0,1])

            for i in xrange(3):
                n[0][i]=2
                n[1][i]=2
            game=1
            for i in xrange(3):
                for j in xrange(3):
                    board[i][j]="  "
                    v[i][j]=0
            winner=" "
            while (game==1):


                turn=nturn
                #Player's Move!!!
                c0=0
                while c0==0:
                    print "-----------------------------------------------------------"
                    print "-----------------------------------------------------------"
                    print "%s...What's your move???" % (names[turn])
                    c1=0
                    while c1==0:
                        print "Pick the box you wish to place your Gobbler..."
                        i=input("What's the line of the box you wish to place the Gobbler? (1-3)")
                        i=i-1
                        j=input("What's the column of the box you wish to place the Gobbler? (1-3)")
                        j=j-1
                        if (type(i) == int and type(j) == int):
                            if (i>=0 and i<=2 and j>=0 and j<=2):
                                if v[i][j]<3:
                                    c1=1
                                if v[i][j]==3:
                                    print "You can't place a Gobbler over one of the Biggest Gobblers...Re-think your strategy and choose another box!"

                    print "What kind of Gobbler would you like to place in the %s,%s box? (1-3)" % (i+1,j+1)
                    c2=0
                    while c2==0:
                        value=input("Choose the Gobbler's value...")
                        if (type(value)==int):
                            if (n[turn][value-1]>=1):
                                if (v[i][j]<value):
                                    c2=1
                                else:
                                    print "You need to place a higher value than the one in the box..."
                            else:
                                print "There are no other Gobblers of that value left..."
                    c3=0
                    while c3==0:
                        print "%s,you have chosen to place a %s-value Gobbler in the box %s,%s" % (names[turn],value,i+1,j+1)
                        answer=raw_input("Is this your final decision?(press 'Y' for 'Yes' or 'N' for 'No')")
                        if (answer=="N" or answer=="n"):
                            c3=1
                        if (answer=="Y" or answer=="y"):
                            c3=1
                            c0=1
                            board[i][j]=p[turn][value-1]
                            v[i][j]=value
                            n[turn][value-1]=(n[turn][value-1])-1

                #Clear the screen and print the score and the board...
                os.system('cls')
                print "-----------------------------------------------------------"
                print "-----------------------------------------------------------"
                print "%s : %s wins -- %s : %s wins" % (names[0],wins[0],names[1],wins[1])
                print "-----------------------------------------------------------"

                print('    |     |')
                print(' ' + board[0][0] + ' | ' + board[0][1] + '  | ' + board[0][2])
                print('    |     |')
                print('----------------')
                print('    |     |')
                print(' ' + board[1][0] + ' | ' + board[1][1] + '  | ' + board[1][2])
                print('    |     |')
                print('----------------')
                print('    |     |')
                print(' ' + board[2][0] + ' | ' + board[2][1] + '  | ' + board[2][2])
                print('    |     |')





                game_on(board)
                win(turn,board)
                g=game_on(board)
                w=win(turn,board)
                game=g*w
                if (turn==0):
                    nturn=1
                else:
                    nturn=0






            if (w==0):
                wins[turn]+=1
                os.system('cls')
                print "-----------------------------------------------------------"
                print "-----------------------------------------------------------"
                print "%s : %s wins -- %s : %s wins" % (names[0],wins[0],names[1],wins[1])
                print "-----------------------------------------------------------"

                print('    |     |')
                print(' ' + board[0][0] + ' | ' + board[0][1] + '  | ' + board[0][2])
                print('    |     |')
                print('----------------')
                print('    |     |')
                print(' ' + board[1][0] + ' | ' + board[1][1] + '  | ' + board[1][2])
                print('    |     |')
                print('----------------')
                print('    |     |')
                print(' ' + board[2][0] + ' | ' + board[2][1] + '  | ' + board[2][2])
                print('    |     |')
                print "Congratulations %s!!!You are the Champ..." % (names[turn])
                print "-----------------------------------------------------------"
                print "-----------------------------------------------------------"
            else:
                print "Draw!you noobs..."
                print "-----------------------------------------------------------"
                print "-----------------------------------------------------------"
            c=0
            while c==0:
                d=raw_input("Now my friends,press 'P' if you want to play another game,press 'H' if you want to read the instructions or press 'E' if you have other things to do and leave me be...")
                if (d=="p" or d=="P" or d=="h" or d=="H" or d=="e" or d=="E"):
                    c=1

    if (d=="E" or d=="e"):
        break

print "%s!...%s!...It has been a pleasure!!!" %(names[0],names[1])
print "Till next time....(don't make me emotional...)"
bye=input("\m/ (^_^) \m/")
bye="Bye!"
