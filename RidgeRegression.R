library(plyr)
library(readr)
library(dplyr)
library(caret)
library(ggplot2)
library(repr)

dat = read.csv("/Users/Viven/Group49CSVData/combinedDataNoYear.csv")
glimpse(dat)

set.seed(100)

index = sample(1:nrow(dat), 0.7*nrow(dat)) 

train = dat[index,] # Create the training data 
test = dat[-index,] # Create the test data

dim(train)
dim(test)

cols = c('Forest.Cover.Loss.in.Alaska..Square.Meters.', 'Snowfall..mm.', 'Green.House.Gas.Emissions.Per.Capita', 'Surface.Temperature..C.')

pre_proc_val <- preProcess(train[,cols], method = c("center", "scale"))

train[,cols] = predict(pre_proc_val, train[,cols])
test[,cols] = predict(pre_proc_val, test[,cols])

summary(train)

lr = lm(NDSI ~ Forest.Cover.Loss.in.Alaska..Square.Meters. + Snowfall..mm. + Green.House.Gas.Emissions.Per.Capita + Surface.Temperature..C., data = train)
summary(lr)

cols_reg = c('Forest.Cover.Loss.in.Alaska..Square.Meters.', 'Snowfall..mm.', 'Green.House.Gas.Emissions.Per.Capita', 'Surface.Temperature..C.', 'NDSI')

dummies <- dummyVars(NDSI ~ ., data = dat[,cols_reg])

train_dummies = predict(dummies, newdata = train[,cols_reg])

test_dummies = predict(dummies, newdata = test[,cols_reg])

print(dim(train_dummies)); print(dim(test_dummies))

install.packages("glmnet", repos = "https://cran.us.r-project.org")

library(glmnet)

x = as.matrix(train_dummies)
y_train = train$NDSI

x_test = as.matrix(test_dummies)
y_test = test$NDSI

lambdas <- 10^seq(2, -3, by = -.1)
ridge_reg = glmnet(x, y_train, nlambda = 25, alpha = 0, family = 'gaussian', lambda = lambdas)

summary(ridge_reg)

cv_ridge <- cv.glmnet(x, y_train, alpha = 0, lambda = lambdas)
optimal_lambda <- cv_ridge$lambda.min
optimal_lambda

# Compute R^2 from true and predicted values
eval_results <- function(true, predicted, df) {
    SSE <- sum((predicted - true)^2)
    SST <- sum((true - mean(true))^2)
    R_square <- 1 - SSE / SST
    RMSE = sqrt(SSE/nrow(df))
  
    
    # Model performance metrics
data.frame(
  RMSE = RMSE,
  Rsquare = R_square
)
}

# Prediction and evaluation on train data
predictions_train <- predict(ridge_reg, s = optimal_lambda, newx = x)
eval_results(y_train, predictions_train, train)

# Prediction and evaluation on test data
predictions_test <- predict(ridge_reg, s = optimal_lambda, newx = x_test)
eval_results(y_test, predictions_test, test)