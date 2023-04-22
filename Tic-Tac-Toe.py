class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self):
        n = input(f'Игрок {self.name}, введите координаты x, y от одного до трех через пробел: ').split()
        if any(not i.isdigit() for i in n) or any(not 1 <= int(i) <= 3 for i in n) or len(n) == 1 or not n:
            return self.choose()
        return list(map(lambda x: int(x) - 1, n))


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.field = [['*' for _ in range(3)] for _ in range(3)]

    def check_choice(self, coord, name):
        x, y = coord[0], coord[1]
        if self.field[x][y] == '*':
            self.field[x][y] = name
            m = self.win()
            print('Вот текущее поле:')
            for i in self.field:
                print(*i)
            if m is None:
                return True
            return m
        return False


    def check_field(self, lst):
        lst1 = [[lst[j][i] for j in range(3)] for i in range(3)]
        for i in lst:
            if i.count('O') == 3:
                return 'O'
            if i.count('X') == 3:
                return 'X'
        for i in lst1:
            if i.count('O') == 3:
                return 'O'
            if i.count('X') == 3:
                return 'X'
        return None

    def play(self):
        choice = self.player1.choose()
        check = self.check_choice(choice, self.player1.name)
        while not check:
            print(f'Игрок {self.player1.name}, такие координаты уже были!')
            choice = self.player1.choose()
            check = self.check_choice(choice, self.player1.name)
        if type(check) == str:
            print(check)
            return True
        else:
            choice = self.player2.choose()
            check = self.check_choice(choice, self.player2.name)
            while not check:
                print(f'Игрок {self.player2.name}, такие координаты уже были!')
                choice = self.player2.choose()
                check = self.check_choice(choice, self.player2.name)
            if type(check) == str:
                print(check)
                return True
            else:
                self.play()

    def win(self):
        n = self.check_field(self.field)
        if n is not None:
            return f'Победил(-а) {n}'


def want_play():
    player1 = Player('X')
    player2 = Player('O')
    game = Game(player1, player2)
    game.play()
    answer = input('Сыграем еще? Y/N: ')
    while answer in 'yY':
        return want_play()


want_play()

