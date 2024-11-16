import os

from svcutils.svcutils import get_logger, load_config
from webutils.webutils import get_browser_driver


NAME = os.path.splitext(os.path.basename(os.path.realpath(__file__)))[0]
WORK_PATH = os.path.join(os.path.expanduser('~'), f'.{NAME}')

logger = get_logger(path=WORK_PATH, name=NAME)


def main(config_file):
    config = load_config(config_file)
    print('running')
    logger.info('config value:', config.CONST)
    logger.info('running')
