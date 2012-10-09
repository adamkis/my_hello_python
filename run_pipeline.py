#!/usr/bin/python

#import sys;
#sys.path.append("D:\\python\\workspace\\hello_python_copy")


#print(sys.path);


from pipes.lib.pipeline import Pipeline
#import Pipeline

import logging

if __name__=="__main__":
    logging.basicConfig(level='INFO')
    input = {
        'original': 'Hello Python'
    }
    pipeline = Pipeline()
    logging.info('Input is = {0}'.format(input))
    pipeline.run(input)
    logging.info('Input is now = {0}'.format(input))
