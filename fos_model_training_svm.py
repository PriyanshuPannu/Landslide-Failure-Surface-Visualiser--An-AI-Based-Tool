import sklearn
import pickle
import pandas as pd
from sklearn.svm import SVR

data=pd.read_excel("data.xlsx")
data=data.dropna()

input_feature_x=data.iloc[:,0:6].values
output_y=data.iloc[:,6].values
model = SVR(kernel = 'rbf')
print("Training started.....")
model.fit(input_feature_x, output_y)

filename = 'fos_model.sav'
pickle.dump(model, open(filename, 'wb'))
print("Training completed!!")
