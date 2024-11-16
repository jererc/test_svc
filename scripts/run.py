import os

from svcutils.service import Service
from test_svc.test_svc import WORK_PATH, main


CONFIG_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
    'user_settings.py')


def run(config_file=CONFIG_FILE):
    Service(
        target=main,
        args=(config_file,),
        work_path=WORK_PATH,
        run_delta=1,
    ).run_once()


if __name__ == '__main__':
    run()
