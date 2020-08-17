class Dog:
    def __init__(self, name, color, breed = 'mixed breed', size = 'unknown'):
        self.name = name
        self.color = color
        self.breed = breed
        self.size = size
    
    def print_dog(self):
        print(self.name + ' is a ' + self.breed + ', has ' + self.color + ' hair, and ' + self.size + ' size.')
        
    def change_breed(self, breed):
        self.breed = breed
        
    def change_color(self, color):
        self.color = color

    def change_name(self, name):
        self.name = name
        
    def change_size(self, size):
        self.size = size    

bobby = Dog('Bobby', 'white')
bobby.print_dog()

bobby.change_breed('maltesse')
bobby.change_size('small')
bobby.print_dog()

lilly = Dog('Lilly', 'black', 'poodle', 'small')
lilly.print_dog()





