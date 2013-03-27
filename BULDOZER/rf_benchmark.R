# makes the random forest submission

library(randomForest)

train <- read.csv("Train.csv")
test <- read.csv("Valid.csv")

labels <- as.factor(train[,"SalePrice"])
#train <- train[,-1] no header for bulldozers
print(dim(train))
print(dim(test))
goodHeaders <- c("YearMade", "MachineID", "ModelID", "auctioneerID", "MachineHoursCurrentMeter")
realtrain <- train[,goodHeaders]

realtrain[realtrain != realtrain] <- 0
realtrain[is.na(realtrain)] <- 0
realtest <- test[,goodHeaders]
realtest[realtest != realtest] <- 0
realtest[is.na(realtest)] <- 0

rf <- randomForest(realtrain, labels, ntree=100)
results <- predict(rf, realtest)
names(results)
predictions <- results

write(predictions, file="rf_benchmark.csv", ncolumns=1)
