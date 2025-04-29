from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.http import JsonResponse
from .models import modelTeam
from .services.classTeam import Team
from .services.classLiga import Liga
from .services.classGame import Game
from .services.generate_schedule import generate_schedule
import json



@require_POST
def reset_league(request):
    # Полностью очищаем сессию
    request.session.flush()
    # Если у вас есть модель, куда вы записываете промежуточные результаты, и
    # вы хотите её тоже очистить, раскомментируйте примерно такой код:
    #
    # from .models import SomeResultModel
    # SomeResultModel.objects.all().delete()

    # После сброса перенаправляем обратно на таблицу
    return redirect('league_table')


def _build_table_data(results_dict):
    """
    Собирает headers и rows по данным results_dict,
    ключ – строка "home_id,guest_id", значение – (homeGoal, guestGoal).
    """

    # 1) Получаем все команды из БД
    team_qs = list(modelTeam.objects.all())
    # 2) Создаём инстансы вашего сервиса Team (чтобы накопить wins, points и т.п.)
    teams = [Team(t.id, t.title, t.liga) for t in team_qs]

    # 3) Инициализируем статистику
    stats = {tm.id: {'played': 0,
                     'wins': 0,
                     'draws': 0,
                     'losses': 0,
                     'gf': 0,
                     'ga': 0,
                     'points': 0} for tm in teams}
    #print(results_dict)
    # 4) Пробегаем по сыгранным матчам
    for tour in range(len(results_dict)):
        for key, (hg, gg) in results_dict[str(tour + 1)].items():
            hid, gid = map(int, key.split(','))
            st_h, st_g = stats[hid], stats[gid]

            st_h['played'] += 1
            st_g['played'] += 1

            st_h['gf'] += hg
            st_h['ga'] += gg

            st_g['gf'] += gg
            st_g['ga'] += hg

            if hg > gg:
                st_h['wins'] += 1
                st_h['points'] += 3
                st_g['losses'] += 1
            elif hg < gg:
                st_g['wins'] += 1
                st_g['points'] += 3
                st_h['losses'] += 1
            else:
                st_h['draws'] += 1
                st_g['draws'] += 1
                st_h['points'] += 1
                st_g['points'] += 1

    # 5) Считаем разницу мячей
    for v in stats.values():
        v['gd'] = v['gf'] - v['ga']

    # 6) Сортируем команды
    teams.sort(key=lambda t: (
        stats[t.id]['points'],
        stats[t.id]['gd'],
        stats[t.id]['gf']
    ), reverse=True)

    # 7) Формируем headers
    headers = ['№', 'Team'] + [str(i + 1) for i in range(len(teams))] + ['P', 'W', 'D', 'L', 'G', 'Pts']

    # 8) Формируем rows для шаблона
    rows = []

    for pos, t in enumerate(teams, start=1):
        row = {
            'pos': pos,
            'team': next(tm for tm in team_qs if tm.id == t.id),
            **stats[t.id],
            'cells': []
        }
        for opp in teams:
            if opp.id == t.id:
                row['cells'].append({'text': '—', 'css': 'self'})
            else:
                k = f'{t.id},{opp.id}'
                text = ''
                css = ''
                for tour, val in results_dict.items():
                    if k in val.keys():
                        hg, gg = results_dict[tour][k]
                        text = f"{hg}:{gg}"
                        if hg == gg:
                            css = 'draw'
                        elif hg > gg:
                            css = 'win'
                        else:
                            css = 'loss'
                row['cells'].append({'text': text, 'css': css, 'match_id': k})
        rows.append(row)

    return headers, rows


def main_view(request):
    """
    Главная страница (аналог Ui_MainWindow)
    """
    return render(request, 'football/main.html')


def new_game_view(request):
    teams = modelTeam.objects.all()
    arrayOfTeams = []

    for x in teams:
        arrayOfTeams.append(Team(x.id, x.title, x.liga))

    globalNumberSeason = 0
    ligas = [Liga(arrayOfTeams[:len(arrayOfTeams)], globalNumberSeason)]

    return render(request, 'football/game.html')


def players_data_view(request):
    """
    Страница работы с данными игроков (аналог BaseDataPlayers)
    """
    return render(request, 'football/players_data.html')


def league_table(request):
    """
    При первом заходе инициализируем очередь матчей и чистим результаты.
    Затем рисуем таблицу.
    """

    if 'match_queue' not in request.session:
        # построим очередь всех пар (home,guest)
        teams = list(modelTeam.objects.all())
        request.session['match_queue'] = generate_schedule([x.id for x in teams])
        request.session['results'] = {}
        request.session.modified = True
    headers, rows = _build_table_data(request.session['results'])

    return render(request, 'football/league.html', {
        'headers': headers,
        'rows': rows,
    })


def match_detail_json(request, match_id):
    matches = request.session.get('matches', {})
    data = {}

    for x in matches:
        if x['id'] == match_id:
            data = x

    if not data:
        return JsonResponse({'error': 'Not found'}, status=404)
    return JsonResponse(data)


@require_POST
def play_round(request):
    """
    Берём из сессии первый матч, играем его, сохраняем результат,
    возвращаем только partial шаблон с обновлённой таблицей.
    """
    queue = request.session.get('match_queue', [])
    results = request.session.get('results', {})
    if queue:
        tour = queue.pop(0)
        number_tour = len(results) + 1
        results[str(number_tour)] = {}
        games = []
        for match in tour:
            hid, gid = match[0], match[1]
            home_m = Team(hid, modelTeam.objects.get(id=hid).title, None)
            guest_m = Team(gid, modelTeam.objects.get(id=gid).title, None)
            game = Game(home_m, guest_m)
            game.choiceSelection()
            game.match()
            games.append(game)
            results[str(number_tour)][f'{hid},{gid}'] = (game.homeGoal, game.guestGoal)

        # обратно в сессию
        request.session['match_queue'] = queue
        request.session['results'] = results

        if request.session.get('matches'):
            request.session['matches'] += [x.to_json() for x in games]
        else:
            request.session['matches'] = [x.to_json() for x in games]
        request.session.modified = True

    headers, rows = _build_table_data(results)
    return render(request, 'football/league_table_body.html', {
        'headers': headers,
        'rows': rows
    })