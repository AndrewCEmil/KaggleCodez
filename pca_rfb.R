library("randomForest")
library("foreach")
library("doSNOW")
registerDoSNOW(makeCluster(8, type="SOCK"))

train <- read.csv("train.csv", header=TRUE)
test <- read.csv("test.csv", header=TRUE)

labels <- as.factor(train[,1])
train <- train[,-1]
fit <- princomp(train)
#realtrain <- train[names(sorted[420:length(sorted)])]
#for(name in names(sorted[420:length(sorted)])) {
#    train[,name] <- NULL
#}
#for i in length(sdev)
    #if sdev[i] < sorted[lim]
        #train[,i] <- null

#train <- train[400:length(train)]
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

#convert test to the new basis
testm <- data.matrix(test)
testmgood <- testm %*% fit$loadings
print(dim(testmgood))
print(typeof(fit$scores))
print(typeof(testmgood))
#rf <- randomForest(fit$scores[,1:450], labels, xtest=testmgood[,1:450], ntree=1000)
rf <- foreach(ntree = rep(125,8), .combine = combine, .packages = "randomForest") %dopar% randomForest(fit$scores[,1:100], labels, ntree=ntree)
#predictions <- levels(labels)[rf$test$predicted]
predictions <- predict(rf,testmgood[,1:100])
print(typeof(predictions))
print(dim(predictions))

write(predictions, file="rf_pca5.csv", ncolumns=1) 
