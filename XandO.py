print("this really is my first python file")

#Develop code for XandO terminal game

#construct input for XandO box
xando = {'7':" ", '8': " ", '9':" ",
'4': " ", '5': " ", '6': " ",
'1': " ", '2': " ", '3': " "}

board_keys = []

for key in xando:
    board_keys.append(key)

#print XandO box to begin game
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


#game function to take player input & update XandO box
def game():
    turn = 'X'
    count = 0

    for i in range(10):

        printboard(xando)
        print('Player ' + turn + ' , please select your move..')

        move = input()

        if xando[move] == " ":
            xando[move] = turn
            count += 1
        else:
            print("Position already filled.\nMove to which place?")
            continue

        #loop to check for winner
        if count >= 5:
            #horizontal
            if xando['7'] == xando['8'] == xando['9'] != " ":
                printboard(xando)
                print("Game over. " + turn + " is the champion")
                break
            elif xando['4'] == xando['5'] == xando['6'] != " ":
                printboard(xando)
                print("Game over. " + turn + " is the champion")
                break
            elif xando['1'] == xando['2'] == xando['3'] != " ":
                printboard(xando)
                print("Game over. " + turn + " is the champion")
                break
            #vertical
            if xando['7'] == xando['4'] == xando['1'] != " ":
                printboard(xando)
                print("Game over. " + turn + " is the champion")
                break
            elif xando['8'] == xando['5'] == xando['2'] != " ":
                printboard(xando)
                print("Game over. " + turn + " is the champion")
                break
            elif xando['9'] == xando['6'] == xando['3'] != " ":
                printboard(xando)
                print("Game over. " + turn + " is the champion")
                break
            #diagonal
            if xando['7'] == xando['5'] == xando['3'] != " ":
                printboard(xando)
                print("Game over. " + turn + " is the champion")
                break
            elif xando['1'] == xando['5'] == xando['9'] != " ":
                printboard(xando)
                print("Game over. " + turn + " is the champion")
                break
        
        if count == 9:
            print("It's a draw game")

        if turn == "X":
            turn = "0"
        else:
            turn = "X"
            

#ask players to play again?
    replay = input("Would you like to play again?(y/n)")
    if replay == "y" or replay == "Y":
        for key in board_keys:
            xando[key] = " "
        
        game()

if __name__ == "__main__":
    game()