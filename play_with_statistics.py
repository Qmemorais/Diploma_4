import collections

totalNumGames = 0
##statistics for team by season "input"
def GetSeasonTeamStat(team, season,data_from_csv):
    goalScored = 0 #Голов забито
    goalAllowed = 0 #Голов пропущено
    gameWin = 0 #Выиграно
    gameDraw = 0 #Ничья
    gameLost = 0 #Проиграно
    totalScore = 0 #Количество набранных очков
    matches = 0 #Количество сыгранных матчей
    average_goals_scored = 0 #Среднее количество забитых мячей за сезон( кол-во забитых / кол-во матчей
    average_goals_allowed = 0 #Среднее количество пропущеных мячей за сезон( кол-во пропущеных / кол-во матчей
    scored_to_allowed = 0 #соотношение забитых мячей к пропущенным ( колв-о забитых минус кол-во пропущеных
    win_to_match = 0 #в процентах величина побед от всех матчей

    for i in range(len(data_from_csv)):
        if ((data_from_csv['season'][i] == season) and ((data_from_csv['localTeam'][i] == team) or (data_from_csv['visitorTeam'][i] == team))):
            matches += 1
            if data_from_csv['localTeam'][i] == team:
                goalScored += data_from_csv['localGoals'][i]
                goalAllowed += data_from_csv['visitorGoals'][i]
                if (data_from_csv['localGoals'][i] > data_from_csv['visitorGoals'][i]):
                    totalScore += 3
                    gameWin += 1
                elif (data_from_csv['localGoals'][i] < data_from_csv['visitorGoals'][i]):
                    gameLost +=1
                else:
                    totalScore += 1
                    gameDraw += 1
            if data_from_csv['visitorTeam'][i] == team:
                goalScored += data_from_csv['visitorGoals'][i]
                goalAllowed += data_from_csv['localGoals'][i]
                if (data_from_csv['visitorGoals'][i] > data_from_csv['localGoals'][i]):
                    totalScore += 3
                    gameWin += 1
                elif (data_from_csv['visitorGoals'][i] < data_from_csv['localGoals'][i]):
                    gameLost +=1
                else:
                    totalScore += 1
                    gameDraw += 1

    average_goals_scored = goalScored / matches
    average_goals_allowed = goalAllowed / matches
    scored_to_allowed = goalScored - goalAllowed
    win_to_match = gameWin / matches * 100

    return [gameWin, gameDraw, gameLost, 
            goalScored, goalAllowed, totalScore, matches,
           average_goals_scored, average_goals_allowed, scored_to_allowed, win_to_match]
##get statistics for all team by season "input"
def GetSeasonAllTeamStat(season,data_from_csv):
    annual = collections.defaultdict(list)
    data_from_season = data_from_csv.loc[data_from_csv.season == season]
    team_name = data_from_season.localTeam.unique().tolist()
    for team in team_name:
        team_vector = GetSeasonTeamStat(team, season,data_from_csv)
        annual[team] = team_vector
    return annual
