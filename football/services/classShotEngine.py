import random
from .dataclassPassShot import Shot, Pass


MIN_SHOT_POWER = 1
MAX_SHOT_POWER = 100
MIN_SAVE_DIFFICULTY = 1
MAX_SAVE_DIFFICULTY = 711


class ShotEngine:

    @staticmethod
    def shot(idTeam, shooter, goalkeeper):
        shotPlayer = random.randint(MIN_SHOT_POWER, MAX_SHOT_POWER - idTeam * 10)
        saveGoalKeaper = random.randint(MIN_SAVE_DIFFICULTY, MAX_SAVE_DIFFICULTY + idTeam * 10)

        shot = Shot(
            shooter=shooter,
            goalkeeper_id=goalkeeper,
            xg=shotPlayer / 1000,
            shot=0,
            shot_on_target=0,
            is_goal=0,
            history=''
        )

        if (shotPlayer + shooter.skillShot) > (goalkeeper.skillSave + saveGoalKeaper):
            shot.shot_on_target = 1
            shot.is_goal = 1
            shooter.goals += 1

            shot.history = f'{shooter.name} бьёт.... ГОООООООЛ!!!!'
        else:
            t = 1 + random.randint(1, 10)

            if t >= 9:
                shot.shot_on_target = 1
                goalkeeper.saves += 1
                shot.history = (f'{shooter.name} бьёт... \n'
                                f'{goalkeeper.name} отбивает!')
            else:
                shot.history = f'{shooter.name} бьёт... МИМО!!'

        return shot
