# makes the random forest submission

library(randomForest)

train <- read.csv("Train.csv")
test <- read.csv("Valid.csv")

targets <- train[,"SalePrice"]
#targets <- as.factor(train[,"SalePrice"])
print(dim(train))
print(dim(test))
goodHeaders <- c("YearMade", "MachineID", "ModelID", "auctioneerID", "MachineHoursCurrentMeter", "saledate")
train <- train[,goodHeaders]
test <- test[,goodHeaders]

train[,"saledate"] <- as.Date(train[,"saledate"],"%m/%d/%Y")
test[,"saledate"] <- as.Date(test[,"saledate"], "%m/%d/%Y")
train[train != train] <- 0 #removes the NAs
train[is.na(train)] <- 0#also removes the NAs lol
test[test != test] <- 0
test[is.na(test)] <- 0
targets[is.na(targets)] <- 0
targets[targets != targets] <- 0
train[,"YearMade"] <- as.Date(train[,"YearMade"],"%Y")
test[,"YearMade"] <- as.Date(test[,"YearMade"],"%Y")

#targs <- na.omit(targets)
#train <- na.omit(train)
#test <- na.omit(test)

#train2 <- train[100000:length(targs2),]
#targs2 <- targs[100000:length(targs2)]
rf <- randomForest(train, targets, ntree=10)
#rf2 <- randomForest(realtrain2, targs2, ntree=1000)
results <- predict(rf, test)
write(results, file="sub5.csv", ncolumns=1)
