import logging

logger = loggig.getLogger('training logger')
mind = {}

def train(filename):
    logger.info('training starting...')
    file = open(filename)
    #go line by line
    linecount = 0
    valcount = 0
    logger.info('train about to start looping over training lines')   
    for line in file.read_lines():
        vals = line.split(',')
        if linecount == 0:
            #if we are on the first iteration dont count, just generate dict
            for val in vals:
                mind[valcount] = 0
                valcount += 1
        else:
            for val in vals:
                newmindval = mind[i] * (linecount - 1)
                newavg = (newmindval + curval) / linecount
                mind[
            #mind i is now (mind[i] * (count - 1) + curval) /count 

        linecount += 1
            
