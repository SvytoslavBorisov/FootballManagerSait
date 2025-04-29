from .classGame import Game
import os


# Класс лиги
class Liga:
    def __init__(self, teams, globalNumberSeason):
        # Количество команд в лиги
        self.countTeams = len(teams)
        # Расписание игр(какая команда с какой)
        self.timetable = []
        # Номер сезона в глобале
        self.globalNumberSeason = globalNumberSeason
        # Открываем файл с расписанием, считываем расписания для countTeams
        with open(f'{os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')), 'static')}\\football\schedules\GamesX{self.countTeams}.txt', 'r') as f:
            for i in range((2 * self.countTeams - 1)):
                for j in range(self.countTeams // 2):
                    st = f.readline()[:-1].split()
                    if st:
                        self.timetable.append([int(st[0]), int(st[1])])
                f.readline()

        # Список команд - участниц
        self.teams = teams
        # Текущий тур
        self.tourNow = 0
        # Список игр
        self.games = []
        # Список всех игроков, всех команд
        self.allPlayers = []
        for i in range(self.countTeams):
            self.allPlayers += self.teams[i].players

    # Проиграть 1 тур сезона
    def playTour(self):
        # Если тур не последний
        if self.tourNow != (self.countTeams - 1) * 2:
            gamesTemp = []
            # Идем по расписанию, составляя матчи по нему
            for teams in self.timetable[self.tourNow * (self.countTeams // 2): (self.tourNow + 1) * (self.countTeams // 2)]:
                # Создаем игру с 2 командами из расписания
                game = Game(self.teams[teams[0] - 1], self.teams[teams[1] - 1])
                # Выбираем состав
                game.choiceSelection()
                # Играем матч
                game.match()
                # Добавляем сыгранный матч в архив сезона
                gamesTemp.append(game)
                self.teams[teams[0] - 1].arrayOfGames.append(game)
                self.teams[teams[1] - 1].arrayOfGames.append(game)
            self.games.append(gamesTemp)

    def findGameForIds(self, ids):
        for j in range(self.tourNow):
            for i in range(len(self.games[j])):
                if ids == self.games[j][i].ids:
                    return self.games[j][i]
        return None

    def findGameForNames(self, name1, name2):
        id1, id2 = 1, 2
        for i in range(len(self.teams)):
            if self.teams[i].name == name1:
                id1 = self.teams[i].id
            if self.teams[i].name == name2:
                id2 = self.teams[i].id
        return self.findGameForIds([id1, id2])
