# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Clint Smith
#               Garret Sumpter
#               Zane Aschenback
#               Alex So
# Section:      573
# Assignment:   12
# Date:        9 11 2024
import random

class RPS:

    title = 'Rock Paper Scissors'

    #computers choice using random
    def computer(self):
        choices = ['Rock', 'Paper', 'Scissors']
        return random.choice(choices)
    #user input make normal then put capital at front to match formatting
    def user(self):
        return input('Enter Rock, Paper, or Scissors (use "stop" to end the game at any time): ').strip().capitalize()
    #determine the winner using user choice and computer choice
    def winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'Y\'all tied'
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Paper' and computer_choice == 'Rock') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper'):
            return 'You win :)'
        else:
            return 'You lost :('
    #use previous definitions and play the game
    def play_game(self):
        print('Lets play Rock-Paper-Scissors!')
        
        while True:
            user_choice = self.user()
            #quit game
            if user_choice.lower() == 'stop':
                print('Thank you for playing!')
                break
            #invalid option
            if user_choice not in ['Rock', 'Paper', 'Scissors']:
                print('Invalid choice. Give it another shot!')
                continue
            
            comp_choice = self.computer()
            #choices
            print(f'You chose: {user_choice}')
            print(f'Computer chose: {comp_choice}')
            #print winner
            result = self.winner(user_choice, comp_choice)
            print(result)
            print('-----------------------------------------------------------')

class TTT:
    title = "Tic Tac Toe"

    # create blank board
    def make_board(self, board):
        for i in range(3):
            print(" | ".join(board[i]))
            if i < 2:  # don't print dashes for the last line
                print("-" * 9)

    # declares winner once line is made
    def winner(self, board, player):
        for row in board:
            if row[0] == row[1] == row[2] == player:
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    # create tic-tac-toe
    def play_game(self):
        myBoard = [[" "] * 3 for i in range(3)]  # Create an empty board
        player = "X"  # Starting player
        counter = 0

        while True:
            counter += 1
            self.make_board(myBoard)  # Show the board
            placement = input(f"Player {player}, enter row and column separated by a space (first row and column are index 0) or type 'stop' to quit: ")

            if placement.lower() == 'stop':  # Allow the player to stop the game
                print("Exiting Tic-Tac-Toe...")
                break

            # input validation
            flag = False
            while not flag:
                try:
                    row, col = map(int, placement.split())
                    if row < 0 or row > 2 or col < 0 or col > 2:
                        raise ValueError("Row and column must be between 0 and 2.")
                    flag = True
                except ValueError as e:
                    print(f"Invalid input. {e}. Try again.")
                    placement = input(f"Player {player}, enter row and column separated by a space (first row and column are index 0) or type 'stop' to quit: ")
                    if placement.lower() == 'stop':  # If player wants to stop during input phase
                        print("Exiting Tic-Tac-Toe...")
                        return  # Exit the game and return to main menu

            if myBoard[row][col] == " ":
                myBoard[row][col] = player
                if self.winner(myBoard, player):
                    self.make_board(myBoard)
                    print(f"Player {player} wins! Congratulations!")
                    break
                tie = True
                for row in myBoard:
                    for cell in row:
                        if cell == " ":
                            tie = False
                if tie:
                    self.make_board(myBoard)
                    print("It's a tie!")
                    break
                player = "O" if player == "X" else "X"  # Switch players
            else:
                print("Cell occupied. Try again.")


