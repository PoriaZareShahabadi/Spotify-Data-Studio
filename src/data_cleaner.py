import pandas as pd
from abc import ABC, abstractmethod
from sklearn.impute import KNNImputer as knnimputer
from scipy.stats import zscore

class BaseImputer(ABC):
    @abstractmethod
    def impute(self):
        pass
    
class MeanImputer(BaseImputer):
    def impute(self, df, properties):
        for column in properties:
            df.fillna({column: df[column].mean()}, inplace = True)

class MedianImputer(BaseImputer):
    def impute(self,df,properties):
        for column in properties:
            df.fillna({column: df[column].median(numeric_only=True)}, inplace = True)

class KNNImputer(BaseImputer):
    def impute(self,df,properties):
        imputer = knnimputer(n_neighbors=10)
        df[properties] = pd.DataFrame(imputer.fit_transform(df[properties]))


class BaseOutlierHandler(ABC):
    @abstractmethod
    def handle(self):
        pass 

class IQROutlierHandler(BaseOutlierHandler):
    
    def handle(self,df,properties):
        for column in properties:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            
            l = Q1 - 1.5 * IQR
            u = Q3 + 1.5 * IQR
            
            df = df[(df[column] >= l) & (df[column] <= u)]

        return df

class ZScoreOutlierHandler(BaseOutlierHandler):
    
    def handle(self,df,properties):
        for column in properties:
            z_scores = zscore(df[column])
            df = df[abs(z_scores) <= 3]
        return df

    """
    def handle(self,df,properties):
        for c in properties:
            mean = df[c].mean()
            std = df[c].std()

            z-scores = (df[c] - mean) / std

            df = df[abs(z-scores) <= 3]
    return df
    """
