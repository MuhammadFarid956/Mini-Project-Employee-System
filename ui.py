import os

class AppUI:
    def __init__(self, manager):
        self.manager = manager

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    



