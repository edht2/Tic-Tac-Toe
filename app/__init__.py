from app.main import TicTacToe

def start_game():
    """ Creates game object and executes main game loop """
    
    game = TicTacToe()
    
    while True:
        
        game.display()
        game.turn()
        
        if game.evaluate():
            game.display()
            break