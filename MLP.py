import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

#Enter the path to dataset
path1 = str("PathToCSV1.csv")
path2 = str("PathToCSV2.csv")

#corresponding DataFrames
df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)

#Features for first network
X1 = df1.drop(columns= ['ExamReg']) #Change name according to dataset
y1 = df1['ExamReg']

#Generating randomly sampled and split train/test sets
Xtr1, Xts1, ytr1, yts1 = train_test_split(X1,y1)

#Features for the seconds network
X2 = df2.drop(columns= ['Scholarship Approved']) #Change name according to dataset
y2 = df2['Scholarship Approved']

#Training
#First network
num_hidden_neuron1 = 4 #Change according to preferences
Network1 = MLPClassifier((num_hidden_neuron1))
Network1.fit(Xtr1,ytr1)
new_feature = Network1.predict(Xtr1)

#Appending new feature to the input of second network
X2 = pd.concat([X2,pd.DataFrame(new_feature)],axis= 1)

#Generating randomly sampled and split train/test sets
Xtr2, Xts2, ytr2, yts2 = train_test_split(X2,y2)

#Second Network 
num_hidden_neuron2 = 4 #Change according to preferences
Network2 = MLPClassifier((num_hidden_neuron2))
Network2.fit(Xtr2,ytr2)

#Testing
new_feature_test = Network1.predict(Xts1)
Xts2 = pd.concat([Xts2,pd.DataFrame(new_feature_test)],axis= 1)
print(Network2.score(Xts2,yts2)) #Prints Accuracy/100



 

