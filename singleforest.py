from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from numpy import genfromtxt, savetxt, array
from collections import Counter
import logging
import csv
import pickle

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
    rf = RandomForestClassifier(n_estimators=1000, n_jobs=8)

    results = []
    logger.debug("About to fit RFC")
    forest = rf.fit(train, target)
    logger.debug('pickling...')
    pickle.dump(forest, open("singleforest.pkl", 'wb'))
    logger.debug('opening test file')
    #test = genfromtxt(open('test.csv','r'), delimiter=',', dtype='f8')[1:]
    csvtest = csv.reader(open('test.csv', 'r'))
    csvtest.next() #dont need header
    datatest = []
    for row in csvtest:
        datatest.append(row)
    #datatest = array(datatestl)
    logger.debug('starting real predicting')
    results = forest.predict(datatest)
    logger.debug('done with prediction!')
    outstring = ''
    for res in results:
        outstring += str(res) + '\n'
    outfile = open('submission2.txt', 'w')
    outfile.write(outstring)

if __name__=="__main__":
    main()
