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
                if(action == 'a'):
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
                        try:
                            gameNum = int(action)
                            if(gameNum <= 0 or gameNum >len(self.games)):
                                raise Exception('Invalid Input')
                            flag = True
                        except:
                            print("Invalid Input, please try again.")
                elif(action == 'b'):
                    gameNum = random.randint(1, len(self.games))
                    currentState = 'GM'
                    prevState = 'MM'
                    self.games[gameNum-1].play_game()
                elif(action == 'c'):
                    print('\n-----------------------------------------------------------\nCredits')
                    print('    > Alexander So - Main Menu and Game Connection Logic; Host Class')
                    print('    > Clint Smith - Rock Paper Scissors Game; RPS Class')
                    print('    > Garret Sumpter - ')
                    print('    > Zane Aschenbeck - ')
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
                    self.printMain()
                    action = self.processInput()
                




gameService = Host(RPS())

gameService.start()