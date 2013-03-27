library(randomForest)

train <- read.csv("train.csv", header=TRUE)
test <- read.csv("test.csv", header=TRUE)

labels <- as.factor(train[,1])
train <- train[,-1]
fit <- princomp(train)

print(sum(sorted[1:420]))
print(sum(sorted[420:length(sorted)]))
#print(dim(train))
#realtrain <- train[names(sorted[420:length(sorted)])]
#for(name in names(sorted[420:length(sorted)])) {
#    train[,name] <- NULL
#}
#for i in length(sdev)
    #if sdev[i] < sorted[lim]
        #train[,i] <- null

#train <- train[420:length(train)]
#print(dim(train))
#print(dim(test))
#test <- test[420:length(test)]
#print(dim(test))
#for(i in 1:length(fit$sdev)) {
#    if(fit$sdev[i] <= sorted[420]) {
#        train <- train[,-i]
#        test <- test[,-i]
#        count[1] <- count[1] + 1
#    }
#}

rf <- randomForest(train, labels, xtest=test, ntree=1000)
predictions <- levels(labels)[rf$test$predicted]

write(predictions, file="rf_pca.csv", ncolumns=1) 
