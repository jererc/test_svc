import os
import time

from svcutils.service import get_logger, load_config


NAME = os.path.splitext(os.path.basename(os.path.realpath(__file__)))[0]
WORK_PATH = os.path.join(os.path.expanduser('~'), f'.{NAME}')

logger = get_logger(path=WORK_PATH, name=NAME)


def main():
    logger.info('started')
    time.sleep(3)
    logger.info('stopped')


if __name__ == '__main__':
    main()
