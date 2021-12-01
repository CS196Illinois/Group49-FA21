import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 
from sklearn import model_selection
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

#define URL where data is located
url = "/Users/abhinav_chinta/Code/Group49-FA21/combinedData.csv"

#read in data
data_full = pd.read_csv(url)

#select subset of data
data = data_full[["Forest Cover Loss in Alaska (Square Meters)", "Snowfall (mm)", "Green House Gas Emissions Per Capita", "Surface Temperature (C)", "NDSI"]]

# Get column names first
names = data_full.columns
# Create the Scaler object
scaler = preprocessing.StandardScaler()
# Fit your data on the scaler object
scaled_df = scaler.fit_transform(data_full)
scaled_df = pd.DataFrame(scaled_df, columns=names)

#view first six rows of data
scaled_df[0:6]
#define predictor and response variables
X = scaled_df[["Forest Cover Loss in Alaska (Square Meters)", "Snowfall (mm)", "Green House Gas Emissions Per Capita", "Surface Temperature (C)"]]
y = scaled_df[["NDSI"]]

#scale predictor variables
pca = PCA()
X_reduced = pca.fit_transform(scale(X))

#define cross validation method
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)

regr = LinearRegression()
mse = []

# Calculate MSE with only the intercept
score = -1*model_selection.cross_val_score(regr, np.ones((len(X_reduced),1)), y, cv=cv, scoring='neg_mean_squared_error').mean()    
mse.append(score)

# Calculate MSE using cross-validation, adding one component at a time
for i in np.arange(1, 6):
    score = -1*model_selection.cross_val_score(regr, X_reduced[:,:i], y, cv=cv, scoring='neg_mean_squared_error').mean()
    mse.append(score)

    
# Plot cross-validation results    
plt.plot(mse)
plt.xlabel('Number of Principal Components')
plt.ylabel('MSE')
plt.title('NDSI')

#calculate percentage of variation explained
np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)

#split the dataset into training (7%) and testing (30%) sets
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.30,random_state=0) 

#scale the training and testing data
X_reduced_train = pca.fit_transform(scale(X_train))
X_reduced_test = pca.transform(scale(X_test))[:,:1]

#train PCR model on training data 
regr = LinearRegression()
regr.fit(X_reduced_train[:,:1], y_train)

#calculate RMSE
pred = regr.predict(X_reduced_test)
print("RMSE value:", np.sqrt(mean_squared_error(y_test, pred)))