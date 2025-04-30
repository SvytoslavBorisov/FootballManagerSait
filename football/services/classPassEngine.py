import random
from .classShotEngine import ShotEngine
from .dataclassPassShot import Shot, Pass


class PassEngine:
    positionsOptionsToPass = {'GK': [0, 400, 800, 900, 1000, 1050, 1075, 1085, 1095, 1097, 1000, 1000],
                              'LB': [50, 50, 200, 250, 350, 550, 700, 1000, 1005, 1015, 1018, 1025],
                              'LCD': [100, 400, 400, 500, 530, 830, 930, 950, 970, 990, 1000, 1050],
                              'RCD': [100, 130, 230, 230, 530, 830, 930, 950, 970, 990, 1000, 1050],
                              'RB': [50, 70, 105, 305, 305, 505, 605, 610, 910, 915, 935, 942],
                              'LCM': [10, 110, 130, 150, 250, 250, 750, 850, 950, 980, 1010, 1080],
                              'RCM': [10, 110, 130, 150, 250, 750, 750, 850, 950, 980, 1010, 1080],
                              'LW': [1, 31, 41, 54, 84, 199, 299, 299, 399, 699, 999, 1099],
                              'ACM': [1, 116, 131, 141, 154, 254, 554, 599, 599, 899, 1000, 1100],
                              'RW': [1, 14, 24, 39, 154, 254, 554, 599, 699, 699, 1000, 1100],
                              'ST': [0, 1, 11, 25, 40, 155, 255, 305, 405, 505, 505, 1005]}
    positionsToStr = {
        1: 'GK',
        2: 'LB',
        3: 'LCD',
        4: 'RCD',
        5: 'RB',
        6: 'LCM',
        7: 'RCM',
        8: 'LW',
        9: 'ACM',
        10: 'RW',
        11: 'ST'
    }

    @staticmethod
    def passTo(idTeam, HomeTeam, idActivePlayerIdTeam, GuestTeam, idActivePlayerOtherTeam):

        postionIdHome = PassEngine.positionsToStr[idActivePlayerIdTeam]

        history = []

        # Рандом к процессу отбора мяча
        otherPlayersSelection = 1 + random.randint(0, 40)
        randomPass = 1 + random.randint(0, 100)

        result = {'WhoBall': [0, 0]}
        event = Pass
        event.homeXGs = 0
        event.homeGoal = 0
        event.guestGoal = 0

        # Сокращение переменных
        skillSelection = GuestTeam.players[idActivePlayerOtherTeam].skillSelection  # Уровень отбора соперника
        skillPass = HomeTeam.players[idActivePlayerIdTeam].skillPass  # Уровень паса игрока

        # Проверяем, удачно ли игрок отдал пас
        if (skillSelection * 2 + otherPlayersSelection <= skillPass * 2 + randomPass) or skillPass == 1:  # если это вратарь
            # На какую позицию отдастся пас по процентному соотношению из positionsOptionsToPass
            playerPass = 1 + random.randint(1, PassEngine.positionsOptionsToPass[postionIdHome][-1])
            # Добавляем игроку 1 удачный пас
            HomeTeam.players[idActivePlayerIdTeam].allPass += 1
            HomeTeam.players[idActivePlayerIdTeam].correctPass += 1

            # Пас голкиперу и т.д.
            if (playerPass > 0) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][0]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[0]].name}')
                # Возвращаем команду у которой мяч и номер позиции, везде аналогично
                result['WhoBall'] = [idTeam, 1]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][0]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][1]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[1]].name}')
                result['WhoBall'] = [idTeam, 2]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][1]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][2]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[2]].name}')
                result['WhoBall'] = [idTeam, 3]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][2]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][3]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[3]].name}')
                result['WhoBall'] = [idTeam, 4]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][3]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][4]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[4]].name}')
                result['WhoBall'] = [idTeam, 5]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][4]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][5]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[5]].name}')
                result['WhoBall'] = [idTeam, 6]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][5]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][6]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[6]].name}')
                result['WhoBall'] = [idTeam, 7]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][6]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][7]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[7]].name}')
                result['WhoBall'] = [idTeam, 8]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][7]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][8]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[8]].name}')
                result['WhoBall'] = [idTeam, 9]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][8]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][9]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[9]].name}')
                result['WhoBall'] = [idTeam, 10]
            elif (playerPass > PassEngine.positionsOptionsToPass[postionIdHome][9]) and (playerPass < PassEngine.positionsOptionsToPass[postionIdHome][10]):
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{HomeTeam.players[HomeTeam.idSostav[10]].name}')
                result['WhoBall'] = [idTeam, 11]

            # Если не попало в пас, то будет произведён удар
            else:
                # Вычитаем 1 пас, так как игрок будет бить
                HomeTeam.players[idActivePlayerIdTeam].allPass -= 1
                HomeTeam.players[idActivePlayerIdTeam].correctPass -= 1
                # Обращаемся к функции удара, передаем команда, которая бьет, и бьющего игрока
                event = ShotEngine.shot(idTeam,
                                        HomeTeam.players[idActivePlayerIdTeam],
                                        GuestTeam.players[GuestTeam.idSostav[0]])
                history.append(event.history)

                if event.is_goal:
                    HomeTeam.goals += 1
                    GuestTeam.loseGoals += 1
                    result['WhoBall'] = [(idTeam + 1) % 2, 6]
                else:
                    result['WhoBall'] = [(idTeam + 1) % 2, 1]

                return result['WhoBall'], HomeTeam, GuestTeam, history, event

        # Если пас неудачен, то игрок другой команды произвел отбор
        else:
            # Прибавляем игроку потерю
            HomeTeam.players[idActivePlayerIdTeam].loseBall += 1
            history.append(f'{GuestTeam.players[idActivePlayerOtherTeam].name}'
                                f' отобрал мяч у {HomeTeam.players[idActivePlayerIdTeam].name}')
            # Прибавляем игроку отбор
            GuestTeam.players[idActivePlayerOtherTeam].selections += 1
            # Возвращаем команду у которой мяч и номер позиции
            result['WhoBall'] = [(idTeam + 1) % 2, idActivePlayerOtherTeam + 1]

        event = Pass(
            history='',
            is_goal=False,
            xg=0
        )

        return result['WhoBall'], HomeTeam, GuestTeam, history, event
