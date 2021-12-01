install.packages('glmnet')
library(glmnet)
names(data) <- c('year', 'forest', 'snowfall', 'ghg', 'temp', 'ndsi')
y <- data$ndsi
x <- data.matrix(data[, c('forest', 'snowfall', 'ghg', 'temp')])
cv_model <- cv.glmnet(x, y, alpha = 1)
best_lambda <- cv_model$lambda.min
best_lambda
plot(cv_model)
best_model <- glmnet(x, y, alpha = 1, lambda = best_lambda)
coef(best_model)
y_predicted <- predict(best_model, s = best_lambda, newx = x)
sst <- sum((y - mean(y))^2)
sse <- sum((y_predicted - y)^2)
rsq <- 1 - sse/sst
rsq
