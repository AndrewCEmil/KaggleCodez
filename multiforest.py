from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from numpy import genfromtxt, savetxt, array
from collections import Counter
import logging
import csv

logging.basicConfig(filename='RFC.log',level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger('RFC')

def main():
    #create the training & test sets, skipping the header row with [1:]
    logger.debug("Startin")
    #dataset = genfromtxt(open('train.csv','r'), delimiter=',', dtype='f8')[1:]    
    csvfile = csv.reader(open('train.csv','r'))
    csvfile.next() #dont need the first one
    targetl = []
    trainl = []
    for row in csvfile:
        targetl.append(row[0])
        trainl.append(row[1:])
    target = array(targetl)
    train = array(trainl)

    """
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    """
    logger.debug("About to create RFC")
    #create and train the random forest
    #multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    rf = RandomForestClassifier(n_estimators=1000, n_jobs=2)

    cv = cross_validation.KFold(len(train), n_folds=5)

    results = []
    forests = []
    logger.debug("About to fit RFC")
    count = 0
    for traincv, testcv in cv:
        logger.debug("fitting")
        forest = rf.fit(train[traincv], target[traincv])
        cls = forest.predict(train[testcv])
        forests.append(forest)
        logger.debug("fit")
        pickle.dump(forest, open('forest' + str(count) + '.pkl', 'wb'))
        count += 1
        """
        logger.debug("resulting")
        good = 0
        bad = 0
        logger.debug('about to compare results')
        for i in range(len(testcv)):
            if target[testcv[i]] != cls[i]:
                logger.info('bad guess, target: ' + target[testcv][i] +', guess: ' + cls[i])
                bad += 1
            else:
                good += 1
        logger.debug('round done, good: ' + str(good) + ', bad: ' + str(bad))
        """

    logger.debug('testing accuracy')
    testpredictions = []
    testresults = []
    for forest in forests:
        testpredictions.append(forest.predict(train))
    good = 0
    bad = 0
    for i in range(len(target)):
        counter = Counter([testpredictions[j][i] for j in range(len(forests))])
        result = counter.most_common()[0][0]
        if result == target[i]:
            good += 1
        else:
            bad += 1
            logger.debug('Bad guess, target: ' + str(target[i]) + ', guess: ' + str(result))

    print good
    print bad
    logger.debug('results, good: ' + str(good) + ', bad: ' + str(bad))
    logger.debug('doing real results now')
    logger.debug('opening test file')
    #test = genfromtxt(open('test.csv','r'), delimiter=',', dtype='f8')[1:]
    csvtest = csv.reader(open('test.csv', 'r'))
    csvtest.next() #dont need header
    datatest = []
    for row in csvtest:
        datatest.append(row)
    #datatest = array(datatestl)
    logger.debug('starting real predicting')
    results =[]

    fullresults = []
    for forest in forests:
        logger.debug('doing a prediction')
        res = forest.predict(datatest)
        fullresults.append(res)
    logger.debug('compiling results')
    for i in range(len(fullresults[0])):
        counter = Counter([fullresults[j][i] for j in range(len(forests))])
        print counter
        result = counter.most_common()[0][0]
        print result
        results.append(result)
        
        """

    for i in range(len(datatest)):
        subresults = []
        logger.debug('doing prediction')
        for forest in forests:
            res = forest.predict(datatest[i])
            subresults.append(res[0])
        #now append the mode of subresults to results
        counter = Counter(subresults) 
        result = counter.most_common()[0][0]
        print result
        results.append(result)
    logger.debug('done with prediction!')
    print results
    """
    outstring = ''
    for res in results:
        outstring += str(res) + '\n'
    outfile = open('multisubmit1000.txt', 'w')
    outfile.write(outstring)

if __name__=="__main__":
    main()
