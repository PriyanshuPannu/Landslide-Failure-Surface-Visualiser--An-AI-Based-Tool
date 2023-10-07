import sklearn
import pickle
import pandas as pd
from sklearn.svm import SVR

data=pd.read_excel("data.xlsx")

input_feature_x=data.iloc[:,0:2].values
output_y=data.iloc[:,2].values
model = SVR(kernel = 'rbf')
model.fit(input_feature_x, output_y)

filename = 'fos_model.sav'
pickle.dump(model, open(filename, 'wb'))