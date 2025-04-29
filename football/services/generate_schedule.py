
def generate_schedule(team_ids):
    """
    Классический «round robin» генератор расписания:
    возвращает список списков пар (id_home, id_guest) для каждого тура.
    Если число команд нечётное — добавляет «бай» (None).
    """
    ids = list(team_ids)
    if len(ids) % 2:
        ids.append(None)
    n = len(ids)
    schedule = []
    for round_idx in range(n - 1):
        pairs = []
        for i in range(n // 2):
            h, g = ids[i], ids[n - 1 - i]
            if h is not None and g is not None:
                pairs.append((h, g))
        # вращаем всех, кроме первого
        ids = [ids[0]] + [ids[-1]] + ids[1:-1]
        schedule.append(pairs)

    for round_idx in range(n - 1):
        pairs = []
        for i in range(n // 2):
            h, g = ids[i], ids[n - 1 - i]
            if h is not None and g is not None:
                pairs.append((g, h))
        # вращаем всех, кроме первого
        ids = [ids[0]] + [ids[-1]] + ids[1:-1]
        schedule.append(pairs)

    return schedule
