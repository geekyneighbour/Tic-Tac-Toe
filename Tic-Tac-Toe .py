class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self):
        n = input(f'Игрок {self.name}, введите координаты x, y от одного до трех через пробел: ').split()
        while any(not i.isdigit() for i in n) or any(not 1 <= int(i) <= 3 for i in n):
            n = input(f'Игрок {self.name}, введите координаты x, y от одного до трех через пробел: ').split()
        return list(map(lambda x: int(x) - 1, n))


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.field = [[1 for _ in range(3)] for _ in range(3)]

    def check_choice(self, coord):
        if coord is not None:
            x, y = coord[0], coord[1]
            if self.field[x][y] == 1:
                return True
        return False

    def check_field(self, lst):
        lst1 = [[lst[j][i] for j in range(3)] for i in range(3)]
        for i in lst:
            if i.count('0') == 3:
                return '0'
            if i.count('X') == 3:
                return 'X'
        for i in lst1:
            if i.count('0') == 3:
                return '0'
            if i.count('X') == 3:
                return 'X'
        return None

    def play(self):
        choice1 = self.player1.choose()
        choice2 = self.player2.choose()
        if not self.check_choice(choice1):
            choice1 = self.player1.choose()
        self.field[choice1[0]][choice1[1]] = self.player1.name
        if not self.check_choice(choice2):
            choice2 = self.player1.choose()
        self.field[choice2[0]][choice2[1]] = self.player2.name
        self.win()

    def win(self):
        n = self.check_field(self.field)
        if n is None:
            self.play()
        else:
            print(f'Победил(-а) {n}')


def want_play():
    player1 = Player('X')
    player2 = Player('0')
    game = Game(player1, player2)
    game.win()
    answer = input('Сыграем еще? Y/N: ')
    while answer == 'Y':
        return want_play()



want_play()

