import os

from svcutils.svcutils import Service, get_logger
from webutils.webutils import get_browser_driver


NAME = os.path.splitext(os.path.basename(os.path.realpath(__file__)))[0]
WORK_PATH = os.path.join(os.path.expanduser('~'), f'.{NAME}')

logger = get_logger(path=WORK_PATH, name=NAME)


def target():
    logger.info('running')


def main():
    service = Service(
        target=target,
        work_path=WORK_PATH,
        run_delta=60,
        max_cpu_percent=10,
    )
    service.run_once()


if __name__ == '__main__':
    main()
