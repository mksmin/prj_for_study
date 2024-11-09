from loguru import logger
from time import sleep


def foo():
    logger.info('Start sync foo')
    sleep(1)
    logger.info('Finish sync foo')


def bar():
    logger.info('Start sync bar')
    sleep(1)
    logger.info('Finish sync bar')


def run_main():
    foo()
    bar()


def main():
    logger.info('Starting main')
    run_main()
    logger.warning('finished main')


if __name__ == '__main__':
    main()
