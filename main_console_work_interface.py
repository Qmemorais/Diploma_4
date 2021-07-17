##load modules and else

import sys
import work_with_csv as wws
import play_with_statistics as pws
import train_model as tm

##load "Welcome"
def first_load():
    print("Hello!\nWe just need a few seconds to get start\nPlease wait\n")

def main_interface(data_from_csv):
    ##to output in console
    returnNames = ["\nWon", "Draw", "Lose",
               "\nGoals scored", "Goals conceded", "\nPoints scored",
               "\nNumber of games played","\nNumber of goals scored per match",
               "\nNumber of goals conceded per match","\nRatio of goals per season",
               "\nRatio of wins to total matches in %"]
    ##work with app
    while True:
        try:
            choice = int(input("\n1 - View team statistics for the season\n2 - Predict the result of a match between teams\n0 - Exit\nPlease enter your choice: "))
        except:
            print("You`re input symbols. Not a numeric. Please try again")
            continue
        if choice == 1:
            season_to_choose = all_season_output(data_from_csv.season.unique().tolist())
            season_to_statictics = input("\nEnter season. An example for input is shown below.\n2015-17\n2014-15\n: ")
            if season_to_statictics in data_from_csv.season.unique().tolist():
                print("")
            else:
                print("Wrong season. Please try again\n")
                continue
            team_to_choose = all_teams_name(data_from_csv,season_to_statictics)
            team_name = input("\nEnter the team name. An example for input is shown below.\nBarcelona\nReal Madrid\n: ")
            if team_name in team_to_choose:
                for i, n in zip(returnNames, pws.GetSeasonTeamStat(team_name,season_to_statictics,data_from_csv)):
                    print(i, n)
            else:                
                print("Something went wrong. Please check the entered values\n")
                continue
        elif choice == 2:
            team_to_choose = all_teams_name(data_from_csv,"2017-18")
            try:
                team_name_1,team_name_2 = input("\nEnter the team name, separated by commas. An example for input is shown below.\nReal Madrid,Atletico de Bilbao\n: ").split(',')
            except:
                print("You`re input only one team")
                continue
            if team_name_1 in team_to_choose:
                team_vector_first = pws.GetSeasonTeamStat(team_name_1,'2017-18',data_from_csv)
            else: 
                print("Wrong team name. Please try again\n")
                continue
            if team_name_2 in team_to_choose:
                team_vector_second = pws.GetSeasonTeamStat(team_name_2,'2017-18',data_from_csv)
            else: 
                print("Wrong team name. Please try again\n")    
                continue
            print ('The likelihood that {0} will win : {1}'.format(team_name_1,tm.createGamePrediction(team_vector_first, team_vector_second,data_from_csv)))
            print ('The likelihood that {0} will win : {1}'.format(team_name_2,tm.createGamePrediction(team_vector_second, team_vector_first,data_from_csv)))
        elif choice == 0:
            sys.exit()
        else :
            print("You entered an invalid value. Please try again\n")

def print_pretty_table(data, cell_sep=' | ', header_separator=True):
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [data[row][col] for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    for i, row in enumerate(range(rows)):
        result = []
        for col in range(cols):
            item = data[row][col].rjust(col_width[col])
            result.append(item)

        print(cell_sep.join(result))

def  all_teams_name(data_from_csv,season):
    print("Soccer team names you can use:\n")
    table_data=[[]]
    count=0
    team_names = data_from_csv.loc[(data_from_csv.division == 1) & (data_from_csv.season == season)].localTeam.unique().tolist()
    for name_team_index in team_names:
        if team_names.index(name_team_index) % 4 == 0 and team_names.index(name_team_index) != 0:
            count+=1
            table_data.append(list())
            table_data[count].append(name_team_index)
        else: 
            table_data[count].append(name_team_index)
    while len(table_data[count]) != 4:
        table_data[count].append("")
    print_pretty_table(table_data)
    return team_names

def  all_season_output(season_to_choose):
    print("Seasons you can use:\n")
    table_data=[[]]
    count=0
    for season_to_choose_index in season_to_choose:
        if season_to_choose.index(season_to_choose_index) % 4 == 0 and season_to_choose.index(season_to_choose_index) != 0:
            count+=1
            table_data.append(list())
            table_data[count].append(season_to_choose_index)
        else: 
            table_data[count].append(season_to_choose_index)
    while len(table_data[count]) != 4:
        table_data[count].append("")
    print_pretty_table(table_data)
    return season_to_choose