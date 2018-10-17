class animal:

    def eat(self):
        print('eat')

    def drink(self):
        print ('drink')

    def caca(self):
        print('faire caca')

    def pi(self):
        print ('pi')


class cat(animal):
    def __init__(self, name):
        self.name = name
        self.breed = 'cat'

    def cry(self):
        print('miao')

    def detail(self):
        print (self.name, self.breed)


class dog(animal):
    def __init__(self, name):
        self.name = name
        self.breed = 'dog'

    def cry(self):
        print('wang')


dog1 = dog('wudong')
cat1 = cat('gulu')
dog1.cry()
dog1.eat()
cat1.drink()
cat1.cry()
cat1.detail()