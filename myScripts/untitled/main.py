class GameEntry():
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def __str__(self):
        return '{0} : \t{1}'.format(self._name, self._score)

    def get_score(self):
        return self._score

    def get_name(self):
        return self._name

class Scoreboard():
    length = 5
    all_scores = [GameEntry('Untitled', 0) for i in range(length)]

    def new(self, game_entry):
        if (Scoreboard.check_if_highest(game_entry._score)):
            Scoreboard.put_in_order(game_entry)

    def __init__(self, game_entry):
        if (Scoreboard.check_if_highest(game_entry._score)):
            Scoreboard.put_in_order(game_entry)

    def __str__(self):
        return '\n'.join([str(i._name) + '\t' + str(i._score) for i in Scoreboard.all_scores])

    @classmethod
    def check_if_highest(cls, score):
        for i in range(cls.length):
            if cls.all_scores[i]._score < score:
                return True
        return False

    @classmethod
    def move_forward(cls, arr, n, num):
        arr_new = [0 for i in range(len(arr) + 1)]
        for i in range(len(arr)):
            if i < n:
                arr_new[i] = arr[i]
            elif i == n:
                arr_new[i] = num
                arr_new[i + 1] = arr[i]
            else:
                arr_new[i + 1] = arr[i]
        return arr_new

    @classmethod
    def put_in_order(cls, score):
        for i in range(cls.length):
            if score._score > cls.all_scores[i]._score:
                cls.all_scores = Scoreboard.move_forward(cls.all_scores, i, score)
                cls.all_scores.pop()
                return

    def get_all_scores(self):
        return Scoreboard.all_scores

s = Scoreboard(GameEntry('Sanil', 100))
s.new(GameEntry('Sanil2', 50))
s.new(GameEntry('Sanil3', 70))
print(s)
