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
        if linecount >= 0:
            vals = line.split(',')
            target = val[0]
            if target not in mind.keys():
                logger.debug('got new target: ' + target)
                mind[target] = {}
            logger.info('looping over vals')
            for i in range(1,784):
                if i not in mind[target].keys():
                    mind[target][i] = 0
                newmindval = mind[target][i] * (linecount)
                newavg = (newmindval + vals[i]) / (linecount + 1)
                mind[target][i] = newavg
        linecount += 1
        logger.debug('finished another line')

    logger.debug('DONE')
    logger.debug(str(mind))
    print mind

train('./train.csv')
