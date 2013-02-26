from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt
import logging
logging.basicConfig(filename='copied.log',level=logging.DEBUG)

logger = logging.getLogger('copier')

def main():
    logger.debug('starting')
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt(open('./train.csv','r'), delimiter=',', dtype='f8')[1:]    
    logger.debug('opened dataset')
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]

    logger.debug('about to start training the random forest')
    #create and train the random forest
    #multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    logger.debug('calling fit...')
    rf.fit(train, target)

    logger.debug('about to run the test')
    #run the real test
    test = genfromtxt(open('./test.csv','r'), delimiter=',', dtype='f8')[1:]
    logger.debug('opened test, looping over tests...')
    predicted_probs = [x[1] for x in rf.predict(test)]

    logger.debug('writing out to file')
    savetxt('./submission.csv', predicted_probs, delimiter=',', fmt='%f')

if __name__=="__main__":
    main()

