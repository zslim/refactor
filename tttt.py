import random
import os


def generateTable():
    table = []
    for x in range(0, 9):
        table.append(str(x + 1))
    return table


def is_win(table, win=False):
    for x in range(0, 3):
        y = x * 3
        if (table[y] == table[(y + 1)] and table[y] == table[(y + 2)]):
            win = True
            os.system('clear')
            printBoard(table)
            return win

        if (table[x] == table[(x + 3)] and table[x] == table[(x + 6)]):
            win = True
            os.system('clear')
            printBoard(table)
            return win

    if((table[0] == table[4] and table[0] == table[8]) or (table[2] == table[4] and table[4] == table[6])):
        win = True
        os.system('clear')
        printBoard(table)
        return win


def is_tie(table, tie, win):
    if(len(set(table)) == 2):
        if not win:
            tie = True
            os.system('clear')
            printBoard(table)
            return tie


def colored(text, color):
    codes = {"red": "\u001b[31m",
             "yellow": "\u001b[33m",
             "blue": "\u001b[34m",
             "light blue": "\u001b[36m",
             "end": "\u001b[0m"}
    return codes[color] + text + codes["end"]


def winmsg(tie, p1turn, p1, p2):
    global player1score, player2score
    if tie:
        print(colored("It's a tie!\n", "yellow"))
        os.system('spd-say "It\'s a tie"')
    else:
        if p1turn:
            if p2.upper() == 'AI':
                os.system('spd-say -r -50 "haa haa haa silly hooman you lost ha ha ha"')
                player2score += 1
                print(colored(p2 + " wins!       ツ\n", "blue"))
            else:
                os.system('spd-say -r -50 "Player 2 wins"')
                print(colored("Congratulations!\n", "yellow"))
                player2score += 1
                print(colored(p2 + " wins!       ツ\n", "blue"))

        else:
            print(colored("Congratulations!\n", "yellow"))
            print(colored(p1 + " wins!       ツ\n", "red"))
            os.system('spd-say -r -50 "Player 1 wins"')
            player1score += 1


def giveError():
    print(colored("Must be a number between 1 and 9!\n", "yellow"))


def giveIllegalMove():
    print(colored("\nThat number is already taken, chose another!\n", "yellow"))


def welcome():
    os.system('clear')
    print(colored("Welcome to our ToeTacTic demo!\n", "yellow"))


def restart(p1, p2):
    print(colored("The score is: \n", "light blue"))
    print(colored(str(p1) + ": " + str(player1score), "red"))
    print(colored(str(p2) + ": " + str(player2score), "blue"))
    again = input(colored("\nPress (Y) to play again or (any key) to quit! \n", "light blue"))
    if again[0].upper() == 'Y':
        try:
            os.system('clear')
            main(p1, p2)
        except IndexError:
            quit()
    else:
        os.system('clear')
        if player1score > player2score:
            print(colored(str(p1) + " wins!\n", "red"))
        elif player1score == player2score:
            print(colored("\nIt's a tie!\n", "yellow"))
        else:
            print(colored("\n" + str(p2) + " wins!\n", "blue"))
        print(colored(str(player1score), "red") + " : " + colored(str(player2score) + "\n", "blue"))
        print(colored("\nGood bye!\n", "yellow"))
        os.system('spd-say -r -50 "Good bye"')
        quit()


def input_p1():
    os.system('spd-say -r -50 "What is your name human?"')
    p1 = input(colored("First player's name: \n", "red"))
    return p1


def input_p2():
    p2 = input(colored("Second player's name: (Type 'AI' to play against the AI) \n", "blue"))
    return p2


def main(p1, p2):
    table = generateTable()
    p1turn = True
    tie = False
    win = False
    circle = colored("◉", "blue")
    cross = colored("✘", "red")
    p1 = p1
    p2 = p2
    os.system('clear')
    printBoard(table)
    if p2.upper() == 'AI':
        os.system('spd-say -r -50 "i let you go first human wink wink"')
    while not win and not tie:
        if p1turn:
            print(colored(str(p1) + "\'s turn!\n", "red"))
            try:
                choice = int(input(colored("Enter a number: ", "red")))
                if choice < 1 or choice > 9:
                    giveError()
                    continue
                elif table[choice - 1] == cross or table[choice - 1] == circle:
                    giveIllegalMove()
                    continue
                else:
                    table[choice - 1] = cross
                    os.system('clear')
                    printBoard(table)
                    p1turn = False
            except ValueError:
                giveError()
                continue
        else:
            if p2.upper() == 'AI':
                while not p1turn:
                    for i in range(9):
                        ai_table = table.copy()
                        win_move = False
                        if table[i] == cross or table[i] == circle:
                            continue
                        ai_table[i] = circle
                        win_move = is_win(ai_table)
                        if win_move:
                            table[i] = circle
                            os.system('clear')
                            printBoard(table)
                            p1turn = True
                            break
                    if not p1turn:
                        for i in range(9):
                            ai_table = table.copy()
                            win_move = False
                            if table[i] == cross or table[i] == circle:
                                continue
                            ai_table[i] = cross
                            win_move = is_win(ai_table)
                            if win_move:
                                table[i] = circle
                                os.system('clear')
                                printBoard(table)
                                p1turn = True
                                break
                        ai_choice = random.randint(0, 8)
                        if table[ai_choice] == cross or table[ai_choice] == circle:
                            continue
                        elif p1turn:
                            break
                        if table[4] != circle and table[4] != cross:
                            table[4] = circle
                            os.system('clear')
                            printBoard(table)
                            p1turn = True
                        else:
                            table[ai_choice] = circle
                            os.system('clear')
                            printBoard(table)
                            p1turn = True
            else:
                print(colored(str(p2) + "\'s turn! \n", "blue"))
                try:
                    p2_choice = int(input(colored("Enter a number: ", "blue")))
                    if p2_choice < 1 or p2_choice > 9:
                        giveError()
                        continue
                    elif table[p2_choice - 1] == cross or table[p2_choice - 1] == circle:
                        giveIllegalMove()
                        continue
                    else:
                        table[p2_choice - 1] = circle
                        os.system('clear')
                        printBoard(table)
                        p1turn = True
                except ValueError:
                    giveError()
                    continue
        win = is_win(table, win)
        tie = is_tie(table, tie, win)
    winmsg(tie, p1turn, p1, p2)
    restart(p1, p2)


def printBoard(table):
    print('\
 ┌───┬───┬───┐\n\
 │ {0} │ {1} │ {2} │\n\
 ├───┼───┼───┤\n\
 │ {3} │ {4} │ {5} │\n\
 ├───┼───┼───┤\n\
 │ {6} │ {7} │ {8} │\n\
 └───┴───┴───┘ '.format(*table))


player1score = 0
player2score = 0
welcome()
main(input_p1(), input_p2())
