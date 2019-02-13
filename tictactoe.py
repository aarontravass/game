playg=[[0,0,0],[0,0,0],[0,0,0]]# main play map
# current player will choose 2. opponent 1.
#main loop to run. will run by defsult from 0 to 9
print("Choose numbers greater than zero")
print("Your choice")
p1=int(input())
print("Opponent's choice")
p2=int(input())
a=0
for i in range(9):
    #------------------------------------------------------------------------------------------------
    #choice selection based on row,column
    if(a==0):
        print("Your turn")
        print("Enter row,column")
        row, col = map(int, input().split())

        playg[row][col] = p1
        a=1
    elif(a==1):
        print("Opponent's turn")
        print("Enter row,column")
        row, col = map(int, input().split())

        playg[row][col] = p2
        a=0

    print(playg[0])
    print(playg[1])
    print(playg[2])
    c=0
    #choice completed
    #minimum no moves required to win is 5. hence search will start when i=4
    #-------------------------------------------------------------------------------------------------
    #search code
    if(i>=4):
        #for loop to check horizontal and vertical rows
        for j in range(0,3):
            if(playg[0][j]==playg[1][j] and playg[1][j]==playg[2][j] and playg[0][j]==playg[2][j]):
                if(playg[0][j]==p1):
                    print("you won")
                    c=1
                    break
                elif(playg[0][j]==p2):
                    print("opponent won")
                    c=1
                    break
            elif (playg[j][0] == playg[j][1] and playg[j][1] == playg[j][2] and playg[j][0] == playg[j][2]):
                if (playg[j][0] == p1):
                    print("you won")
                    c=1
                    break
                elif (playg[j][0] == p2):
                    print("opponent won")
                    c=1
                    break
        #following conditions to check diagonal elements
        if(playg[0][0]==playg[1][1] and playg[1][1]==playg[2][2] and playg[2][2]==playg[0][0]):
            if (playg[0][0] == p1):
                print("you won")
                c=1
                break
            elif (playg[0][0] == p2):
                print("opponent won")
                c=1
                break
        elif(playg[0][2]==playg[1][1] and playg[1][1]==playg[2][0] and playg[2][0]==playg[0][2]):
            if (playg[1][1] == p1):
                print("you won")
                c=1
                break
            elif (playg[1][1] == p2):
                print("opponent won")
                c=1
                break
        #if player already won then end the game
        if(c==1):
            break
    #-------------------------------------------------------------------------------------------------
if(c==0):
    print("Nobody won, tie!!")
