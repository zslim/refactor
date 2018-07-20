import random
import os


def generateTable():
    table = []
    for x in range(0, 9):
        table.append(str(x + 1))
    return table


def is_win(table, win=False):
    if ((table[0] == table[4] and table[0] == table[8]) or
            (table[2] == table[4] and table[4] == table[6])):
        win = True
    else:
        for x in range(0, 3):
            y = x * 3
            if ((table[y] == table[(y + 1)] and table[y] == table[(y + 2)]) or
                    (table[x] == table[(x + 3)] and table[x] == table[(x + 6)])):
                win = True
    if win:
        os.system('clear')
        printBoard(table)
    return win


def is_tie(table, win, tie = False):
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


def winmsg(tie, player_1_turn, player_1_name, player_2_name):
    global player1score, player2score
    if tie:
        print(colored("It's a tie!\n", "yellow"))
        os.system('spd-say "It\'s a tie"')
    else:
        if player_1_turn:
            if player_2_name.upper() == 'AI':
                os.system('spd-say -r -50 "haa haa haa silly hooman you lost ha ha ha"')
                player2score += 1
                print(colored(player_2_name + " wins!       ツ\n", "blue"))
            else:
                os.system('spd-say -r -50 "Player 2 wins"')
                print(colored("Congratulations!\n", "yellow"))
                player2score += 1
                print(colored(player_2_name + " wins!       ツ\n", "blue"))

        else:
            print(colored("Congratulations!\n", "yellow"))
            print(colored(player_1_name + " wins!       ツ\n", "red"))
            os.system('spd-say -r -50 "Player 1 wins"')
            player1score += 1


def giveError():
    print(colored("Must be a number between 1 and 9!\n", "yellow"))


def giveIllegalMove():
    print(colored("\nThat number is already taken, chose another!\n", "yellow"))


def welcome():
    os.system('clear')
    print(colored("Welcome to our ToeTacTic demo!\n", "yellow"))


def restart(player_1_name, player_2_name):
    print(colored("The score is: \n", "light blue"))
    print(colored(str(player_1_name) + ": " + str(player1score), "red"))
    print(colored(str(player_2_name) + ": " + str(player2score), "blue"))
    again = input(colored("\nPress (Y) to play again or (any key) to quit! \n", "light blue"))
    if again[0].upper() == 'Y':
        try:
            os.system('clear')
            main(player_1_name, player_2_name)
        except IndexError:
            quit()
    else:
        os.system('clear')
        if player1score > player2score:
            print(colored(str(player_1_name) + " wins!\n", "red"))
        elif player1score == player2score:
            print(colored("\nIt's a tie!\n", "yellow"))
        else:
            print(colored("\n" + str(player_2_name) + " wins!\n", "blue"))
        print(colored(str(player1score), "red") + " : " + colored(str(player2score) + "\n", "blue"))
        print(colored("\nGood bye!\n", "yellow"))
        os.system('spd-say -r -50 "Good bye"')
        quit()


def input_player_1_name():
    os.system('spd-say -r -50 "What is your name human?"')
    player_1_name = input(colored("First player's name: \n", "red"))
    return player_1_name


def input_player_2_name():
    player_2_name = input(colored("Second player's name: (Type 'AI' to play against the AI) \n", "blue"))
    return player_2_name


def main(player_1_name, player_2_name):
    table = generateTable()
    player_1_turn = True
    tie = False
    win = False
    circle = colored("◉", "blue")
    cross = colored("✘", "red")
    player_1_name = player_1_name
    player_2_name = player_2_name
    os.system('clear')
    printBoard(table)
    if player_2_name.upper() == 'AI':
        os.system('spd-say -r -50 "i let you go first human wink wink"')
    while not win and not tie:
        if player_1_turn:
            print(colored(str(player_1_name) + "\'s turn!\n", "red"))
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
                    player_1_turn = False
            except ValueError:
                giveError()
                continue
        else:
            if player_2_name.upper() == 'AI':
                while not player_1_turn:
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
                            player_1_turn = True
                            break
                    if not player_1_turn:
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
                                player_1_turn = True
                                break
                        ai_choice = random.randint(0, 8)
                        if table[ai_choice] == cross or table[ai_choice] == circle:
                            continue
                        elif player_1_turn:
                            break
                        if table[4] != circle and table[4] != cross:
                            table[4] = circle
                            os.system('clear')
                            printBoard(table)
                            player_1_turn = True
                        else:
                            table[ai_choice] = circle
                            os.system('clear')
                            printBoard(table)
                            player_1_turn = True
            else:
                print(colored(str(player_2_name) + "\'s turn! \n", "blue"))
                try:
                    player_2_choice = int(input(colored("Enter a number: ", "blue")))
                    if player_2_choice < 1 or player_2_choice > 9:
                        giveError()
                        continue
                    elif table[player_2_choice - 1] == cross or table[player_2_choice - 1] == circle:
                        giveIllegalMove()
                        continue
                    else:
                        table[player_2_choice - 1] = circle
                        os.system('clear')
                        printBoard(table)
                        player_1_turn = True
                except ValueError:
                    giveError()
                    continue
        win = is_win(table, win)
        tie = is_tie(table, win, tie)
    winmsg(tie, player_1_turn, player_1_name, player_2_name)
    restart(player_1_name, player_2_name)


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
main(input_player_1_name(), input_player_2_name())
