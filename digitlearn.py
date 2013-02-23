import logging

logging.basicConfig(filename='trainer.log',level=logging.DEBUG)
logger = logging.getLogger('training logger')
mind = {}

def train(filename):
    logger.info('training starting...')
    file = open(filename)
    #go line by line
    linecount = 0
    valcount = 0
    logger.info('train about to start looping over training lines')   
    for line in file.readlines():
        if linecount > 0:
            vals = line.split(',')
            target = vals[0]
            logger.debug('new line, target = ' + target)
            if target not in mind.keys():
                logger.debug('got new target: ' + target)
                mind[target] = {}
            logger.info('looping over vals')
            for i in range(1,784):
                if i not in mind[target].keys():
                    mind[target][i] = [0,0]
                if int(vals[i]) > 0:
                    mind[target][i][1] += 1
                else:
                    mind[target][i][0] += 1
        linecount += 1
        logger.debug('finished another line')
        logger.debug('linecount: ' + str(linecount))

    logger.debug('DONE')
    logger.debug(str(mind))
    print mind

train('./train.csv')
