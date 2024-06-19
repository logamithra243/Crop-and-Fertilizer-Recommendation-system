import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay,accuracy_score,classification_report
import sklearn
print('The scikit-learn version is {}.'.format(sklearn.__version__))


fertilizer=pd.read_csv("Fertilizer Prediction.csv")


soil_dict={
            'Loamy':1,
            'Sandy':2,
            'Clayey':3,
            'Black':4,
            'Red':5
        }

crop_dict={
            'Sugarcane':1,
            'Cotton':2,
            'Millets':3,
            'Paddy':4,
            'Pulses':5,
            'Wheat':6,
            'Tobacco':7,
            'Barley':8,
            'Oil seeds':9,
            'Ground Nuts':10,
            'Maize':11

        }

fertilizer['Soil_Num']=fertilizer['Soil Type'].map(soil_dict)
fertilizer['Crop_Num']=fertilizer['Crop Type'].map(crop_dict)

fertilizer=fertilizer.drop(['Soil Type','Crop Type'],axis=1)
    

X=fertilizer.drop(['Fertilizer Name'],axis=1)
Y=fertilizer['Fertilizer Name']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

models = {
            'Logistic Regression': LogisticRegression(),
            'Support Vector Machine': SVC(),
            'K-Nearest Neighbors': KNeighborsClassifier(),
            'Decision Tree': DecisionTreeClassifier(),
            'Gradient Boosting': GradientBoostingClassifier(),
            'Extra Trees': ExtraTreeClassifier(),
        }

            
model=DecisionTreeClassifier()
model.fit(X_train,Y_train)

class FertilizerClassifier:
    def __init__(self, model):
        self.model = model
        
    def predict(self, features):
       
        return self.model.predict(features)
def fertilizer_recommendation(temperature,humidity,moisture,nitrogen,potassium,phosphorous,soil_type,crop_type):  
  
    features = np.array([[temperature, humidity, moisture, nitrogen, potassium, phosphorous]])
    

    soil_num = soil_dict.get(soil_type, -1)
    crop_num = crop_dict.get(crop_type, -1)
    

    features_with_soil_crop = np.append(features, [[soil_num, crop_num]], axis=1)
    
  
    classifier = FertilizerClassifier(model) 
    fertilizer_type = classifier.predict(features_with_soil_crop)
    
    return fertilizer_type
def frecommend(T,H,M,N,P,PH,st,ct):
# Example usage
    temperature = T
    humidity = H
    moisture = M
    nitrogen = N
    potassium = P
    phosphorous = PH
    soil_type = st
    crop_type = ct


    recommended_fertilizer = fertilizer_recommendation(temperature, humidity, moisture, nitrogen, potassium, phosphorous, soil_type, crop_type)
    print("Recommended fertilizer:", recommended_fertilizer)
    return recommended_fertilizer