# makes the random forest submission

library(randomForest)

train <- read.csv("Train.csv")
test <- read.csv("Valid.csv")

targets <- train[,"SalePrice"]
#targets <- as.factor(train[,"SalePrice"])
print(dim(train))
print(dim(test))
goodHeaders <- c("YearMade", "MachineID", "ModelID", "auctioneerID", "MachineHoursCurrentMeter")
realtrain <- train[,goodHeaders]
realtest <- test[,goodHeaders]

realtrain[realtrain != realtrain] <- 0 #removes the NAs
realtrain[is.na(realtrain)] <- 0#also removes the NAs lol
realtest[realtest != realtest] <- 0
realtest[is.na(realtest)] <- 0
targets[is.na(targets)] <- 0
targets[targets != targets] <- 0
#targs <- na.omit(targets)
#realtrain <- na.omit(realtrain)
#realtest <- na.omit(realtest)

realtrain2 <- realtrain[100000:length(targs2),]
targs2 <- targs[100000:length(targs2)]
#rf <- randomForest(realtrain, targets, ntree=100)
print(length(targs2))
print(dim(realtrain2))
rf2 <- randomForest(realtrain2, targs2, ntree=100)
results <- predict(rf2, realtest)
predictions <- results

write(predictions, file="rfout.csv", ncolumns=1)
