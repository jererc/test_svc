import argparse
import os
import sys
import time

from svcutils.service import get_logger


NAME = 'test_svc'
WORK_PATH = os.path.join(os.path.expanduser('~'), f'.{NAME}')

logger = get_logger(path=WORK_PATH, name=NAME)


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='cmd')
    collect_parser = subparsers.add_parser('collect')
    collect_parser.add_argument('--path')
    collect_parser.add_argument('--daemon', action='store_true')
    collect_parser.add_argument('--task', action='store_true')
    collect_parser.add_argument('--no-headless', action='store_true')
    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        sys.exit()
    return args


def main():
    args = parse_args()
    logger.info(f'running with args: {args}')
    time.sleep(3)
    logger.info('ended')


if __name__ == '__main__':
    main()
