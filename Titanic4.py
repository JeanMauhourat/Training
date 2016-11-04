# VARIABLE DESCRIPTIONS:
#
# survival        Survival
#                 (0 = No; 1 = Yes)
# pclass          Passenger Class
#                 (1 = 1st; 2 = 2nd; 3 = 3rd)
# name            Name
# sex             Sex
# age             Age
# sibsp           Number of Siblings/Spouses Aboard
# parch           Number of Parents/Children Aboard
# ticket          Ticket Number
# fare            Passenger Fare
# cabin           Cabin
# embarked        Port of Embarkation
#                 (C = Cherbourg; Q = Queenstown; S = Southampton)
#
# SPECIAL NOTES:
# Pclass is a proxy for socio-economic status (SES)
#  1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower
# 
# Age is in Years; Fractional if Age less than One (1)
#  If the Age is Estimated, it is in the form xx.5
# 
# With respect to the family relation variables (i.e. sibsp and parch)
# some relations were ignored.  The following are the definitions used
# for sibsp and parch.
# 
# Sibling:  Brother, Sister, Stepbrother, or Stepsister of Passenger Aboard Titanic
# Spouse:   Husband or Wife of Passenger Aboard Titanic (Mistresses and Fiances Ignored)
# Parent:   Mother or Father of Passenger Aboard Titanic
# Child:    Son, Daughter, Stepson, or Stepdaughter of Passenger Aboard Titanic
# 
# Other family relatives excluded from this study include cousins,
# nephews/nieces, aunts/uncles, and in-laws.  Some children travelled
# only with a nanny, therefore parch=0 for them.  As well, some
# travelled with very close friends or neighbors in a village, however,
# the definitions do not support such relations.
# 
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import pylab as P
import seaborn as sb
sb.set_style('whitegrid')
Path='P:/Documents/Formation Data Scientist AXA/Prework/'
#
#
#
# STEP 1 : cleaning, formating & featuring data
#
# Training sample :
TrainDF = pd.read_csv(Path+'train.csv', header=0)
TrainDF.info()
TrainDF.describe()
sb.countplot(x='Sex', data=TrainDF)
sb.countplot(x='Embarked', data=TrainDF)
TrainDF['SexNum'] = TrainDF['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
TrainDF['EmbarkedFill'] = TrainDF['Embarked'].fillna("S")
TrainDF['EmbarkedNum'] = TrainDF['EmbarkedFill'].map( {'Q': 0, 'C': 1, 'S': 2} ).astype(int)
TrainDF['EmbarkedIsQ'] = TrainDF['EmbarkedFill'].map( lambda x: (x == "Q")*1 )
TrainDF['EmbarkedIsC'] = TrainDF['EmbarkedFill'].map( lambda x: (x == "C")*1 )
TrainMeanAge=TrainDF['Age'].mean()
print TrainMeanAge
TrainDF["AgeFill"] = TrainDF['Age'].fillna(TrainMeanAge)
TrainDF['AgeIsNaN'] = pd.isnull(TrainDF.Age).astype(int)
sb.countplot(x='EmbarkedFill', data=TrainDF)
sb.countplot(x='AgeIsNaN', data=TrainDF)
TrainDF['Age'].hist()
P.show()
TrainDF['AgeFill'].hist()
P.show()
TrainDF['FamilySize'] = TrainDF['SibSp'] + TrainDF['Parch']
TrainDF['FamilyB'] = TrainDF['FamilySize'].map( lambda x: (x > 0)*1 )
TrainDF[ TrainDF['Cabin'].isnull()==0 ][['Cabin']]
TrainDF['CabinFill'] = TrainDF['Cabin'].fillna("?")
TrainDF['CabinFirstLetter'] = TrainDF['CabinFill'].map( lambda x: x[0].upper() )
sb.countplot(x='CabinFirstLetter', data=TrainDF)
TrainDF['CabinFirstLetterNum'] = TrainDF['CabinFirstLetter'].map( {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'T': 7,'?': -1} ).astype(int)
TrainDF['CabinIsA'] = TrainDF['CabinFirstLetter'].map( lambda x: (x == "A")*1 )
TrainDF['CabinIsB'] = TrainDF['CabinFirstLetter'].map( lambda x: (x == "B")*1 )
TrainDF['CabinIsC'] = TrainDF['CabinFirstLetter'].map( lambda x: (x == "C")*1 )
TrainDF['CabinIsD'] = TrainDF['CabinFirstLetter'].map( lambda x: (x == "D")*1 )
TrainDF['CabinIsE'] = TrainDF['CabinFirstLetter'].map( lambda x: (x == "E")*1 )
TrainDF['CabinIsF'] = TrainDF['CabinFirstLetter'].map( lambda x: (x == "F")*1 )
TrainDF['CabinIsG'] = TrainDF['CabinFirstLetter'].map( lambda x: (x == "G")*1 )
TrainDF['CabinIsT'] = TrainDF['CabinFirstLetter'].map( lambda x: (x == "T")*1 )
#
# Testing sample : no Y, just X to submit prediction to Kaggle
TestDF = pd.read_csv(Path+'test.csv', header=0)
TestDF.info()
TestDF.describe()
sb.countplot(x='Sex', data=TestDF)
sb.countplot(x='Embarked', data=TestDF)
TestDF['SexNum'] = TestDF['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
TestDF['EmbarkedFill'] = TestDF['Embarked'].fillna("S")
TestDF['EmbarkedNum'] = TestDF['EmbarkedFill'].map( {'Q': 0, 'C': 1, 'S': 2} ).astype(int)
TestDF['EmbarkedIsQ'] = TestDF['EmbarkedFill'].map( lambda x: (x == "Q")*1 )
TestDF['EmbarkedIsC'] = TestDF['EmbarkedFill'].map( lambda x: (x == "C")*1 )
TestMeanAge=TestDF['Age'].mean()
print TestMeanAge
TestDF["AgeFill"] = TestDF['Age'].fillna(TestMeanAge)
TestDF['AgeIsNaN'] = pd.isnull(TestDF.Age).astype(int)
sb.countplot(x='EmbarkedFill', data=TestDF)
sb.countplot(x='AgeIsNaN', data=TestDF)
TestDF['Age'].hist()
P.show()
TestDF['AgeFill'].hist()
P.show()
TestDF['FamilySize'] = TestDF['SibSp'] + TestDF['Parch']
TestDF['FamilyB'] = TestDF['FamilySize'].map( lambda x: (x > 0)*1 )
TestDF[ TestDF['Cabin'].isnull()==0 ][['Cabin']]
TestDF['CabinFill'] = TestDF['Cabin'].fillna("?")
TestDF['CabinFirstLetter'] = TestDF['CabinFill'].map( lambda x: x[0].upper() )
sb.countplot(x='CabinFirstLetter', data=TestDF)
TestDF['CabinFirstLetterNum'] = TestDF['CabinFirstLetter'].map( {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'T': 7,'?': -1} ).astype(int)
TestDF['CabinIsA'] = TestDF['CabinFirstLetter'].map( lambda x: (x == "A")*1 )
TestDF['CabinIsB'] = TestDF['CabinFirstLetter'].map( lambda x: (x == "B")*1 )
TestDF['CabinIsC'] = TestDF['CabinFirstLetter'].map( lambda x: (x == "C")*1 )
TestDF['CabinIsD'] = TestDF['CabinFirstLetter'].map( lambda x: (x == "D")*1 )
TestDF['CabinIsE'] = TestDF['CabinFirstLetter'].map( lambda x: (x == "E")*1 )
TestDF['CabinIsF'] = TestDF['CabinFirstLetter'].map( lambda x: (x == "F")*1 )
TestDF['CabinIsG'] = TestDF['CabinFirstLetter'].map( lambda x: (x == "G")*1 )
TestDF['CabinIsT'] = TestDF['CabinFirstLetter'].map( lambda x: (x == "T")*1 )
TestDF[ TestDF['Fare'].isnull()][['Pclass','Embarked','Sex','Age','SibSp','Parch','Ticket']]
FareMissing=TestDF[ (TestDF['Fare'].isnull()==0) & (TestDF['Pclass']==3) & (TestDF['Sex']=="male") & (TestDF['Embarked']=="S") & (TestDF['FamilyB']==0) ]['Fare'].median()
TestDF['Fare'] = TestDF['Fare'].fillna(FareMissing)
#
#
#
# STEP 2 : provide basic descriptive stat
#
# This step provide survival rate for various population : by sex, class,
# age interval, sex x class, etc.
# This step is not yet implemented here whith Python,
# but it has been made in Excel with DCT.
#
# To be completed...
#
#
#
# STEP 3 : Prepare data for fitting & submitting prediction to Kaggle
TrainYdf=TrainDF[['Survived']]
#
# X1 is a good X for learning machine fitting methods like GBM
# but not for other methods like logistic regression for which we prefer X2.
X1=['Pclass','SexNum','AgeFill','AgeIsNaN','SibSp','Parch','FamilySize','FamilyB','Fare','CabinFirstLetterNum','EmbarkedNum']
X2=['Pclass','SexNum','AgeFill','AgeIsNaN','SibSp','Parch','FamilyB','Fare','CabinIsA','CabinIsB','CabinIsC','CabinIsD','CabinIsE','CabinIsF','CabinIsG','CabinIsT','EmbarkedIsC','EmbarkedIsQ']
# X3 = ...
#
# Chose X below (X=X1 or X2 or etc.) and run pgm until the end of step 3 
# before fitting with one or several fitting methods at Step 4 (GBM, SVM, etc.)
X=X2
TrainXdf=TrainDF[X]
TestXdf=TestDF[X]
#
UnifRandomSeries=Series(np.random.randn(len(TrainYdf)))
#
TrainYdf['UnifRandom']=UnifRandomSeries
TrainXdf['UnifRandom']=UnifRandomSeries
#
# Training sample is split into (real) training vs testing sample.
# Chose below the share of the (real) training sample.
TrainSampleSizePercent=0.66
#
TrainYdfTrain=TrainYdf[TrainYdf['UnifRandom']<TrainSampleSizePercent]
TrainYdfTest=TrainYdf[TrainYdf['UnifRandom']>=TrainSampleSizePercent]
TrainXdfTrain=TrainXdf[TrainYdf['UnifRandom']<TrainSampleSizePercent]
TrainXdfTest=TrainXdf[TrainYdf['UnifRandom']>=TrainSampleSizePercent]
#
TrainYdf=TrainYdf.drop('UnifRandom',axis=1)
TrainYdfTrain=TrainYdfTrain.drop('UnifRandom',axis=1)
TrainYdfTest=TrainYdfTest.drop('UnifRandom',axis=1)
TrainXdf=TrainXdf.drop('UnifRandom',axis=1)
TrainXdfTrain=TrainXdfTrain.drop('UnifRandom',axis=1)
TrainXdfTest=TrainXdfTest.drop('UnifRandom',axis=1)
#
TrainComparTest=TrainYdfTest[['Survived']]
#
#
#
# STEP 4 : fit with one of several fitting methods below (logistic regression, random forest, GBM, etc.)
#
# Fit with Logistic GLM, not learning machine.
# X2 is a good X for this fitting method but not X1.
from sklearn.linear_model import LogisticRegression
LRSpe = LogisticRegression()
LRSpe.fit(TrainXdfTrain,TrainYdfTrain)
ScoreTrainLR=LRSpe.score(TrainXdfTrain,TrainYdfTrain)
print ScoreTrainLR
TrainYPredTest=LRSpe.predict(TrainXdfTest)
TrainComparTest['SurvivedPredLR']=TrainYPredTest
ScoreTestLR=len(TrainComparTest[TrainComparTest['SurvivedPredLR']==TrainComparTest['Survived']])
ScoreTestLR=float(ScoreTestLR)/len(TrainComparTest)
print ScoreTestLR
#
#
#
# Fit with Random Forest 
from sklearn.ensemble import RandomForestClassifier 
ForestSpe = RandomForestClassifier(n_estimators = 100)
ForestSpe.fit(TrainXdfTrain,TrainYdfTrain)
ScoreTrainRFC=ForestSpe.score(TrainXdfTrain,TrainYdfTrain)
print ScoreTrainRFC
TrainYPredTest=ForestSpe.predict(TrainXdfTest)
TrainComparTest['SurvivedPredRFC']=TrainYPredTest
ScoreTestRFC=len(TrainComparTest[TrainComparTest['SurvivedPredRFC']==TrainComparTest['Survived']])
ScoreTestRFC=float(ScoreTestRFC)/len(TrainComparTest)
print ScoreTestRFC
#
#
#
# Fit with GBM
from sklearn.ensemble import GradientBoostingClassifier
GBCSpe = GradientBoostingClassifier(n_estimators=100000,learning_rate=0.001)
GBCSpe.fit(TrainXdfTrain,TrainYdfTrain)
ScoreTrainGBC=GBCSpe.score(TrainXdfTrain,TrainYdfTrain)
print ScoreTrainGBC
TrainYPredTest=GBCSpe.predict(TrainXdfTest)
TrainComparTest['SurvivedPredGBC']=TrainYPredTest
ScoreTestGBC=len(TrainComparTest[TrainComparTest['SurvivedPredGBC']==TrainComparTest['Survived']])
ScoreTestGBC=float(ScoreTestGBC)/len(TrainComparTest)
print ScoreTestGBC
#
#
#
# Fit with SVM
from sklearn.svm import SVC
SVCSpe = SVC()
SVCSpe.fit(TrainXdfTrain,TrainYdfTrain)
ScoreTrainSVC=SVCSpe.score(TrainXdfTrain,TrainYdfTrain)
print ScoreTrainSVC
TrainYPredTest=SVCSpe.predict(TrainXdfTest)
TrainComparTest['SurvivedPredSVC']=TrainYPredTest
ScoreTestSVC=len(TrainComparTest[TrainComparTest['SurvivedPredSVC']==TrainComparTest['Survived']])
ScoreTestSVC=float(ScoreTestSVC)/len(TrainComparTest)
print ScoreTestSVC
#
#
#
# Fit with K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
KNCSpe=KNeighborsClassifier(n_neighbors = 3)
KNCSpe.fit(TrainXdfTrain,TrainYdfTrain)
ScoreTrainKNC=KNCSpe.score(TrainXdfTrain,TrainYdfTrain)
print ScoreTrainKNC
TrainYPredTest=KNCSpe.predict(TrainXdfTest)
TrainComparTest['SurvivedPredKNC']=TrainYPredTest
ScoreTestKNC=len(TrainComparTest[TrainComparTest['SurvivedPredKNC']==TrainComparTest['Survived']])
ScoreTestKNC=float(ScoreTestKNC)/len(TrainComparTest)
print ScoreTestKNC
#
# 
#
# Other methods of fitting are interesting but lack of time...
# Notably Neural Networks after normalization of data.
#
#
#
# For submission 1 to Kaggle, we select GBM with X=X1 (see above) because the testing score is the best.
# But we re-calibrate it with the entire training sample.
#
GBCSpe = GradientBoostingClassifier(n_estimators=100000,learning_rate=0.001)
GBCSpe.fit(TrainXdf,TrainYdf)
ScoreTrainGBC=GBCSpe.score(TrainXdf,TrainYdf)
print ScoreTrainGBC
#
submission = pd.DataFrame({
        "PassengerId": TestDF["PassengerId"],
        "Survived": GBCSpe.predict(TestXdf)
    })
submission.to_csv(Path+'TitanicSubmit1.csv', index=False)
#
#
# For submission 2 to Kaggle, we select Logit Regression with X=X2 (see above) because the 
# 1st submission provide bullshit (score=0.72). This 2nd one improve weakly the Kaggle score (0.75)
#
LRSpe = LogisticRegression()
LRSpe.fit(TrainXdf,TrainYdf)
ScoreTrainLR=LRSpe.score(TrainXdf,TrainYdf)
print ScoreTrainLR
#
submission = pd.DataFrame({
        "PassengerId": TestDF["PassengerId"],
        "Survived": LRSpe.predict(TestXdf)
    })
submission.to_csv(Path+'TitanicSubmit2.csv', index=False)
#
#
#
# Conclusion at this stage : Need to improve featuring, model specification, learning machine parameters.
