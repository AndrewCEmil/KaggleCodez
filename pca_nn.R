library("nnet")
library("foreach")

train <- read.csv("train.csv", header=TRUE)
test <- read.csv("test.csv", header=TRUE)

labels <- as.factor(train[,1])
train <- train[,-1]
fit <- princomp(train)

testm <- data.matrix(test)
testmgood <- testm %*% fit$loadings

print(dim(testmgood))
print(typeof(fit$scores))
print(typeof(testmgood))

nn <- nnet(fit$scores[,1:40], as.numeric(labels), size=10)
predictions <- predict(nn,testmgood[,1:40])

print(typeof(predictions))
print(dim(predictions))

write(predictions, file="nn_pca2.csv", ncolumns=1) 
