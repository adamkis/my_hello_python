import logging

import datetime

"""
Step for duplicating the input string and adding date at the end
"""
class Step(object):

    def run(self, input):
        logging.info('Duplicating')

        # Adding new element to input:
        # the original input duplicated and concatenated with current date
        input['DUPLICATED'] = input['original'] + " " + input['original'] + " " + datetime.datetime.now().strftime("%Y-%m-%d")
