import random
import Optional
from .dataclassPassShot import Shot, Pass


MIN_SHOT_POWER = 1
MAX_SHOT_POWER = 100
MIN_SAVE_DIFFICULTY = 1
MAX_SAVE_DIFFICULTY = 711


class ShotEngine:

    @staticmethod
    def shot(idTeam, HomeTeam, idActivePlayerIdTeam, GuestTeam, idActivePlayerOtherTeam, history):

        eventShot = Shot

        # Добавление рандома к процессу удара
        shotPlayer = random.randint(MIN_SHOT_POWER, MAX_SHOT_POWER - idTeam * 10)
        saveGoalKeaper = random.randint(MIN_SAVE_DIFFICULTY, MAX_SAVE_DIFFICULTY + idTeam * 10)

        eventShot.homeXGs = shotPlayer / 1000
        eventShot.homeShots = 1
        eventShot.homeGoal = 0
        eventShot.guestGoal = 0

        shot = Shot(
            shooter_id=shooter.id,
            goalkeeper_id=goalkeeper.id,
            xg=xg,
            on_target=on_target,
            is_goal=is_goal,
        )

        # Сокращение переменных
        skillShot = HomeTeam.players[idActivePlayerIdTeam].skillShot
        skillSave = GuestTeam.players[GuestTeam.idSostav[0]].skillSave

        # Если удар точен
        if (shotPlayer + skillShot) > (skillSave + saveGoalKeaper):
            eventShot.homeShotsTo = 1
            # По индексу определяем кому прибавлять гол
            if idTeam:
                eventShot.guestGoal = 1
                eventShot.whoScoreGuest = idActivePlayerIdTeam
            else:
                eventShot.homeGoal = 1
                eventShot.whoScoreHome = idActivePlayerIdTeam

            # Прибавляем команде 1 забитый гол
            HomeTeam.goals += 1

            # Прибавляем команде 1 пропущенный гол
            GuestTeam.loseGoals += 1
            history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} бьёт.... ГОООООООЛ!!!!')

            # Прибавляем игроку 1 забитый гол
            HomeTeam.players[idActivePlayerIdTeam].goals += 1

            # Возвращаем индекс пропустившей команды, и разыгрывающего игрока
            return [(idTeam + 1) % 2, 6], HomeTeam, GuestTeam, history, Shot

        # Если удар не точен
        else:
            # Добавляем рандома к процессу сейва
            t = 1 + random.randint(1, 10)

            # Если вратарь отбил то прибаляем вратарю сейв, иначе игрок ударил мимо
            if t >= 9:
                eventShot.homeShotsTo = 1
                GuestTeam.players[GuestTeam.idSostav[0]].saves += 1
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} бьёт... '
                                    f'{GuestTeam.players[GuestTeam.idSostav[0]].name} отбивает!')
            else:
                history.append(f'{HomeTeam.players[idActivePlayerIdTeam].name} бьёт... МИМО!!')

            # Возвращаем команду у которой мяч и номер позиции
            return [(idTeam + 1) % 2, 1], HomeTeam, GuestTeam, history, Shot
