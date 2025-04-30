import pandas as pd


class Footballer:
    """
    Класс игрока, загружаемый из SQLite, с сырыми данными,
    рассчитанными FIFA-атрибутами и мастерством по позициям.
    """
    # Сырые поля, соответствующие FIELD_MAP
    RAW_FIELDS = [
        'player_id', 'full_name', 'first_name', 'last_name', 'age', 'date_of_birth', 'shirt_number',
        'squad_position', 'squad_position_detailed', 'contestantClubName', 'apps', 'mins_played',
        'goals', 'xg', 'np_goals', 'np_xg',
        'shots', 'shots_on_target', 'passes', 'successful_passes', 'pass_perc',
        'op_crosses', 'successful_op_crosses', 'cross_perc', 'xa', 'assists',
        'carries', 'dist_per_carry', 'tackles', 'interceptions', 'recoveries',
        'blocks', 'clearances', 'ground_duels', 'ground_duels_won',
        'ground_duel_perc', 'aerial_duels', 'aerial_duels_won', 'aerial_duel_perc',
        'yellows', 'reds', 'fouls_commited', 'pens_conceded', 'offsides', 'assists_minus_xa',
        'carry_end_assist','carry_end_moment', 'carry_end_goal','carry_end_shot', 'fifa_goals', 'fifa_physic'
    ]

    # Поля FIFA-атрибутов (вычислены ранее и сохранены в БД)
    FIFA_FIELDS = [
        'Acceleration','SprintSpeed','PaceAverage','Positioning','Finishing','ShotPower',
        'LongShots','Volleys','Penalties','ShootingAverage','Vision','Crossing','FKAccuracy',
        'ShortPassing','LongPassing','Curve','PassingAverage','Agility','Reactions','Balance',
        'Dribbling','BallControl','Composure','DribblingAverage','Interceptions','HeadingAccuracy',
        'DefAwareness','StandingTackle','SlidingTackle','DefenseAverage','Jumping','Stamina', 'Working foot',
        'Strength','Aggression','PhysicalAverage','GK_Diving','GK_Handling','GK_Kicking',
        'GK_Position','GK_Reflexes','GK_Average'
    ]
    # Формулы мастерства по позициям (список нужных атрибутов)
    POSITION_FORMULAS = {
        'GK':  ['GK_Diving','GK_Handling','GK_Kicking','GK_Position','GK_Reflexes','GK_Average'],
        'LB':  ['PaceAverage','DefenseAverage','PhysicalAverage','PassingAverage','DribblingAverage'],
        'CB1':  ['DefenseAverage','PhysicalAverage','Interceptions','HeadingAccuracy','StandingTackle'],
        'CB2': ['DefenseAverage', 'PhysicalAverage', 'Interceptions', 'HeadingAccuracy', 'StandingTackle'],
        'RB':  ['PaceAverage','DefenseAverage','PhysicalAverage','PassingAverage','DribblingAverage'],
        'CDM': ['DefenseAverage','PhysicalAverage','PassingAverage','Stamina','Aggression'],
        'CM':  ['PassingAverage','DribblingAverage','DefenseAverage','Stamina','PhysicalAverage'],
        'LW':  ['PaceAverage','DribblingAverage','ShootingAverage','PassingAverage','Agility'],
        'CAM': ['PassingAverage','DribblingAverage','ShootingAverage','Vision','Balance'],
        'RW':  ['PaceAverage','DribblingAverage','ShootingAverage','PassingAverage','Agility'],
        'ST':  ['ShootingAverage','PaceAverage','PhysicalAverage','DribblingAverage','HeadingAccuracy']
    }

    def __init__(self, row: pd.Series, team):
        # Присваиваем сырые поля как атрибуты
        for field in Footballer.RAW_FIELDS:
            attr = field.lower().replace(' ', '_').replace('ё', 'е')
            setattr(self, attr, row.get(field, 0))

        self.name = self.full_name
        self.age = self.age
        self.club = team
        self.workingFoot = getattr(self, 'working foot', 0)
        self.height = 170

        self.skillSave = getattr(self, 'DefenseAverage', 0)
        self.skillSelection = getattr(self, 'DribblingAverage', 0)
        self.skillPass = getattr(self, 'DribblingAverage', 0)
        self.skillShot = getattr(self, 'ShootingAverage', 0)

        # Статистика сезона
        self.active = False
        self.goals = self.fifa_goals
        self.correctPass = 0
        self.physic = self.fifa_physic
        self.shots = 0
        self.allPass = 0
        self.loseBall = 0
        self.selections = 0
        self.saves = 0

        # Присваиваем FIFA атрибуты
        for field in Footballer.FIFA_FIELDS:
            attr = field.lower()
            setattr(self, attr, row.get(attr, 0))

        # Вычисляем мастерство по позициям
        self.skills = []
        for pos, attrs in Footballer.POSITION_FORMULAS.items():
            vals = [getattr(self, f.lower(), 0) for f in attrs]
            self.skills.append(int(sum(vals) / len(vals)) if vals else 0)

    # Восстановление статусов
    def zeroingOfActive(self):
        self.active = False

    def zeroingPhysic(self):
        if self.physic + 250 / self.age >= 100:
            self.physic = 100
        else:
            self.physic += 250 / self.age

    def oneMove(self):
        self.physic = self.physic / (self.age * 7)

    # Утилита подсчёта навыков
    def countSkillPosition(self, for4, for3, for2, for1, count, difference):
        temp = (
            4 * sum(int(self.skillsAll[i]) for i in for4) +
            3 * sum(int(self.skillsAll[i]) for i in for3) +
            2 * sum(int(self.skillsAll[i]) for i in for2) +
                sum(int(self.skillsAll[i]) for i in for1)
        ) / count
        return temp + difference
