import os
import logging 
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('## EVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)
    


''' 
Lambda functions can and should include logging statements, which are written to CloudWatch.

Implement structured logging throughout your applications. Most runtimes provide libraries to help use structured logging. See Lambda Powertools Python Homepage(opens in a new tab) for Python examples, or Lambda Powertools Java Homepage(opens in a new tab) for Java examples. 



Here's an example of logging using the logger function in Python.
'''