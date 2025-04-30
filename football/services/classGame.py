from .dataclassPassShot import Pass, Shot
from football.services.classPassEngine import PassEngine


class Game:
    def __init__(self, team1, team2):
        # Текущая минута матча
        self.minute = 1
        # Количество мячей, которая забила 1 / 2 команда
        self.homeGoal = 0
        self.guestGoal = 0
        # У какого игрока мяч в данный момент (0 - НomeTeam, 1 - GuestTeam; 1,2,3,4,5,6,7,8,9,10,11 - Позиции на поле)

        #               11(ST)
        #
        #        8(LW)  9(AM)  10(RW)
        #
        #            6(CM) 7(CM)
        #
        #      2(LD) 3(DC) 4(DC) 5(RB)
        #
        #                1(GK)

        self.WhichBall = [0, 0]
        # Вероятность паса одной позиции на другую
        self.positionsOptionsToPass = [[0, 400, 800, 900, 1000, 1050, 1075, 1085, 1095, 1097, 1000, 1000],
                                       [50, 50, 200, 250, 350, 550, 700, 1000, 1005, 1015, 1018, 1025],
                                       [100, 400, 400, 500, 530, 830, 930, 950, 970, 990, 1000, 1050],
                                       [100, 130, 230, 230, 530, 830, 930, 950, 970, 990, 1000, 1050],
                                       [50, 70, 105, 305, 305, 505, 605, 610, 910, 915, 935, 942],
                                       [10, 110, 130, 150, 250, 250, 750, 850, 950, 980, 1010, 1080],
                                       [10, 110, 130, 150, 250, 750, 750, 850, 950, 980, 1010, 1080],
                                       [1, 31, 41, 54, 84, 199, 299, 299, 399, 699, 999, 1099],
                                       [1, 116, 131, 141, 154, 254, 554, 599, 599, 899, 1000, 1100],
                                       [1, 14, 24, 39, 154, 254, 554, 599, 699, 699, 1000, 1100],
                                       [0, 1, 11, 25, 40, 155, 255, 305, 405, 505, 505, 1005]
                                       ]
        # 2 команды, которые играют между собой
        self.teams = [team1, team2]
        self.ids = [team1.id, team2.id]
        self.structures = [[], []]
        self.whoScoreHome = []
        self.whoScoreGuest = []
        self.history = []
        self.mainHistory = []
        self.xgs = [0, 0]
        self.shoots = [0, 0]
        self.shoots_to = [0, 0]
        self.control = [0, 0]

    # Выбор состава для 2 играющих команд
    def choiceSelection(self):
        # Цикл по 2 командам (1 и 2)
        for j in range(2):
            # Максимальный уровень команды
            maxSkills = 0
            # Индексы игроков для максимального уровня
            dataOfIdMax = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            # Цикл по позициям (11 позиций в футболе)
            for k in range(0, 11):
                # Обнуление активных игроков(все игроки доступны)
                self.teams[j].zeroingOfPlayersActive()
                # Временный максимальный уровень команды
                maxSkillsTEMP = 0
                # Временный список индексов игроков для максимального уровня
                dataOfIdMaxTEMP = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                # Цикл от k позиции до 11
                for i in range(k, 11):
                    # Получения (индекса игрока, максимального значения позиции) для определенной позиции
                    idTemp, skillTemp = self.teams[j].choicePlayer(i)
                    # Сохраняем значение во временное значение
                    maxSkillsTEMP += skillTemp
                    # Сохраняем индекс во временный список
                    dataOfIdMaxTEMP[i] = idTemp
                    # Устанавливаем для выбранного игрока ACTIVE = True, чтобы его больше нельзя было использовать в оставшихся позициях
                    self.teams[j].players[idTemp].active = True

                # Цикл от 0 до k позиции
                for i in range(0, k):
                    # Получения (индекса игрока, максимального значения позиции) для определенной позиции
                    idTemp, skillTemp = self.teams[j].choicePlayer(i)
                    # Сохраняем значение во временное значение
                    maxSkillsTEMP += skillTemp
                    # Сохраняем индекс во временный список
                    dataOfIdMaxTEMP[i] = idTemp
                    # Устанавливаем для выбранного игрока ACTIVE = True, чтобы его больше нельзя было использовать в оставшихся позициях
                    self.teams[j].players[idTemp].active = True
                # Если временное значение оказалось больше, чем максимальный уровень, то заменяем
                if maxSkills < maxSkillsTEMP:
                    maxSkills = maxSkillsTEMP
                    dataOfIdMax = dataOfIdMaxTEMP
            # Передаем команде индексы игроков, которые будут играть в матче
            self.teams[j].idSostav = list(dataOfIdMax)
            self.structures[j] = list(dataOfIdMax)

    # Проиграть 1 матч между 2 командами
    def match(self):

        # Home team 0/ NumberPosition 6
        self.whichBall = [0, 6]
        if self.whichBall[0]:
            self.control[0] += 1
        else:
            self.control[1] += 1

        # Проход по каждой минуте матча (540 - для большей реалистичности итогового результата)
        while self.minute < 540:
            # Для сокращения названия переменных
            wb = self.whichBall[0]
            wb1 = self.whichBall[1]
            # Мяч перемещяется на другую позицию
            self.whichBall, self.teams[wb], self.teams[(wb + 1) % 2], self.history, event = PassEngine.passTo(wb, self.teams[wb], wb1,
                                         self.teams[(wb + 1) % 2], 11 - wb1)  # id игрока - сопреника и его позиция
            if wb == 0:
                self.xgs[0] += event.homeXGs
            elif wb == 1:
                self.xgs[1] += event.homeXGs

            self.homeGoal += event.homeGoal
            self.guestGoal += event.guestGoal

            #self.mainHistory.append((f'{self.teams[].players[idActivePlayerIdTeam].name} ГОЛ', idTeam, self.minute))
            if self.whichBall[0]:
                self.control[0] += 1
            else:
                self.control[1] += 1

            # Прибавляем минуту
            self.minute += 1

        # self.teams[0].zeroingPhysic()
        # self.teams[1].zeroingPhysic()
        # Если у 1 команды больше голов, чем у 2, победа присуждается 1
        if self.homeGoal > self.guestGoal:
            self.teams[0].wins += 1
            self.teams[1].defeats += 1
            # За победу присуждается 3 очка
            self.teams[0].points += 3

        # Если у 2 команды больше голов, чем у 1, победа присуждается 2
        elif self.homeGoal < self.guestGoal:
            self.teams[1].wins += 1
            self.teams[0].defeats += 1
            # За победу присуждается 3 очка
            self.teams[1].points += 3

        # Если у 2 команды столько же голов, сколько у 1, ничья
        else:
            self.teams[1].draws += 1
            self.teams[0].draws += 1

            # За ничью присуждается по 1 очку
            self.teams[1].points += 1
            self.teams[0].points += 1

        # Увеличиваем общее количество игр у каждой команды
        self.teams[0].games += 1
        self.teams[1].games += 1

    def returnResult(self):
        return f'{self.homeGoal}:{self.guestGoal}'

    def returnSostav(self):
        stTemp = ''
        dataPlayer1Team = []
        dataPlayer2Team = []
        for i in range(11):
            dataPlayer1Team.append(self.teams[0].returnPlayerOnPosition(i))
            dataPlayer2Team.append(self.teams[1].returnPlayerOnPosition(i))
        maxLenPlayer = max(dataPlayer1Team, key=lambda x: len(x))
        for i in range(11):
            stTemp += dataPlayer1Team[i] + ' ' * (10 + len(maxLenPlayer) - len(dataPlayer1Team[i])) + dataPlayer2Team[i] + '\n'

        return stTemp

    def to_json(self):
        self.returnSostav()
        ids_home = [self.structures[0][i] for i in range(11)]
        sostav_home = []
        for y in ids_home:
            for i, x in enumerate(self.teams[0].players):
                if i == y:
                    sostav_home.append(x.name)

        ids_guest = [self.structures[1][i] for i in range(11)]
        sostav_guest = []
        for y in ids_guest:
            for i, x in enumerate(self.teams[1].players):
                if i == y:
                    sostav_guest.append(x.name)

        return {
            'id': f'{self.ids[0]},{self.ids[1]}',
            'home_team': self.ids[0],
            'home_team_name': self.teams[0].name,
            'guest_team': self.ids[0],
            'guest_team_name': self.teams[1].name,
            'home_team_goals': self.homeGoal,
            'guest_team_goals': self.guestGoal,
            'home_lineup': sostav_home,
            'guest_lineup': sostav_guest,
            'who_score_home': {x[0]: x[2] for x in self.mainHistory if x[1] == 0},
            'who_score_guest': {x[0]: x[2] for x in self.mainHistory if x[1] == 1},
            'stats': {"XG": { "home": self.xgs[0], "away": self.xgs[1]},
                      "Удары": { "home": self.shoots[0], "away": self.shoots[1]},
                      "Удары в створ": { "home": self.shoots_to[0], "away": self.shoots_to[1]},
                      "Владение": {"home": int((self.control[0] / 540) * 100), "away": int((self.control[1] / 540) * 100)}},
            "events": [{"minute": x[2], "team": x[1], "description": x[0]} for x in self.mainHistory]
        }


