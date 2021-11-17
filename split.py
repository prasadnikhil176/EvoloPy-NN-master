import pandas as pd
from sklearn.model_selection import train_test_split


data= pd.read_csv("C:\\Users\\COI-AI-21\\Desktop\\EvoloPy-NN-master\\datasets\\heart.csv")

#test =pd.read_csv("C:\\Users\\COI-AI-21\\Desktop\\EvoloPy-NN-master\\datasets\\heartTest.csv")


heart1Train,heart1Test = train_test_split(data,test_size=0.34,random_state=0)
heart1Train.to_csv("C:\\Users\\COI-AI-21\\Desktop\\EvoloPy-NN-master\\datasets\\heartTrain.csv",header= None, index= False)
heart1Test.to_csv("C:\\Users\\COI-AI-21\\Desktop\\EvoloPy-NN-master\\datasets\\heartTest.csv", header = None, index= False)