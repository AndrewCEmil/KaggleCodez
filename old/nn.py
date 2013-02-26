import pickle
import os
import sys
from sklearn.ensemble import RandomForestClassifier
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets.classification import ClassificationDataSet
from numpy import genfromtxt, savetxt
import logging

logging.basicConfig(filename='nuralnet.log',level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger('NeuralNet')

basepath = '.'
def main():
    logger.debug('starting')
    print 'starting'
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt(open(basepath + '/train.csv','r'), delimiter=',', dtype='f8')[1:]    
    logger.debug('opened dataset')
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    print target
    logger.debug('about to build data set')
    print 'building dataset'
    cds = ClassificationDataSet(784, target=10, nb_classes=10)
    for i in range(len(target)):
        targetvec = [0 for j in range(10)]
        targetnum = float(target[i])
        targetvec[int(float(target[i]))] = 1
        cds.addSample(train[i], targetvec)
        print i
        print 'adding sample: ' + str(targetnum)
        print targetvec
    logger.debug('about to build network')
    net = buildNetwork(784, 20, 10)
    logger.debug('about to build trainer')
    trainer = BackpropTrainer(net, dataset=cds, momentum=0.1, verbose=True, weightdecay=0.01)
    logger.debug('about to start training')
    print 'training'
    trainer.trainUntilConvergence()
    #save the net
    nfile = open(basepath + '/nn.pickle', 'w')
    pickle.dump(net, nfile)
    nfile.close()
    #run the real test
    logger.debug('opening test set')
    tests = genfromtxt(open(basepath + '/test.csv','r'), delimiter=',', dtype='f8')[1:]
    results = []
    print 'testing'
    for test in tests:
        logger.debug('activating net!')
        res = net.activate(test)
        logger.debug('result: ' + str(res))
        results.append(res)
        
    resultfile = open(basepath + '/nn.output', 'w')
    resultfile.write(str(results))
    print 'done'

if __name__=="__main__":
    print 'STARTING'
    logger.debug('staring')
    main()

