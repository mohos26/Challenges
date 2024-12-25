# https://edabit.com/challenge/dLnZLi8FjaK6qKcvv
# Hard
# 10.09.2024


class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if not self.words or (not self.game_over and self.words[-1][-1] == word[0] and word not in self.words):
            self.words.append(word)
            return self.words
        self.game_over = True
        return 'game over'

    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'
