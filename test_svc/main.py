import os
import time

from svcutils.service import get_logger


NAME = 'test_svc'
WORK_PATH = os.path.join(os.path.expanduser('~'), f'.{NAME}')

logger = get_logger(path=WORK_PATH, name=NAME)


def main():
    logger.info('started')
    time.sleep(3)
    logger.info('stopped')


if __name__ == '__main__':
    main()
