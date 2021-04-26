import pandas as pd

class Analyse:

    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        self.df.drop(columns= self.df.columns[-8:], inplace=True)
        self.df.drop(columns= ['id'], inplace=True)
    
    def getPositionData(self):
        return self.df.groupby('banner_pos').count()['hour']

    def getDataset(self):
        return self.df