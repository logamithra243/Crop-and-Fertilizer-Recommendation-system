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


crop = pd.read_csv("Crop_recommendation.csv")
x = crop[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = crop['label']




x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
models = {
    'Logistic Regression': LogisticRegression(),
    'Support Vector Machine': SVC(),
    'K-Nearest Neighbors': KNeighborsClassifier(),
    'Decision Tree': DecisionTreeClassifier(),
    'Gradient Boosting': GradientBoostingClassifier(),
    'Extra Trees': ExtraTreeClassifier(),
}


dt_classifier_gini = DecisionTreeClassifier(random_state=1,criterion='gini',splitter='best',max_leaf_nodes=None)
dt_classifier_gini.fit(x_train, y_train)
def crecommend(input):

    sample_input = input


    if(dt_classifier_gini.predict(sample_input)):
        print("the recommended crop is:",dt_classifier_gini.predict(sample_input))
        return dt_classifier_gini.predict(sample_input)
    else:
        print("No Suggestion")





