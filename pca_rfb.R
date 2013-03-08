library(randomForest)

train <- read.csv("train.csv", header=TRUE)
test <- read.csv("test.csv", header=TRUE)

labels <- as.factor(train[,1])
train <- train[,-1]
print(dim(train))
print(typeof(train))

fit <- princomp(train)
for(i in 1:length(fit$sdev)) {
    if(fit$sdev[i] == 0) {
        train <- train[,-i] 
        test <- test[,-i]
    }
}


print(dim(train))


rf <- randomForest(train, labels, xtest=test, ntree=1000)
predictions <- levels(labels)[rf$test$predicted]

write(predictions, file="rf_benchmark.csv", ncolumns=1) 