class Trivia:
    title = "TAMU Trivia"
    
    def play_game(self):
        # Trivia game
        score = 0

        # Question 1
        print('What year was Lawrence Sullivan Ross Born?')
        print(' a: 1833\n b: 1838\n c: 1890\n d: 1852')
        ans1 = input('Enter letter answer here: ')
        if ans1.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans1 == 'b':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Question 2
        print('When was the college of A&M established?')
        print(' a: 1852\n b: 1876\n c: 1863\n d: 1862')
        ans2 = input('Enter letter answer here: ')
        if ans2.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans2 == 'd':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Question 3
        print('What day of the week was A&M opened for instruction?')
        print(' a: Tuesday\n b: Thursday\n c: Wednesday\n d: Friday\n')
        ans3 = input('Enter letter answer here: ')
        if ans3.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans3 == 'c':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Question 4
        print('What is NOT a Core Value of Texas A&M')
        print(' a: Excellence\n b: Courage\n c: Leadership\n d: Respect\n')
        ans4 = input('Enter letter answer here: ')
        if ans4.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans4 == 'b':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Question 5
        print('At what time did the bonfire stack collapse?')
        print(' a: 2:42\n b: 4:28\n c: 3:57\n d: 1:30\n')
        ans5 = input('Enter letter answer here: ')
        if ans5.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans5 == 'a':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Question 6
        print('How many Aggies served in World War II?')
        print(' a: 14,000\n b: 20,000\n c: 16,405\n d: Over 20,000\n')
        ans6 = input('Enter letter answer here: ')
        if ans6.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans6 == 'd':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Question 7
        print('When did Reveille originally join the ranks of Texas A&M?')
        print(' a: 1931\n b: 1940\n c: 1975\n d: 1890\n')
        ans7 = input('Enter letter answer here: ')
        if ans7.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans7 == 'a':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Question 8
        print('What is the date of Aggie Muster?')
        print(' a: April 27th\n b: April 19th\n c: March 21st\n d: April 21st\n')
        ans8 = input('Enter letter answer here: ')
        if ans8.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans8 == 'd':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Question 9
        print('When was the first game between Texas A&M and tu played?')
        print(' a: 1931\n b: 1899\n c: 1894\n d: 1902\n')
        ans9 = input('Enter letter answer here: ')
        if ans9.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans9 == 'c':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Question 10
        print('What class year was James Earl Rudder?')
        print(' a: 1949\n b: 1971\n c: 1911\n d: 1932\n')
        ans10 = input('Enter letter answer here: ')
        if ans10.lower() == 'stop':
            print('Exiting Trivia...')
            return  # Exit and return to main menu
        if ans10 == 'd':
            print('Correct')
            print()
            score += 1
        else:
            print('Incorrect')
            print()

        # Final score
        printscore = (f'| SCORE: {score * 10}%|')
        print('-' * len(printscore))
        print(printscore)
        print('-' * len(printscore))

        

class Host:
    games = []
    def __init__(self, *args):
        for game in args:
            self.games.append(game)
    
    def addGame(self, game):
        self.games.append(game)




    def printMain(self):
        print('-----------------------------------------------------------')
        print(f'Options:\nA > Show Game List\nB > Play Random Game\nC > View Credits')
        print('-----------------------------------------------------------')
    def processInput(self):
        return input('Enter Action, Type \'back\' to go Back, or Type \'stop\' to Stop. >>').lower()
    def showGameList(self):
        print('\n-----------------------------------------------------------\nGame List')
        i = 1
        for game in self.games:
            print(f'  {i} > {game.title}')
            i += 1
        print('-----------------------------------------------------------')


    def start(self):
        self.printMain()
        prevState = ''
        currentState = 'MM'
        
        action = self.processInput()


        while(action != 'stop'):
            if(currentState == 'MM'):
                prevState = 'MM'
                if(action == 'a'):#game list
                    currentState = 'GL'
                    self.showGameList()

                    flag = False
                    while(not flag):
                        action = self.processInput()
                        if(action == 'back'):
                            currentState = 'MM'
                            prevState = 'GL'
                            self.printMain()
                            action = self.processInput()
                            break
                        if(action == 'stop'):
                            break
                        try:
                            gameNum = int(action)
                            if(gameNum <= 0 or gameNum >len(self.games)):
                                raise Exception('Invalid Input')
                            flag = True
                        except:
                            print("Invalid Input, please try again.")
                elif(action == 'b'):#random game
                    gameNum = random.randint(1, len(self.games))
                    currentState = 'GM'
                    prevState = 'MM'
                    self.games[gameNum-1].play_game()
                elif(action == 'c'):#credits
                    print('\n-----------------------------------------------------------\nCredits')
                    print('    > Alexander So - Main Menu and Game Connection Logic; Host Class')
                    print('    > Clint Smith - Rock Paper Scissors Game; RPS Class')
                    print('    > Garret Sumpter - Trivia Game; Trivia Class')
                    print('    > Zane Aschenbeck - Tic Tac Toe Game; TTT Class')
                    print('-----------------------------------------------------------')
                    self.printMain()
                    action = self.processInput()
                else:
                    print('Invalid Input, please try again.')
                    action = self.processInput()


            elif(currentState == 'GL'):
                gameNum = int(action)
                prevState = 'GL'
                currentState = 'GM'
                self.games[gameNum-1].play_game()
                
            elif(currentState == 'GM'):
                if(prevState == 'GL'):
                    currentState = 'MM'
                    prevState = 'GM'
                    action = 'a'
                else:
                    currentState = 'MM'
                    prevState = 'GM'
                    self.printMain()
                    action = self.processInput()
                



#add games to host
gameService = Host(RPS())
gameService.addGame(TTT())
gameService.addGame(Trivia())
gameService.start()