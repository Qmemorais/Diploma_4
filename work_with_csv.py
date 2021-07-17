import pandas as pd
import numpy as np

def read_csv():
    data_from_csv = pd.read_csv('FMEL_Dataset.csv')
    data_from_csv_plus_winner = []
    for i in range(len(data_from_csv)):
        if data_from_csv.localGoals[i] > data_from_csv.visitorGoals[i]:
            data_from_csv_plus_winner.append(data_from_csv.localTeam[i])
        else:
            data_from_csv_plus_winner.append(data_from_csv.visitorTeam[i])
    data_from_csv_plus_winner = pd.DataFrame(data_from_csv_plus_winner,columns = ['winner'])
    data_from_csv = data_from_csv.assign(winner = data_from_csv_plus_winner.values)
    return data_from_csv
