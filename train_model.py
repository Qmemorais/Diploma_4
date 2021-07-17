##load modules and else
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np
import play_with_statistics as pws

##data for train
def GetTrainingData(seasons,division,data_from_csv):
    totalNumGames = 0
    for season in seasons:
        annual = data_from_csv.loc[(data_from_csv.season == season) & (data_from_csv.division) == division]
        totalNumGames += len(annual.index)
    numFeatures = len(pws.GetSeasonTeamStat('Real Madrid', '2016-17',data_from_csv)) 
    xTrain = np.zeros(( totalNumGames, numFeatures))
    yTrain = np.zeros(( totalNumGames ))
    indexCounter = 0
    for season in seasons:
        team_vectors = pws.GetSeasonAllTeamStat(season,data_from_csv)
        annual = data_from_csv.loc[(data_from_csv.season == season) & (data_from_csv.division) == division]
        numGamesInYear = len(annual.index)
        xTrainAnnual = np.zeros(( numGamesInYear, numFeatures))
        yTrainAnnual = np.zeros(( numGamesInYear ))
        counter = 0
        for index, row in annual.iterrows():
            team = row['localTeam']
            t_vector = team_vectors[team]
            rivals = row['visitorTeam']
            r_vector = team_vectors[rivals]
           
            diff = [a - b for a, b in zip(t_vector, r_vector)]
            
            if len(diff) != 0:
                xTrainAnnual[counter] = diff
            if team == row['winner']:
                yTrainAnnual[counter] = 1
            else: 
                yTrainAnnual[counter] = 0
            counter += 1   
        xTrain[indexCounter:numGamesInYear+indexCounter] = xTrainAnnual
        yTrain[indexCounter:numGamesInYear+indexCounter] = yTrainAnnual
        indexCounter += numGamesInYear
    return xTrain, yTrain


def load_or_train(data_from_csv):
    seasons = data_from_csv.season.unique().tolist()
    try:
        ##if we already have the model of prediction
        model=joblib.load("model_of_prediction.pkl")
        print("We already have a model")
    except:
        ##else we train model
        xTrain, yTrain = GetTrainingData(seasons,1,data_from_csv)
        model = LinearRegression()
        model.fit(xTrain, yTrain)
        joblib.dump( model, "model_of_prediction.pkl")
        print("We save the model to use in future")
    return model
##output prediction for game
def createGamePrediction(team1_vector, team2_vector,data_from_csv):
    model = load_or_train(data_from_csv)
    diff = [[a - b for a, b in zip(team1_vector, team2_vector)]]
    predictions = model.predict(diff)
    return predictions
