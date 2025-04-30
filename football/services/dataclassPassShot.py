from dataclasses import dataclass


@dataclass
class Shot:
    history: str
    shooter: int
    goalkeeper_id: int
    xg: int
    shot: int
    shot_on_target: int
    is_goal: int
    shot_on_target: int


@dataclass
class Pass:
    history: str
    is_goal: int
    xg: int