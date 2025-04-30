from dataclasses import dataclass


@dataclass
class Shot:
    minute: int
    homeGoal: int
    guestGoal: int
    homeShots: int
    whoScoreGuest: int
    whoScoreHome: int
    homeShotsTo: int
    homeXGs: int


@dataclass
class Pass:
    minute: int
    homeGoal: int
    guestGoal: int
    homeShots: int
    whoScoreGuest: int
    whoScoreHome: int
    homeShotsTo: int
    player_id: int
    homeXGs: int
    guestXGs: int